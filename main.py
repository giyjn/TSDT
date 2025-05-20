from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@contextmanager
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    try:
        yield driver
    finally:
        driver.quit()

with chrome_driver() as browser:
    browser.get('http://localhost:8000')
    body = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body')))
    assert 'django' in body.text.lower()
    print("测试成功！")
    input("按回车键退出...")

