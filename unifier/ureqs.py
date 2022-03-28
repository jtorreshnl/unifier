class UnifierRequest:
    ''' Execute HTTP requests to Unifier.

    '''
    def __init__(self, env):
        ''' Create the request object.

        '''
        self.env = env
        self.token = None
        self.headers = None
        self.base_url = None
        self.ulogin = None
        self.portal_url = None
        self.username = None
        self.chromedriver = None
        self.driver = None
        self.suuref = None
        self.sutoken = None
        self.log_path = None
        self.engine = None
        self.con = None
        self.res = None
        self.data = None
        self.home = None
        self.uconfig = None
        self.config_path = None
        self.config_filename = None
        self.load_config()
        return

    from unifier.util import (
        load_config,
        set_token,
        set_headers,
        set_base_url,
        set_environment,
        set_ulogin,
        set_portal_url,
        set_username,
        set_chromedriver,
        set_log_path,
        set_engine,
        set_connection,
        write_log
    )

    from unifier.bp import (
        read_records,
        read_record,
        read_record_attachments,
        create_record,
        update_record,
        update_record_attachment
    )

    from unifier.dm import (
        read_folders,
        read_documents,
        create_folder,
        create_abspath,
        create_document,
        update_folder
    )

    from unifier.ds import (
        read_data_element,
        read_data_definition,
        update_data_definition_data_set
    )

    from unifier.udr import (
        read_udr,
        read_udr_formatted
    )

    from unifier.user import (
        read_users,
        read_user_shell_groups,
        update_user_shell_groups,
        update_user_groups
    )

    from unifier.uutil import (
        read_bpid,
        read_pid
    )

    from unifier.sureqs import (
        create_sinstance,
        get_suuref,
        get_sutoken,
        set_suuref,
        set_sutoken,
        navigate_to_shell,
        terminate_sinstance
    )

    from unifier.sbp import (
        delete_record_attachment
    )

    from unifier.sudr import (
        read_udrs_metadata,
        delete_udr
    )
