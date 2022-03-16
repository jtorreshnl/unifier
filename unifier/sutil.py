from selenium.webdriver.common.by import (
    By
)

from selenium.webdriver.support import (
    expected_conditions as EC
)

from selenium.webdriver.support.ui import (
    WebDriverWait
)

def get_element_by_css_selector(driver, tag, value):
    ''' Get a specified element by tag and attribute value.

    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, f'{tag}.{value}'))
    )
    if is_located:
        return driver.find_element(By.CSS_SELECTOR, f'{tag}.{value}')

def get_element_by_id(driver, id):
    ''' Get a specified element by id.

    Wait until the element is visible.
    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.ID, id))
    )
    if is_located:
        return driver.find_element(By.ID, id)

def get_element_by_id_clickable(driver, id):
    ''' Get elements by id.

    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.ID, id))
    )
    if is_located:
        return driver.find_element(By.ID, id)

def get_element_by_id_ext(driver, id):
    ''' Get a specified element by id.

    Wait until the element is visible.
    '''
    is_located = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, id))
    )
    if is_located:
        return driver.find_element(By.ID, id)

def get_element_by_tag(driver, tag):
    ''' Get a specified element by tag.

    Wait until the element is visible.
    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.TAG_NAME, tag))
    )
    if is_located:
        return driver.find_element(By.TAG_NAME, tag)

def get_element_by_tag_and_text(driver, tag, text):
    ''' Get a specified element by tag and text.

    Wait until the element is visible.
    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, tag), text)
    )
    if is_located:
        return driver.find_element(By.TAG_NAME, tag)

def get_element_by_xpath(driver, xpath):
    ''' Get element by xpath.

    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, f'{xpath}'))
    )
    if is_located:
        return driver.find_element(By.XPATH, f'{xpath}')

def get_element_by_xpath_clickable(driver, xpath):
    ''' Get element by xpath.

    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, f'{xpath}'))
    )
    if is_located:
        return driver.find_element(By.XPATH, f'{xpath}')

def get_element_by_xpath_visible(driver, xpath):
    ''' Get element by xpath.

    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.XPATH, f'{xpath}'))
    )
    if is_located:
        return driver.find_element(By.XPATH, f'{xpath}')

def get_elements_by_css_selector(driver, selector):
    ''' Get elements by css selector.

    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, f'{selector}'))
    )
    if is_located:
        return driver.find_elements(By.CSS_SELECTOR, f'{selector}')

def get_elements_by_tag(driver, tag):
    ''' Get all elements by tag.

    Wait until the elements are visible.
    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.TAG_NAME, tag))
    )
    if is_located:
        return driver.find_elements(By.TAG_NAME, tag)

def get_elements_by_tag_ext(driver, tag):
    ''' Get all elements by tag.

    Wait until the elements are visible.
    '''
    is_located = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, tag))
    )
    if is_located:
        return driver.find_elements(By.TAG_NAME, tag)

def get_elements_by_xpath(driver, xpath):
    ''' Get elements by xpath.

    '''
    is_located = WebDriverWait(driver, 4).until(
        EC.presence_of_all_elements_located((By.XPATH, f'{xpath}'))
    )
    if is_located:
        return driver.find_elements(By.XPATH, f'{xpath}')
