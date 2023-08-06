#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019-2020, Gluware Inc.

# Gluware Ansible Inventory Plugin

ANSIBLE_METADATA = {'metadata_version': '1.2.0',
                    'status': ['released'],
                    'supported_by': 'Gluware Inc'}

DOCUMENTATION = '''
    name: glu_devices
    plugin_type: inventory
    short_description: Gluware Control Inventory Source
    description:
        - Get inventory from Device Manager in Gluware Control.
        - Uses a YAML configuration file that ends with C(glu_devices.yml) for the host of the Gluware Control system and the userName and password to that Gluware Control system.
        - If there are any Gluware Control custom attributes with values on the devices that start with 'ansible_var_' then those variables will be added to the host (minus the 'ansible_var_' part).
        - If there is a Gluware Control custom field of 'ansible_connection' on the device then that will be the connection for that host.  Otherwise 'network_cli' will be the connection.
        - If there is a Gluware Control custom field of 'ansible_network_os' on the device then that will be the 'ansible_network_os' for that hose.  Otherwise 'discoveredOs' (if available) will be the 'ansible_network_os' for that host.
    version_added: '2.8'
    author:
        - John Anderson
    options:
        plugin:
            description: This tells ansible (through the auto inventory plugin) this is a source file for the glu_devices plugin.
            required: True
            choices: ['glu_devices']
        host:
            description: The network address or name of your Gluware Control system host.
            type: string
            env:
                - name: GLU_CONTROL_HOST
            required: True
        username:
            description: The user used to access devices (inventories) from the Gluware Control system.
            type: string
            env:
                - name: GLU_CONTROL_USERNAME
            required: True
        password:
            description: The password for the username of the Gluware Control system.
            type: string
            env:
                - name: GLU_CONTROL_PASSWORD
            required: True
        trust_any_host_https_certs:
            description: 
                - Specify whether Ansible should verify the SSL certificate of https calls on the Control Gluware system host.
                - This is used for self-signed Gluware Control Systems.
            type: bool
            default: False
            env:
                - name: GLU_CONTROL_TRUST_ANY_HOST_HTTPS_CERTS
            required: False
            aliases: [ verify_ssl ]
        compose:
            description: 
                - Add a host variable from Jinja2 expressions.
                - The keys of the dictionary are the host variables.
                - The values of the dictionary are Jinja 2 exzpresions.
                - The Jinja 2 expressions can use Gluware Control device attributes (including custom attributes).
            type: dict
            required: False
        groups:
            description: 
                - Define groups for a host based on Jinja2 conditionals.
                - The keys of the dictionary are the groups.
                - The values of the dictionary are Jinja 2 conditionals where a truthful condition causes current host be in the group specified in the key.
                - The Jinja 2 conditionals can use Gluware Control device attributes (including custom attributes).
            type: dict
            required: False
        keyed_groups:
            description: 
                - Define groups for a host from Jinja2 expresions.
                - Each list item is a dictionary with the following keys.
                - (key) a required Jinga 2 expression
                - (prefix) a optional text to prefix the value of the (key) expression. The default is a empty string.
                - (separator) a optional text to separate the (prefix) and (key) expression. The default is a underscore '_'.
                - (parent_group) a optional text to specify the parent group for this group.
                - The Jinja 2 expressions can use Gluware Control device attributes (including custom attributes).
            type: list
            required: False
        variable_map:
            description: 
                - (DEPRECATED) use the 'compose' option. 'compose' eclipses the functionality of this option. 
                - This option is a dictionary where the keys are variable names of Gluware Control devices attributes (including custom attributes).
                - The values of the dictionary are strings that specify the variable names on the host in Ansible.
            type: dict
            required: false
'''

EXAMPLES = r'''
    #
    # Minimal Configuration for *glu_devices.yml files where no GLU_CONTROL_* environment variables are defined.
    plugin: glu_devices
    host: 'https://10.0.0.1'
    username: <user name in Gluware Control system for device API calls>
    password: <password for user name>

    #
    # Configuration to use a Gluware Control system that has a self-signed certificate.
    plugin: glu_devices
    host: 'https://10.0.0.1'
    username: <user name in Gluware Control system for device API calls>
    password: <password for user name>
    trust_any_host_https_certs: True

    #
    # Configuration to map the Gluware device attribute 'discoveredSerialNumber' to the Ansible host variable 'serial_num'
    plugin: glu_devices
    host: 'https://10.0.0.1'
    username: <user name in Gluware Control system for device API calls>
    password: <password for user name>
    trust_any_host_https_certs: True
    compose:
        serial_num : discoveredSerialNumber

    #
    # Configuration to have Gluware Control devices grouped under the value custom attribute 'Area' where 'Area' is also the parent group.
    plugin: glu_devices
    host: 'https://10.0.0.1'
    username: <user name in Gluware Control system for device API calls>
    password: <password for user name>
    trust_any_host_https_certs: True
    keyed_groups:
        - key: Area
          separator: ''
          parent_group: Area

    #
    # Configuration to have Gluware Control devices grouped under 'front_devices' where the text 'Front' is found in the 'Area' custom attribute.
    plugin: glu_devices
    host: 'https://10.0.0.1'
    username: <user name in Gluware Control system for device API calls>
    password: <password for user name>
    trust_any_host_https_certs: True
    groups:
        front_devices: "'Front' in Area"

'''

