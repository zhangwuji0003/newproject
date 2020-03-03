# 联系人保存页面
import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactSavedPage(BaseAction):

    # 保存页面 - 大标题
    large_title_label = By.ID, "com.android.contacts:id/large_title"

    @allure.step(title="联系人保存 - 获取大标题的文字")
    def get_large_title_text(self):
        return self.get_text(self.large_title_label)


