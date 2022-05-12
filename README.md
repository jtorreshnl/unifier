# Unifier

## About

The Unifier library provides a lightweight interface to Primavera Unifier. The UnifierRequest class contains methods to perform HTTP requests. The full list of methods can be found in the methods table below. After creating the UnifierRequest object, it can be used to make subsequent requests for a given environment. Docstrings should be sufficient for use, but the functions can be referenced in their respective files, grouped together by type, e.g. bp.py = Business Process and dm = Document Manager.

## Sample Usage

    from unifier import UnifierRequest as ur

    req = ur(
        env='prod'
    )

    res = req.read_records(
        project_number='PROJ001',
        bpname='Drawings'
    )

    print(res.json())

## Configuration

Upon instantiation, a config file is read, and settings are updated accordingly.

The user must set a system variable, named HOME, such that HOME is equal to the directory where the config file is stored at.

The config file must be named uconfig.json.

A template of the config file is available in the repo.

## uconfig.json

The config file will be referenced for tokens, urls, environment variables, login information, database information, and more.

Please use the uconfig.json file in this repo as a template, and refer to the table below for usage.

It is important to note that only two key value pairs are required in the config file: tokens and base_urls. These key value pairs identify the Unifier environment, token, and url to be used during the session. It is important to ensure that tokens and base_urls each have at least one entry, and the env keys match. The session env is required during instantiation, and it must match an env in the config file. Again, please refer to the uconfig.json template for an example.

|Key|Value|Notes|Required|
|---|-----|-----|--------|
|tokens|A list of env value pairs, where env is the Unifier environment and value is the corresponding token|It is common to have more than one environment in Unifier. A company could have a production environment, as well as a testing environment.|x|
|base_urls|A list of env value pairs, where env is the Unifier environment and value is the url|The Unifier environment must correspond with its base url. REST endpoints are concatenated with the base urls to form the full url to where requests are sent. Refer to uconfig.json for an example.|x|
|environment|A list of name value pairs, where name is the system environment variable name and value is its value.|The main purpose of these variables is for setting up proxies. HTTP proxies can be added to bypass network settings, if applicable. Refer to uconfig.json for an example.|
|login|A valid Unifier username and password|This is only necessary if needing to access functions that use web automation, such as deleting attachments.|
|portal_url|The portal used to log into Unifier|This is only necessary if needing to access functions that use web automation, such as deleting attachments.|
|username|The username to be selected when creating records|In some cases, the creator or owner is selected automatically in Unifier.|
|chromedriver|The path of the chromedriver.exe file|This is only necessary if needing to access functions that use web automation, such as deleting attachments.|
|log|The path where log files should be written to|Log files are not generated automatically. A log file is only generated by calling the write_log() method.|
|engine|The sqlalchemy engine string to be used|
|connection|The pyodbc connection string to be used|

## Methods

|Type|Function Name|Notes|
|----|-------------|-----|
|Business Process|read_records|
|Business Process|read_record|
|Business Process|read_record_attachments|Attachments are returned as a base64 zip file string.
|Business Process|update_record|
|Business Process|update_record_attachment|
|Business Process|delete_record_attachment|This method uses seleniumrequests and needs the Unifier file id.|
|Document Manager|read_folder|
|Document Manager|read_documents|Documents and folder structure are returned as zip file bytes.
|Document Manager|create_folder|
|Document Manager|create_abspath|If folders do not exist in the abspath, they will be created.|
|Document Manager|create_document|
|Document Manager|update_folder|
|Data Structure|read_data_element|
|Data Structure|read_data_definition|
|Data Structure|update_data_definition_data_set|
|User-Defined Report|read_udr|
|User-Defined Report|read_udr_formatted|The udr is returned in a pandas DataFrame.|
|User-Defined Report|read_udrs_metadata|This method uses selenium requests to read metadata of all udrs in the current shell.|
|User-Defined Report|delete_udr|This method must be called from within the shell.|
|User|read_users|
|User|read_user_shell_groups|
|User|update_user_shell_groups|
|User|update_user_groups|
|Utility|read_bpid|
|Utility|read_pid|
