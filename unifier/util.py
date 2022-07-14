from datetime import (
    datetime as dt
)

import json
import os
import pandas as pd
import pyodbc
import sqlalchemy

def load_config(self):
    ''' Load the configuration settings.

    '''
    self.config_filename = 'uconfig.json'
    try:
        self.home = os.environ['HOME']
        self.config_path = os.path.join(self.home, self.config_filename)
    except:
        raise OSError('Error: HOME environment variable is not set')
    if not os.path.isfile(self.config_path):
        raise FileNotFoundError(f'Error: unable to locate config file at '\
        + self.config_path)
    try:
        with open(self.config_path, 'r') as file:
            self.uconfig = json.load(file)
    except:
        raise ValueError('Error: expected JSON format')
    self.set_token()
    self.set_headers()
    self.set_base_url()
    self.set_environment()
    self.set_ulogin()
    self.set_portal_url()
    self.set_username()
    self.set_chromedriver()
    self.set_chrome_binary_location()
    self.set_log_path()
    self.set_engine()
    self.set_connection()

def set_token(self):
    ''' Set the token for api calls.

    '''
    prefix = 'Bearer '
    try:
        for token in self.uconfig['tokens']:
            if token['env'] == self.env:
                self.token = prefix + token['value']
                break
    except:
        pass
    return

def set_headers(self):
    ''' Set the headers to be used in requests.

    '''
    self.headers = {
        'Authorization': self.token
    }
    return

def set_base_url(self):
    ''' Set the base url.

    '''
    try:
        for url in self.uconfig['base_urls']:
            if url['env'] == self.env:
                self.base_url = url['value']
                break
    except:
        pass
    return

def set_environment(self):
    ''' Set the system environment variables.

    '''
    try:
        for variable in self.uconfig['environment']:
            os.environ[variable['name']] = variable['value']
    except:
        pass
    return

def set_ulogin(self):
    ''' Set the Unifier login credentials.

    '''
    try:
        self.ulogin = {
            'username': self.uconfig['login']['username'],
            'password': self.uconfig['login']['password']
        }
    except:
        pass
    return

def set_portal_url(self):
    ''' Set the Unifier portal url.

    '''
    try:
        self.portal_url = self.uconfig['portal_url']
    except:
        pass
    return

def set_username(self):
    ''' Set the Unifier default username for requests.

    '''
    try:
        self.username = self.uconfig['username']
    except:
        pass
    return

def set_chromedriver(self):
    ''' Set the location of the chromedriver.

    '''
    try:
        self.chromedriver = self.uconfig['chromedriver']
    except:
        pass
    return

def set_chromedriver(self):
    ''' Set the location of the chromedriver.

    '''
    try:
        self.chrome_binary_location = self.uconfig['chrome_binary_location']
    except:
        pass
    return

def set_log_path(self):
    ''' Set the default write path of the log.

    '''
    try:
        self.log_path = self.uconfig['log']
    except:
        pass
    return

def set_engine(self):
    ''' Set the sqlalchemy engine.

    '''
    try:
        self.engine = sqlalchemy.create_engine(self.uconfig['engine'])
    except:
        pass
    return

def set_connection(self):
    ''' Set the pyodbc connection.

    '''
    try:
        self.con = pyodbc.connect(self.uconfig['connection'])
    except:
        pass
    return

def write_log(self, results):
    ''' Write the results of a request to a log.

    The results should be a list of dictionaries.
    '''
    now = dt.now().strftime('%Y%m%d_%H%M%S')
    filename = f'ureqs_{now}.csv'
    abspath = f'{self.log_path}/{filename}'
    output = pd.DataFrame(results)
    output.to_csv(f'{abspath}', sep=',', index=False)
    print(f'Results written to \'{abspath}\'')
    return
