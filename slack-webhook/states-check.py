# This will send json data from a file 
# to a slack channel via slacks incoming webook 
import os
from os import system
import requests
from pathlib import Path
import json

BUILD_FILE = 'info.json'
PATH_TO_FILE = Path('./info.json')
WEBHOOK = 'https://hooks.example.com/XYz123'

def check_file_exists():

    FILE_CHECK = Path(BUILD_FILE)
    if FILE_CHECK.is_file():
        print(f'Found {BUILD_FILE} file')
        print(f'Print {BUILD_FILE} file content')

        with open(BUILD_FILE) as f:
            STATE_DATA = json.load(f)
            print(STATE_DATA)

        # set text field and add new python variable as string
        full_data = {'text': 'States Info Provided' + str(STATE_DATA) + ' .'}

        # send slack message via webhook
        SLACK_SEND = requests.post(url=WEBHOOK, json=full_data)
        print(SLACK_SEND.content)
    else:
        print(f'Could not find {BUILD_FILE} file. does not exist')
        print(f'BUILD STAGE COMPLETED')


def main():
    check_file_exists()

if __name__ == '__main__':
    main()
