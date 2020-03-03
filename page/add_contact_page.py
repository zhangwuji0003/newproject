# 添加联系人页面
import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddContactPage(BaseAction):
    # 本地保存
    local_button = By.XPATH, "//*[@text='本地保存']"

    # 姓名输入框
    name_edit_text = By.XPATH, "//*[@text='姓名']"

    # 电话输入框
    phone_edit_text = By.XPATH, "//*[@text='电话']"

    # 返回按钮
    back_button = By.XPATH, "//*[@content-desc='向上导航']"

    @allure.step(title="添加联系人 - 点击本地保存")
    def click_local(self):
        self.click(self.local_button)

    @allure.step(title="添加联系人 - 输入用户名")
    def input_name(self, text):
        allure.attach("这是一个输入用户名的方法，用户名为："+text)
        self.input(self.name_edit_text, text)

    @allure.step(title="添加联系人 - 输入电话")
    def input_phone(self, text):
        allure.attach("这是一个输入电话的方法，电话为：" + text)
        self.input(self.phone_edit_text, text)

    @allure.step(title="添加联系人 - 点击返回")
    def click_back(self):
        self.click(self.back_button)