import os
import re
import json
import pprint

from ansible.module_utils.urls import Request, urllib_error, ConnectionError, socket, httplib
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_native, to_text
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable

# Python 2/3 Compatibility
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

# Mapping between the discoveredOs variable and ansible_network_os    
DiscoveredOSToAnsibleNetworkOS = {
    'NX-OS' : 'nxos',
    'IOS/IOS XE' : 'ios',
}  
  
class InventoryModule(BaseInventoryPlugin, Constructable):
  NAME = 'glu_devices'

  def __init__(self):
      super(InventoryModule, self).__init__()

      self.group_prefix = 'glu_'


  @staticmethod  
  def _convertGroupName(group_name):
      '''
        Convert group names to valid characters that can be a directory on a file system.
      '''
      group_name = re.sub('[^a-zA-Z0-9]', '_', group_name)
      return group_name

  def _api_call(self, requestHandler, api_url, api_url_2):
    '''
        Make the api call for the api_url with the requestHandler and on success return object with data.
        If api_url fails then try api_url_2.
    '''
    # Make the actual api call.
    try:
        response = requestHandler.get(api_url)
    except (ConnectionError, httplib.HTTPException, socket.error, urllib_error.URLError):
        # If the first call returns a URL error then try this second call.
        try:
            response = requestHandler.get(api_url_2)
        except (ConnectionError, httplib.HTTPException, socket.error, urllib_error.URLError) as e2:
            errorMsg = 'Gluware Control call2 failed: {msg}'.format(msg=e2)
            raise AnsibleError(to_native(errorMsg))
    
    # Read in the JSON response to a object.
    try: 
        readResponse = response.read()
        objResponse = json.loads(readResponse)
        return objResponse
    except (ValueError, TypeError) as e:
        errorMsg = 'Gluware Control call response failed to be parsed as JSON: {msg}'.format(msg=e)
        raise AnsibleError(to_native(errorMsg))

  def _updateInventoryObj(self, api_devices):
    '''
        Take the api_devices object and update the self.inventory object
    '''
    # pprint.pprint(api_devices)

    option_compose = self.get_option('compose')
    option_groups = self.get_option('groups')
    option_keyed_groups = self.get_option('keyed_groups')

    # Default ansible_connection to 'network_cli'.  This if for paramiko (used in Ansible Networking) instead of the default 'ssh' (used in normal Ansible)
    self.inventory.set_variable('all', 'ansible_connection', 'network_cli')

    for device_obj in api_devices:
        device_name = device_obj.get('name')
        # Set the glu_device_id to work with the gluware ansible modules.
        glu_device_id = device_obj.get('id')


        # Try to used the discoveredOs from the device. 
        #   If that is not found the try to use the ansible_network_os on the device.
        network_OS = ''
        discoveredOS = device_obj.get('discoveredOs')
        # print "DiscoveredOS: ", discoveredOS
        if discoveredOS: network_OS = DiscoveredOSToAnsibleNetworkOS.get(discoveredOS)
        if not network_OS:
            network_OS = device_obj.get('ansible_network_os')
        if not network_OS:
            # Since there was no mapping or overriding ansible_network_os property use the discoveredOS directly.
            # The idea behind this logic is maybe the discoveredOS will adopt the ansible convention of network os id.
            network_OS = discoveredOS

        # print "network_OS: ", network_OS
    
        # In case the ansible connection is overridden.
        ansible_connection = device_obj.get('ansible_connection')
        if device_name:
            connection_info_obj = device_obj.get('connectionInformation')
            if connection_info_obj:
                connect_ip = connection_info_obj.get('ip')
                connect_port = connection_info_obj.get('port')
                connect_username = connection_info_obj.get('userName')
                connect_password = connection_info_obj.get('password')
                connect_enable_password = connection_info_obj.get('enablePassword')

                # Special logic if password and enable password is not available.
                if not connect_password: connect_password = device_obj.get('x_word')
                if not connect_enable_password: connect_enable_password = device_obj.get('x_e_word')

                # TODO: add logic for proxy objects. Paramiko might support proxy logic.


                # Check that that the device is not already added by some other inventory plugin.
                if not self.inventory.get_host(device_name):
                    # If there is a network_OS then use that as a group and assign that host to the group.
                    group = None
                    if network_OS:
                        group = self._convertGroupName(network_OS)
                        self.inventory.add_group(group)
                    host = self.inventory.add_host(device_name, group, connect_port)

                    # Set the ansible_network_os no matter what.  This is so it is not undefined in the playbook.
                    self.inventory.set_variable(host,'ansible_network_os', network_OS)
                    
                    if connect_ip: self.inventory.set_variable(host, 'ansible_host', connect_ip)
                    if connect_username: self.inventory.set_variable(host,'ansible_user', connect_username)
                    if connect_password: self.inventory.set_variable(host,'ansible_password', connect_password)
                    if ansible_connection: self.inventory.set_variable(host,'ansible_connection', ansible_connection)

                    # Gluware device id is set on this inventory item to be used with other Gluware modules.
                    if glu_device_id: self.inventory.set_variable(host, 'glu_device_id', glu_device_id)

                    # For any device_obj properties that start with 'ansible_var_' add that variable (minus the 'ansible_var_' part) to the host.
                    for propName, propVal in device_obj.items():
                        if propName.startswith('ansible_var_'):
                            ansibleVar = propName[len('ansible_var_'):]
                            if ansibleVar: self.inventory.set_variable(host, ansibleVar, propVal)

                    # If there is a variable_map then look for the variable in the device_obj and assign it to the ansibleVarName to the host.
                    variableMap = self.get_option('variable_map')
                    if variableMap:
                        for gluPropName, ansibleVarName in variableMap.items():
                            devicePropVal = device_obj.get(gluPropName)
                            if devicePropVal: self.inventory.set_variable(host, ansibleVarName, devicePropVal)
            if option_compose:
                self._set_composite_vars(option_compose, device_obj, device_name)
            if option_groups:
                self._add_host_to_composed_groups(option_groups, device_obj, device_name)
            if option_keyed_groups:
                self._add_host_to_keyed_groups(option_keyed_groups, device_obj, device_name)

    # Finalize inventory
    self.inventory.reconcile_inventory()


  def verify_file(self, path):
    '''
        Called by ansible first to verify if the path is valid for this inventory plugin.
    '''
    if super(InventoryModule, self).verify_file(path):
        # base class verifies that file exists and is readable by current user
        if path.endswith('glu_devices.yml'):
            return True
    return False


  def parse(self, inventory, loader, path, cache=True):
    '''
        Called by ansible second to fill in the passed inventory object for the specified path.
        The self.verify_file() was called first so state could have been set on the self object there
        that can be used here.
    '''

    # Use the super classes functionality to setup the self object correcly.
    super(InventoryModule, self).parse(inventory, loader, path)
    self._read_config_data(path)

    # Setup for the API call for the data for the inventory.    
    api_host = self.get_option('host')
    if (not api_host): 
        api_host = os.environ.get('GLU_CONTROL_HOST')

    if not re.match('(?:http|https)://', api_host):
        api_host = 'https://{host}'.format(host=api_host)

    # This api call is for Gluware Control 3.6 and greater.
    apiURL_1 = urljoin(api_host, '/api/devices?showPassword=true')
    # This api call is for Gluware Control 3.5.
    apiURL_2 = urljoin(api_host, '/api/devices')
    
    api_user = self.get_option('username')
    if (not api_user):
        api_user = os.environ.get('GLU_CONTROL_USERNAME')

    api_password = self.get_option('password')
    if (not api_password):
        api_password = os.environ.get('GLU_CONTROL_PASSWORD')

    api_trust_https = self.get_option('trust_any_host_https_certs')
    if (not api_trust_https):
        api_trust_https = os.environ.get('GLU_CONTROL_TRUST_ANY_HOST_HTTPS_CERTS')

    requestHandler = Request(url_username=api_user, 
                            url_password=api_password, 
                            validate_certs=not(api_trust_https), 
                            force_basic_auth=True)

    # Make the API Call for the data for the inventory.
    api_devices = self._api_call(requestHandler, apiURL_1, apiURL_2)

    # Process the API data into the inventory object.
    self._updateInventoryObj(api_devices)

