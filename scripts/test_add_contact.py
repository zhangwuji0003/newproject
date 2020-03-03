import time

import allure
import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestAddContact:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # zhangsan, 188
    # lisi, 177
    # wangwu, 166
    @pytest.mark.parametrize("args", analyze_data("add_contact_data", "test_add_contact"))
    def test_add_contact(self, args):
        name = args["name"]
        phone = args["phone"]

        # 联系人列表 - 点击添加联系人
        self.page.contact_list.click_add_contact()
        # 添加联系人 - 点击本地保存
        self.page.add_contact.click_local()
        # 添加联系人 - 输入姓名
        self.page.add_contact.input_name(name)
        # 添加联系人 - 输入电话
        self.page.add_contact.input_phone(phone)
        # 添加联系人 - 点击返回
        self.page.add_contact.click_back()

        # 截图
        self.driver.get_screenshot_as_file("xx.png")

        try:
            # 保存页面 - 断言 大标题的内容 是否与输入的用户名一致
            assert self.page.contact_saved.get_large_title_text() == name + "123"
        except Exception as e:
            # 将图片添加到报告中
            allure.attach.file("xx.png", attachment_type=allure.attachment_type.PNG)

        assert self.page.contact_saved.get_large_title_text() == name + "123456"

    

