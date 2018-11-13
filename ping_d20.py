#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>
# (c) 2016, Toshio Kuratomi <tkuratomi@ansible.com>
# (c) 2018, Bianca Henderson <beeankha@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'core'}

DOCUMENTATION = '''
---
module: ping_d20
version_added: historical
short_description: Try to connect to host, verify a usable python and return C(pong) and the result of a random d20 roll on success
description:
   - A trivial test module, this module always returns C(pong) on successful
     contact as well as a d20 roll. It does not make sense in playbooks, but it is useful from
     C(/usr/bin/ansible) to verify the ability to login and that a usable Python is configured.
   - This is NOT ICMP ping, this is just a trivial test module that requires Python on the remote-node.
   - For Windows targets, use the M(win_ping) module instead.
   - For Network targets, use the M(net_ping) module instead.
notes:
   - For Windows targets, use the M(win_ping) module instead.
   - For Network targets, use the M(net_ping) module instead.
options:
  data:
    description:
      - Data to return for the C(ping) return value.
      - If this parameter is set to C(crash), the module will cause an exception.
    default: pong
author:
    - Ansible Core Team
    - Michael DeHaan
'''

EXAMPLES = '''
# Test we can logon to 'webservers' and execute python with json lib.
# ansible webservers -m ping_d20

# Example from an Ansible Playbook
- ping_d20:

# Induce an exception to see what happens
- ping_d20:
    data: crash
'''

RETURN = '''
ping_d20:
    description: value provided with the data parameter
    returned: success
    type: string
    sample: pong
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping_d20=module.params['data'],
    )

    module.exit_json(**result)


if __name__ == '__main__':
    main()

# d20 script content is below:
from random import randint
import sys
import os

print('Input any key to roll!')
do_roll = input()

roll = (randint(1,20))
if roll == 1:
    print(f"You rolled a {roll}, CRITICAL MISS!")
elif roll == 20:
    print("You rolled a NATURAL TWENTY!")
else:
    print(f"Your roll is {roll}.")

os.execl(sys.executable, sys.executable, *sys.argv)
