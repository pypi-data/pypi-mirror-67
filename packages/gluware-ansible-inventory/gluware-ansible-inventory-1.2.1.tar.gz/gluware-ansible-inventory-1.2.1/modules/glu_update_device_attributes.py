#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Gluware Inc.

ANSIBLE_METADATA = {'metadata_version': '1.2.0',
                    'status': ['stableinterface'],
                    'supported_by': 'Gluware Inc'}

DOCUMENTATION = '''
    module: glu_update_device_attributes
    short_description: Update device attributes on a Gluware Device
    description:
        - For the current Gluware device update specified attribute values in Gluware Control using the glu_device_id.
        - >
          Note: If an error of 'HTTP Error 400: Bad Request' is displayed then possibly the playbook task is trying to set a
          read only attribute or a non existent attribute.
    version_added: '2.8'
    author:
        - John Anderson
    options:
        glu_connection_file:
            description:
                - Reference to a yaml file with connection information to the Gluware Control system.
                - The glu_devices inventory file (*glu_devices.yml) can be used for this file.
                - The keys of 'host', 'username', 'password', or 'trust_any_host_https_certs' are 
                  read from the this file for connection information.
                - For a key not found in the connection file then the environment variable is used, if available.
                - If the glu_connection_file is not specified then the environment variables are used, if available.
                - If there is no connection information then this module will error out.
            env:
                - name: GLU_CONTROL_HOST
                - name: GLU_CONTROL_USERNAME
                - name: GLU_CONTROL_PASSWORD
                - name: GLU_CONTROL_TRUST_ANY_HOST_HTTPS_CERTS
            type: string
            required: False
        glu_device_id:
            description:
                - Id in Gluware Control for the device.
                - The glu_devices inventory plugin automatically supplies this variable.
            type: string
            required: True
        data:
            description:
                - Attributes with values to update to.
            type: dict
            required: True
'''

EXAMPLES = r'''
    #
    # Update Gluware Control attribute (including custom attributes) values for the current device
    #
    - name: Update the custom attribute playbook_date with the current date in Gluware Control
      glu_update_device_attributes:
        glu_connection_file : "{{ inventory_file }}"
        glu_device_id: "{{ glu_device_id }}"
        data:
          playbook_date : "{{ lookup('pipe','date +%Y-%m-%d-%H-%M-%S') }}"

'''

import re
import json
import sys
import os
import pprint
import yaml

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import Request, urllib_error, ConnectionError, socket, httplib

# Python 2/3 Compatibility
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

def run_module():

    # Module parameters
    module_args = dict(
        glu_device_id=dict(type='str', required=True),
        glu_connection_file=dict(type='str', required=False),
        data=dict(type='dict', required=True)
    )

    # Initialize the AnsibleModule to use in communication from and to the
    # code (playbook, etc) interacting with this module.
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    glu_connection_file = module.params.get('glu_connection_file')

    # Figure out the Gluware Control connection information.
    api_dict = {
        'host' : os.environ.get('GLU_CONTROL_HOST'),
        'username' : os.environ.get('GLU_CONTROL_USERNAME'),
        'password' : os.environ.get('GLU_CONTROL_PASSWORD'),
        'trust_any_host_https_certs' : os.environ.get('GLU_CONTROL_TRUST_ANY_HOST_HTTPS_CERTS'),
    }

    if (glu_connection_file) :
        # Try to read the inventory file for the connection information.
        file_err = ""
        if (os.path.exists(glu_connection_file)):
            try:
                with open(glu_connection_file, "r") as file:
                    file_dict = yaml.safe_load(file)

                    # Merge the file values to the api_dict.
                    # This allows the environment vars to be overriden by the file values, if the environment values exist.
                    api_dict.update(file_dict)
            except IOError as io_err:
                file_err = "File error: "+io_err
                #Do nothing..

    # Test to see if the api_dict has all the required properties.
    if (not api_dict.get('host')):
        module.fail_json(msg="Missing 'host' or GLU_CONTROL_HOST to make Gluware API call.", changed=False)
    if (not api_dict.get('username')):
        module.fail_json(msg="Missing 'username' or GLU_CONTROL_USERNAME to make Gluware API call.", changed=False)
    if (not api_dict.get('password')):
        module.fail_json(msg="Missing 'password' or GLU_CONTROL_PASSWORD to make Gluware API call.", changed=False)
         
    # All the required values exist, so use the information in the file for the connection information.
    api_host = api_dict.get('host')

    # Make sure there is a http or https preference for the api_host
    if not re.match('(?:http|https)://', api_host):
        api_host = 'https://{host}'.format(host=api_host)

    # Make sure the Content-Type is set correctly.. otherwise it defaults to application/x-www-form-urlencoded which
    # causes a 400 from Gluware Control
    http_headers = {
        'Content-Type' : 'application/json'
    }

    # Create the request_handler to make the calls with.
    request_handler = Request(url_username=api_dict['username'], 
                            url_password=api_dict['password'], 
                            validate_certs=not(api_dict.get('trust_any_host_https_certs', False)), 
                            force_basic_auth=True,
                            headers=http_headers)

    # Default result JSON object
    result = dict(
        changed=False
    )

    glu_device_id = module.params.get('glu_device_id')
    api_data = module.params.get('data')

    # This api call is for Gluware Control.
    api_url_1 = urljoin(api_host, '/api/devices/'+glu_device_id)
    
    # Create the body of the request.
    http_body = json.dumps(api_data)

    # Make the actual api call.
    try:
        response = request_handler.put(api_url_1, data=http_body)
    except (ConnectionError, httplib.HTTPException, socket.error, urllib_error.URLError) as e2:
        error_msg = 'Gluware Control call failed: {msg}'.format(msg=e2)
        if ('Bad Request' in error_msg):
            error_msg = 'Invalid attribute(s) being updated on device or invalid value(s) for the attribute(s). Data provided: '+http_body
        module.fail_json(msg=error_msg, changed=False)

    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()

