from unifier.udr import (
    read_udr_formatted
)

def read_bpid(self, bpname):
    ''' Return the corresponding bpid from a passed bpname.

    '''
    bpid = None
    df = read_udr_formatted(
        self,
        reportname='BP List (Integration)'
    )
    for i in range(len(df)):
        if df.loc[i, 'BP_NAME'] == bpname:
            bpid = df.loc[i, 'BPID']
            break
    return bpid

def read_pid(self, shellnumber):
    ''' Return the corresponding pid from a passed shellnumber.

    '''
    pid = None
    df = read_udr_formatted(
        self,
        reportname='Shell Info (Integration)'
    )
    for i in range(len(df)):
        if df.loc[i, 'SHELLNUMBER'] == shellnumber:
            temp = ''
            for ch in df.loc[i, 'PID']:
                if ch.isdigit():
                    temp += ch
            pid = temp
            break
    return pid
