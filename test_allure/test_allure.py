import allure
import pytest


@allure.epic("这是EPIC")
@allure.feature("这是FEATURE")
@allure.story("这是STORY")
class TestAllure:
    @allure.description("用例1的描述")
    def test_normal_1(self):
        print("OK1")

    @allure.description("用例2的描述")
    def test_normal_2(self):
        print("OK2")

    def test_normal_3(self):
        print("OK3")


if __name__ == '__main__':
    pytest.main(['--alluredir=test_allure'])