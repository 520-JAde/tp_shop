from page.comment_page import CommentPage
import pytest
from common.base import open_mobile
import time
import allure


class TestShopping:
    @pytest.allure.severity (pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step (title='测试商品评论')
    def test_comment(self):
        """测试评论"""
        driver = open_mobile ()
        com = CommentPage (driver)  # 实例化评论的方法
        com.click_my ()  # 点击我的
        com.click_login_register ()  # 点击登录
        com.input_username ("18000180007")  # 输入账号密码
        com.input_password ("123456")  # 输入密码
        com.click_login ()  # 点击登录
        allure.attach ("点击我的", "进入个人中心")
        com.wait_comment ()  # 点击等待评价
        T = com.pre_comment_text ()  # 获取等待评价前的文本信息
        print (T)
        allure.attach ("评价前的商品文本信息", f"{T}")
        time.sleep (3)
        com.order_show ()  # 点击晒单评价
        allure.attach ("评价商品", "五星好评")
        com.comment ("你好")  # 输入文本内容
        com.play_start ()  # 为服务打分
        com.submit ()  # 点击提交
        time.sleep (5)  # 等待一段时间
        allure.attach ("跳转点击已评价", "切换到已评价页面")
        com.already_comment ()  # 点击已评价
        t = com.back_comment_text ()  # 获取已评价的所有评价
        for i in t:  # 将所有的评价循环出来
            assert T == i.get_attribute ("text")  # 判断之前取出来的值是否等于评价后的值
        allure.attach ("断言商品", "当评价前的商品出现在已评价里面断言成功")
        com.close_mobile ()
