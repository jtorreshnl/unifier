import pandas as pd
import requests

def read_udr(self, reportname, project_number=None, query=None):
    ''' Run a specified udr and read the data.

    If a query is provided, the format must be a list of dictionaries, e.g.
    [{'label': '_shell_groups / USERNAME', 'value1': 'jtorres'}].
    '''
    url = f'{self.base_url}/ws/rest/service/v1/data/udr/get/'
    if project_number: url += project_number
    input_ = {
        'reportname': reportname,
        'query': query
    }
    return requests.post(url=url, json=input_, headers=self.headers)

def read_udr_formatted(self, reportname, project_number=None, query=None):
    ''' Return a df of the udr with proper column headers.

    '''
    self.res = self.read_udr(reportname, project_number, query)
    headers = self.res.json()['data'][0]['report_header']
    for key in headers.keys():
        headers[key] = headers[key]['name']
    rows = self.res.json()['data'][0]['report_row']
    df = pd.DataFrame(rows)
    df.rename(mapper=headers, axis=1, inplace=True)
    return df
