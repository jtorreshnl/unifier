def read_udrs_metadata(self):
    ''' Read udrs in the current shell.

    The list of udrs, along with pertinent metadata, such as report ids, is
    returned in the response.

    This function must be used after calling create_sinstance() and
    navigate_to_shell().

    The value of suuref is updated upon calling navigate_to_shell(). The updated
    value will be sent in the request, and it is critical for getting the
    correct data. See navigate_to_shell() for more information.
    '''
    if not self.driver:
        raise Exception('Call create_sinstance() to initialize the driver.')
    url = f'{self.base_url}/bp/mod/report/log/query'
    params = {
        'ReportType': 'project',
        'hidden_view_type': 'filter'
    }
    input_ = {
        'page': '1',
        'size': '1000',
        '__token': self.sutoken,
        '__uref': self.suuref
    }
    return self.driver.request(method='POST', url=url, params=params, data=input_)

def delete_udr(self, report_id):
    ''' Delete an udr with the specified report id.

    The udr must be deleted while in the shell, so navigate_to_shell() must be
    called first.
    '''
    if not self.driver:
        raise Exception('Call create_sinstance() to initialize the driver.')
    url = f'{self.base_url}/bp/sys/report/delete'
    input_ = {
        'selected_ids': str(report_id),
        'fromNewUI': '1',
        '__token': self.sutoken,
        '__uref': self.suuref
    }
    return self.driver.request(method='POST', url=url, data=input_)
