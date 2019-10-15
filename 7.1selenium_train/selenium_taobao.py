from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=chrome_options)

try:
    browser.get('https://www.taobao.com')
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    input.send_keys('iPhone')
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    button.click()

    try:
        input = browser.find_element_by_id('tb-beacon-aplus')
    except NoSuchElementException:
        print('No Element')
finally:
    browser.close()