from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 张三听说有一个在线待办事项的应用
        # 他查看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 他注意到页面标题和头部都包含了“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text  # #(1)
        self.assertIn('To-Do', header_text)

        # 应用有一个输入待办事项的文本框
        inputbox = self.browser.find_element(By.ID, 'id_new_item')  #(1)
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 他在文本框中输入了“Buy flowers”
        inputbox.send_keys('Buy flowers')  #(2)

        # 他按下回车键，页面更新了
        # 事情变成了待办列表的一部分：“Buy flowers”
        inputbox.send_keys(Keys.ENTER)  #(3)
        time.sleep(1)  #(4)

        # 页面更新后，列表中出现了“Buy flowers”
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')  #(1)
        self.assertIn('1: Buy flowers', [row.text for row in rows])

        # 页面下方还有一个文本框，用户可以输入待办事项
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('gift to girlfriend')  #(5)

        # 页面再次更新，她的清单中显示了这两个待办事项
        self.fail('Finish the test!')
