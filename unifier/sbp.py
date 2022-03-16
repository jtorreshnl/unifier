def delete_record_attachment(self, projectId, sourcetype, sourceid, file_id):
    ''' Delete an attachment for a specified record.

    The calling function must first call create_sinstance(). After use, the
    calling function should call terminate_sinstance().
    
    The bp must have the respective attachment deletion setting enabled.

    The projectId is the numerical representation of the project number.

    The sourcetype is the bp name identifier.

    The sourceid is the parent id to which the attachment belongs to.

    The file_id is the unique id associated with the attachment.
    '''
    if not self.driver:
        raise Exception('Call create_sinstance() to initialize the driver.')
    url = f'{self.base_url}/bp/studio/share/delete_files'
    data = {
        'delete_files_ids': file_id,
        'parent_rank1': file_id,
        'sourcetype': sourcetype,
        'sourceid': sourceid,
        'isDocReview': 'true',
        'id_1': sourceid,
        'type_1': sourcetype,
        'projectId': projectId,
        '__token': self.sutoken,
        '__uref': self.suuref
    }
    return self.driver.request(method='POST', url=url, data=data)
