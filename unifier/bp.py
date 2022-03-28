import base64
import json
import os
import requests
import zipfile

def read_records(self, project_number, bpname):
    ''' Read all records in a specified shell.

    '''
    url = f'{self.base_url}/ws/rest/service/v1/bp/records/{project_number}'
    input_ = {
        'bpname': bpname,
        'lineitem': 'yes'
    }
    return requests.post(url=url, json=input_, headers=self.headers)

def read_record(self, project_number, bpname, record_no):
    ''' Read a record in a specified shell.

    '''
    url = f'{self.base_url}/ws/rest/service/v1/bp/record/{project_number}'
    input_ = {
        'bpname': bpname,
        'record_no': record_no,
        'lineitem': 'yes'
    }
    params = {
        'input': json.dumps(input_)
    }
    return requests.get(url=url, params=params, headers=self.headers)

def read_record_attachments(self, project_number, bpname, record_no):
    ''' Read a record in a specified shell, and download all attachments.

    The attachments are stored as a base64 string.

    To get the base64 string:
    string = res.json()['data'][0]['file_handler']

    To get the decoded bytes:
    bytes = base64.b64decode(string)

    To write the results to a zip:
    with open('output.zip', 'wb') as file:
        file.write(bytes)
    '''
    url = f'{self.base_url}/ws/rest/service/v1/bp/record/file/{project_number}'
    input_ = {
        'bpname': bpname,
        'record_no': record_no,
        'lineitem': 'yes',
        'lineitem_file': 'yes',
        'general_comments': 'yes',
        'attach_all_publications': 'yes'
    }
    params = {
        'input': json.dumps(input_)
    }
    return requests.get(url=url, params=params, headers=self.headers)

def create_record(self, project_number, bpname, data, record_no=None, workflow_name=None, action_name=None, username=None):
    ''' Create a record in a specified shell.

    A workflow and action can be passed, and the record will be created
    accordingly.
    '''
    url = f'{self.base_url}/ws/rest/service/v1/bp/record/{project_number}'
    input_ = {
        'options': {
            'bpname': bpname,
            'workflow_details': {
                'workflow_name': workflow_name,
                'action_name': action_name,
                'user_name': username
            }
        },
        'data': [{}]
    }
    if not username: input_['options']['workflow_details']['user_name'] = self.username
    if record_no: input_['data'][0]['record_no'] = record_no
    for key, value in data.items():
        input_['data'][0][key] = value
    return requests.post(url=url, json=input_, headers=self.headers)

def update_record(self, project_number, bpname, record_no, data=None, WFCurrentStepName=None, WFActionName=None, LineItemIdentifier=None):
    ''' Update a record in a specified shell.

    A workflow step and action can be passed, and the record will be updated
    accordingly.
    '''
    url = f'{self.base_url}/ws/rest/service/v1/bp/record/{project_number}'
    input_ = {
        'options': {
            'bpname': bpname,
            'workflow_details': {
                'WFCurrentStepName': WFCurrentStepName,
                'WFActionName': WFActionName
            }
        },
        'data': [{
            'record_no': record_no
        }]
    }
    if LineItemIdentifier: input_['options']['LineItemIdentifier'] = LineItemIdentifier
    if data:
        for key, value in data.items():
            input_['data'][0][key] = value
    return requests.put(url=url, json=input_, headers=self.headers)

def update_record_attachment(self, project_number, bpname, record_no, file_name, title=None, issue_date=None, revision_no=None, data=None, WFCurrentStepName=None, WFActionName=None, LineItemIdentifier=None):
    ''' Update a record in a specified shell and include an attachment.

    The project_number, bpname, record_no, and file_name are required.

    A workflow step and action can be passed, and the record will be updated
    accordingly.
    '''
    url = f'{self.base_url}/ws/rest/service/v1/bp/record/file/{project_number}'
    is_removed = False
    cwd = os.getcwd()
    os.chdir(os.path.dirname(file_name))
    base = os.path.basename(file_name)
    zipped_file_name = f'{os.path.splitext(base)[0]}.zip'
    with zipfile.ZipFile(zipped_file_name, 'w') as file:
        file.write(base)
    with open(zipped_file_name, 'rb') as file:
        bytes = file.read()
        encoded = base64.b64encode(bytes)
    input_ = {
        'options': {
            'bpname': bpname,
            'workflow_details': {
                'WFCurrentStepName': WFCurrentStepName,
                'WFActionName': WFActionName
            }
        },
        'data': [{
            'record_no': record_no,
            '_attachment': [{
                'file_name': os.path.basename(file_name),
                'title': title,
                'issue_date': issue_date,
                'revision_no': revision_no
            }]
        }],
        '_attachment': {
            'zipped_file_name': zipped_file_name,
            'zipped_file_size': str(os.path.getsize(zipped_file_name)),
            'zipped_file_content': str(encoded)[2:-1]
        }
    }
    if LineItemIdentifier: input_['options']['LineItemIdentifier'] = LineItemIdentifier
    if data:
        for key, value in data.items():
            input_['data'][0][key] = value
    while not is_removed:
        try:
            os.remove(zipped_file_name)
            is_removed = True
        except:
            is_removed = False
    os.chdir(cwd)
    return requests.put(url=url, json=input_, headers=self.headers)
