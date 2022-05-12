def read_documents_content(self, projectnumber, parentpath, content):
    ''' Delete an attachment for a specified record.

    The calling function must first call create_sinstance(), then
    navigate_to_shell().
    
    After use, the calling function should call terminate_sinstance().
    '''
    if not self.driver:
        raise Exception('Call create_sinstance() to initialize the driver.')
    res = self.read_folder(
        projectnumber=projectnumber,
        parentpath=parentpath
    )
    try:
        projectid = res.json()['data'][0]['project_id']
        parent_id = res.json()['data'][0]['parent_node_id']
        url = f'{self.base_url}/bp/mod/dm/doc/search/fullSearch'
        data = {
            'matchoperator': 'AND',
            'parent_id': parent_id,
            'phase': 'all',
            'page': '1',
            'size': '2000',
            'rows': '10',
            'start': '0',
            'filetype': 'dms',
            'projectid': projectid,
            'searchfolderid': parent_id,
            'is_called_from': 'dmlog',
            'content': content,
            '__token': self.sutoken,
            '__uref': self.suuref
        }
        return self.driver.request(method='POST', url=url, data=data)
    except:
        return None
