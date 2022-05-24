import json
import requests

def read_data_element(self, data_element=None):
    ''' Read a data element.

    If a data element name is not provided, all data elements will be
    returned.
    '''
    url = f'{self.base_url}/ws/rest/service/v1/ds/data-elements'
    filter_ = {}
    if data_element: filter_['data_element'] = data_element
    params = {
        'filter': json.dumps(filter_)
    }
    return requests.get(url=url, params=params, headers=self.headers)

def read_data_definition(self, type='Basic', name=None):
    ''' Read a data definition.

    '''
    url = f'{self.base_url}/ws/rest/service/v1/ds/data-def'
    filter_ = {}
    if name: filter_['name'] = name
    params = {
        'type': type,
        'filter': json.dumps(filter_)
    }
    return requests.get(url=url, params=params, headers=self.headers)

def create_data_element(self, data_element, data_definition, form_label):
    ''' Create a data element.

    '''
    url = f'{self.base_url}/ws/rest/service/v1/ds/data-elements'
    input_ = {
        'data': [{
            'data_element': data_element,
            'data_definition': data_definition,
            'form_label': form_label
        }]
    }
    return requests.post(url=url, json=input_, headers=self.headers)

def update_data_definition_data_set(self, name, data_set):
    ''' Update a data definition.

    The data set must be a list of dictionaries containing the following
    keys: value, row_num, status, label, is_default.

    E.g, data_set = [{'value': 'value', 'row_num': 1, 'status':
    'Active', 'label': 'label', 'is_default': 'No'}, {}]
    '''
    url = f'{self.base_url}/ws/rest/service/v1/ds/data-def'
    input_ = {
        'options': {
            'type': 'Basic'
        },
        'data': [{
            'name': name,
            'dataset_non_modifiable': 'No',
            'data_set': data_set
        }]
    }
    return requests.put(url=url, json=input_, headers=self.headers)
