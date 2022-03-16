import json
import os
import requests

def read_folders(self, projectnumber, parentpath, nodetype=None):
    ''' Read the folders or files in a specified directory.

    The parentpath is the name of the folder, e.g. '/05 Drawings'.

    The nodetype value is either 'Document' or 'Folder'.
    '''
    url = f'{self.base_url}/ws/rest/service/v1/dm/node/properties'
    params = {
        'projectnumber': projectnumber,
        'parentpath': parentpath,
        'nodetype': nodetype
    }
    return requests.get(url=url, params=params, headers=self.headers)

def read_documents(self, parentpath, projectnumber=None, iszip='yes'):
    ''' Read all documents in a specified directory.

    The parentpath is the name of the folder, e.g. '/05 Drawings'.

    The documents are returned as zip file bytes. To build the zip file, execute
    the following code:

    with open('output.zip', 'wb') as file:
        file.write(res.content)

    with zipfile.ZipFile('output.zip', 'r') as file:
        file.extractall('.')
    '''
    url = f'{self.base_url}/ws/rest/service/v1/dm/document'
    params = {
        'parentpath': parentpath,
        'iszip': iszip
    }
    if projectnumber: params['projectnumber'] = projectnumber
    return requests.get(url=url, params=params, headers=self.headers)

def create_folder(self, projectnumber, Path, Name, Owner):
    ''' Create a folder at the specified path.

    The owner of the folder is inherited, such that it is set equal to the
    name of the shell administrator.
    '''
    url = f'{self.base_url}/ws/rest/service/v1/dm/folder/create'
    data = [{
        'Path': Path,
        'Name': Name,
        'Owner': Owner
    }]
    input_ = {
        'projectnumber': projectnumber,
        'data': json.dumps(data)
    }
    return requests.post(url=url, data=input_, headers=self.headers)

def create_abspath(self, abspath, projectnumber=None, sep='/'):
    ''' Create the folder structure in the abspath if it does not exist.

    The abspath must adhere to the following format:
    /foo/bar/baz

    The abspath must not end with a separator.

    If a folder in abspath does not exist, it will be created.
    '''
    values = abspath.split(sep=sep)[1:]
    for i in range(len(values)):
        path = ''
        for j in range(i + 1):
            curr = values[j]
            path += f'/{curr}'
        res = self.read_folders(
            projectnumber=projectnumber,
            parentpath=path,
            nodetype='Folder'
        )
        if res.json()['status'] != 200:
            Path = '/' + '/'.join(values[:i])
            Name = values[i]
            print(f'Creating folder {path}')
            self.create_folder(
                projectnumber=projectnumber,
                Path=Path,
                Name=Name,
                Owner=self.username
            )

def create_document(self, projectnumber, Path, Name, dorevise='no'):
    ''' Create a document at the specified path.

    The Name parameter is the respective file to be uploaded. The value can be
    a relative or absolute path.
    '''
    url = f'{self.base_url}/ws/rest/service/v1/dm/document/create'
    files = {
        'file': open(Name, 'rb')
    }
    data = [{
        'Path': Path,
        'Name': os.path.basename(Name)
    }]
    input_ = {
        'projectnumber': projectnumber,
        'dorevise': dorevise,
        'data': json.dumps(data)
    }
    return requests.post(url=url, data=input_, headers=self.headers, files=files)

def update_folder(self, projectnumber, Path, data):
    ''' Update the folder at the specified path.

    The owner cannot be updated.

    The owner of the folder is inherited, such that it is set equal to the
    name of the shell administrator.
    '''
    url = f'{self.base_url}/ws/rest/service/v1/dm/folder/update'
    data_ = [{
        'Path': Path
    }]
    if data:
        for key, value in data.items():
            data_[0][key] = value
    input_ = {
        'projectnumber': projectnumber,
        'data': json.dumps(data_)
    }
    return requests.post(url=url, data=input_, headers=self.headers)
