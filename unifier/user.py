import requests

def read_users(self, uuu_user_status=1, uuu_user_name=None, uuu_user_email=None):
    ''' Read users.

    The results will be filtered by active users by default.

    If the results are filtered by user name or email, the response will be
    a list with a single record.
    '''
    url = f'{self.base_url}/ws/rest/service/v1/admin/user/get'
    input_ = {
        'filterCondition': f'uuu_user_status={uuu_user_status}'
    }
    res = requests.post(url=url, json=input_, headers=self.headers)
    if uuu_user_name:
        return list(filter(lambda user: user['uuu_user_name'] == uuu_user_name, res.json()['data']))
    if uuu_user_email:
        return list(filter(lambda user: user['uuu_user_email'] == uuu_user_email, res.json()['data']))
    return res

def read_user_shell_groups(self, username, project_number):
    ''' Read the groups a user belongs to in a shell.

    '''
    groups = []
    query = []
    query.append({
        'label': '_shell_groups / USERNAME',
        'value1': username
    })
    query.append({
        'label': '_shell_groups / PROJECT_NUMBER',
        'value1': project_number
    })
    res = self.read_udr(
        reportname='Shell Groups Report (Integration)',
        query=query
    )
    data = res.json()['data'][0]
    for key, value in data['report_header'].items():
        for header in value.keys():
            if value[header] == 'groupname':
                target = key
    for record in data['report_row']:
        groups.append(record[target])
    return groups

def update_user_shell_groups(self, username, shellnumber, group_add=None, group_remove=None, status='Active'):
    ''' Update the groups a user belongs to in a shell.

    '''
    url = f'{self.base_url}/ws/rest/service/v1/admin/user/shell/membership'
    input_ = {
        'shellnumber': shellnumber,
        'users': [{
            'username': username,
            'status': status,
        }]
    }
    if group_add: input_['users'][0]['group_add'] = group_add
    if group_remove: input_['users'][0]['group_remove'] = group_remove
    return requests.put(url=url, json=input_, headers=self.headers)

def update_user_groups(self, username, group_add=None, group_remove=None):
    ''' Update the groups a user belongs too.

    '''
    url = f'{self.base_url}/ws/rest/service/v1/admin/user/group/membership'
    input_ = [{
        'username': username
    }]
    if group_add: input_[0]['group_add'] = group_add
    if group_remove: input_[0]['group_remove'] = group_remove
    return requests.put(url=url, json=input_, headers=self.headers)
