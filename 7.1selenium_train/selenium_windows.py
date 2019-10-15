import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
time.sleep(3)

browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(3)

browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')
time.sleep(3)

browser.close()