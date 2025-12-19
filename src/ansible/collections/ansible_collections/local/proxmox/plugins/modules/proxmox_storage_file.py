#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.local.proxmox.plugins.module_utils.proxmox import proxmox_auth_argument_spec

__metaclass__ = type

DOCUMENTATION = r"""
---
module: my_test

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@yourGitHubHandle)
"""

EXAMPLES = r"""
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
"""

RETURN = r"""
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
"""


def run_module():
    module_args = proxmox_auth_argument_spec()

    node_args = dict(
        # Required options
        content=dict(required=True, choices=["iso", "vztmpl", "import"]),
        filename=dict(required=True),
        node=dict(required=True),
        storage=dict(required=True),
        url={},
        file={},

        # Optional options
        checksum={},
        checksum_algorithm=dict(
            choices=["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
        ),
        compression={},
        verify_certificates=dict(type="bool"),
    )

    module_args.update(node_args)

    module = AnsibleModule(
        argument_spec=module_args,
        required_one_of=[
            ('api_password', 'api_token_id'),
            ('url', 'file')
        ],
        required_together=[('api_token_id', 'api_token_secret')],
        mutually_exclusive=[('url', 'file')],
        supports_check_mode=True,
    )

    result = {"changed": False}

    module.exit_json(msg="Hello world", **result)


def main():
    run_module()


if __name__ == "__main__":
    main()
