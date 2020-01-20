#!/usr/bin/python
# coding: utf-8 -*-
#
# (c) 2020, Bianca Henderson <beeankha@gmail.com>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}


DOCUMENTATION = '''
---
module: dice_module
author: "Bianca Henderson (@bizonka)"
version_added: "2.9"
short_description: The worst way to roll some dice!
description:
    - A way to roll digital dice via Ansible playbook. Currently you can only
    roll one at a time.
options:
    roll_d4:
      description:
        - The command to roll a d4 die.
      required: False
      type: bool
      default: False
    roll_d6:
      description:
        - The command to roll a d6 die.
      required: False
      type: bool
      default: False
    roll_d12:
      description:
        - The command to roll a d12 die.
      required: False
      type: bool
      default: False
    roll_d20:
      description:
        - The command to roll a d20 die.
      required: False
      type: bool
      default: False
'''

EXAMPLES = '''
- name: "Roll some dice"
  dice_module:
    roll_d20: True
  register: roll_result
  # the above outputs the module register into a variable, then you can
  # print out that info via debug (below)
- debug:
    var: roll_result
'''

import random

from ansible.module_utils.basic import AnsibleModule

def main():

    argument_spec = dict(
        roll_d4=dict(required=False, default=False, type='bool'),
        roll_d6=dict(required=False, default=False, type='bool'),
        roll_d12=dict(required=False, default=False, type='bool'),
        roll_d20=dict(required=False, default=False, type='bool'),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    roll_d4 = module.params.get('roll_d4')
    roll_d6 = module.params.get('roll_d6')
    roll_d12 = module.params.get('roll_d12')
    roll_d20 = module.params.get('roll_d20')

    if roll_d4:
        try:
            json_output = {'roll_d4': (random.randint(1,4))}
        except ValueError:
            module.fail_json(msg="This module parameter takes a boolean!")

    elif roll_d6:
        try:
            json_output = {'roll_d6': (random.randint(1,6))}
        except ValueError:
            module.fail_json(msg="This module parameter takes a boolean!")

    elif roll_d12:
        try:
            json_output = {'roll_d12': (random.randint(1,12))}
        except ValueError:
            module.fail_json(msg="This module parameter takes a boolean!")

    elif roll_d20:
        try:
            json_output = {'roll_d20': (random.randint(1,20))}
        except ValueError:
            module.fail_json(msg="This module parameter takes a boolean!")

    module.exit_json(**json_output)


if __name__ == '__main__':
    main()
