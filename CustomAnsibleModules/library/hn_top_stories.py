#!/usr/bin/python
# coding: utf-8 -*-
#
# (c) 2022, Bianca Henderson <bianca@redhat.com>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}


DOCUMENTATION = '''
---
module: api_scraper
author: "Bianca Henderson (@bizonka)"
version_added: "2.9"
short_description: Scrape an API of choice
description:
    - A way to roll digital dice via Ansible playbook. Currently you can only
    roll one at a time.
options:
    number_of_entries:
      description:
        - Number of entries to look at.
      required: False
      type: int
      default: 1
'''

EXAMPLES = '''
- name: "Hacker News API Call"
  api_scraper:
    number_of_entries: 30
  register: top_stories
  # the above outputs the module register into a variable, then you can
  # print out that info via debug (below)
- debug:
    var: top_stories
'''

from ansible.module_utils.basic import AnsibleModule
from operator import itemgetter

import requests


def api_scrape_result(number_of_entries):
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    print(f"Status code: {r.status_code}")

    # Process information about each submission.
    submission_ids = r.json()[:number_of_entries]
    submission_dicts = []
    for submission_id in submission_ids:
        # Make a separate API call for each submission.
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()

        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'story_id': response_dict['id'],
            'score': response_dict['score'],
            'author': response_dict['by'],
            'comments': response_dict.get('descendants', 0),
        }
        submission_dicts.append(submission_dict)

    # Output is sorted by number of comments
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
    return submission_dicts
    # for submission_dict in submission_dicts:
    #     print(f"\nTitle: {submission_dict['title']}")
    #     print(f"Discussion link: {submission_dict['hn_link']}")
    #     print(f"Story ID: {submission_dict['story_id']}")
    #     print(f"Author: {submission_dict['author']}")
    #     print(f"Score: {submission_dict['score']}")
    #     print(f"Comments: {submission_dict['comments']}")

def main():
    argument_spec = dict(
        number_of_entries=dict(required=False, default=1, type='int'),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    number_of_entries = module.params.get('number_of_entries')

    try:
        json_output = {'custom_roll_result': api_scrape_result(number_of_entries)}
    except ValueError:
        module.fail_json(msg="Something went wrong!")

    module.exit_json(**json_output)

if __name__ == '__main__':
    main()
