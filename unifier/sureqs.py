import re

from selenium import (
    webdriver
)

from seleniumrequests import (
    Chrome
)

from unifier.sutil import (
    get_element_by_id,
    get_element_by_id_clickable,
    get_element_by_id_ext,
    get_element_by_xpath_clickable,
    get_elements_by_tag_ext,
    get_elements_by_xpath
)

def create_sinstance(self):
    ''' Create a Selenium instance of Unifier.

    sinstance refers to Selenium instance, where web automation is used to log
    into Unifier. This login is necessary because the uref and token, suuref
    and sutoken respectively, are required for some requests, and obtained
    during an online session.

    After use, call terminate_sinstance().
    '''
    if self.chrome_binary_location:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = self.chrome_binary_location
        self.driver = Chrome(self.chromedriver, chrome_options=chrome_options)
    else:
        self.driver = Chrome(self.chromedriver)
    self.driver.get(self.portal_url)
    el = get_element_by_id_ext(self.driver, 'idcs-signin-basic-signin-form-username')
    el.send_keys(self.ulogin['username'])
    el = get_element_by_id_ext(self.driver, 'idcs-signin-basic-signin-form-password')
    el.send_keys(self.ulogin['password'])
    el = get_element_by_id_ext(self.driver, 'ui-id-4')
    el.click()
    el = get_element_by_id_ext(self.driver, 'agreeCookies')
    el.click()
    if self.env == 'stage': target = 'Stage'
    else: target = 'Production'
    wait = get_element_by_id_ext(self.driver, 'env-label')
    arr = get_elements_by_tag_ext(self.driver, 'span')
    for el in arr:
        if target in el.text:
            el.click()
            break
    arr = get_elements_by_tag_ext(self.driver, 'img')
    for el in arr:
        target = 'Primavera Unifier'
        if target in el.get_attribute('alt'):
            el.click()
    self.driver.switch_to.window(self.driver.window_handles[1])
    wait = get_element_by_id_ext(self.driver, 'openTabsBtn', timeout=20)
    self.set_suuref()
    self.set_sutoken()


def get_suuref(self):
    ''' Get the value of suuref.

    '''
    return self.suuref

def get_sutoken(self):
    ''' Get the value of sutoken.

    '''
    return self.sutoken

def set_suuref(self):
    ''' Set the value of suuref.

    Reference the page source, pattern matching for the uref key.
    '''
    pattern = '("uref")(:)(")(.*)(")'
    page_source = self.driver.page_source
    match = re.search(pattern, page_source)
    self.suuref = match.group(4)

def set_sutoken(self):
    ''' Set the value of sutoken.

    Reference the page source, pattern matching for the token key.
    '''
    pattern = '("token")(:)(")(.*)(")'
    page_source = self.driver.page_source
    match = re.search(pattern, page_source)
    self.sutoken = match.group(4)

def navigate_to_shell(self, project_number):
    ''' Navigate to the specified shell, referencing the shell number.

    Upon navigating to the shell, the value of suuref is updated to match the
    corresponding thread number. This updated value of suuref can now be used
    for requests that require it.

    If the navigation is successful, the function returns True. Otherwise, it
    returns False, and the navigation window is closed.
    '''
    if not self.driver:
        raise Exception('Call create_sinstance() to initialize the driver.')

    page_source = self.driver.page_source
    pattern = '(tab-)(\d+)'
    tabs = re.findall(pattern, page_source)
    max = 0
    for tab in tabs:
        curr = int(tab[1])
        if curr > max:
            max = curr
    target = f'iframe-{max + 1}-body-0'
    el = get_element_by_id_clickable(self.driver, 'openTabsBtn')
    el.click()
    el = get_element_by_xpath_clickable(self.driver, '//oj-button[@title="Open All Locations"]')
    el.click()
    el = get_element_by_xpath_clickable(self.driver, '//oj-button[@title="Find on Page"]')
    el.click()
    el = get_element_by_xpath_clickable(self.driver, '//th[@data-index="shell_number"]/input[@placeholder="\xa0Find\xa0"]')
    el.click()
    el.send_keys(project_number)
    try:
        arr = get_elements_by_xpath(self.driver, '//td/div/div/mark')
        for el in arr:
            if el.text == project_number:
                el.click()
    except:
        el = get_element_by_xpath_clickable(self.driver, '//oj-button[@title="Close"]')
        el.click()
        return False
    el = get_element_by_xpath_clickable(self.driver, '//oj-button[@data-oj-subid="selectButton"]')
    el.click()
    wait = get_element_by_id(self.driver, target)
    self.suuref = re.sub('t\d+', '', self.suuref)
    pattern = self.suuref + 't\d+'
    page_source = self.driver.page_source
    matches = re.findall(pattern, page_source)
    self.suuref = matches[-1]
    return True

def terminate_sinstance(self):
    ''' Terminate the Selenium instance.

    Iterate through the list of active windows in a reverse order, closing each
    window. Then, call driver.quit() and reset object attributes.
    '''
    for i in range(len(self.driver.window_handles) -1, -1, -1):
        self.driver.switch_to.window(self.driver.window_handles[i])
        self.driver.close()
    self.quit()
    self.driver = None
    self.suuref = None
    self.sutoken = None
