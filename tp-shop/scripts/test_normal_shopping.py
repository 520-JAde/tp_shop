from page.goods_page import GoodsPage
import pytest
from common.base import open_mobile
import allure
import time

class TestShopping:

    @pytest.allure.severity (pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step (title='非活动商品使用余额购物')
    def test_normal_good(self):
        """测试正常商品的购买"""
        driver = open_mobile ()
        normal = GoodsPage (driver)  # 实化类
        normal.click_my ()  # 点击我的
        normal.click_login_register ()  # 点击登录
        normal.input_username ("18000180007")  # 输入账号密码
        normal.input_password ("123456")
        normal.click_login ()  # 点击登录
        allure.attach ("登录成功", "进入个人中心")
        time.sleep(3)
        pre_balance = normal.show_my_balance ()  # 结算前的余额
        print(pre_balance)
        allure.attach ("获取前购物前余额", f"获取购买商品前的余额:{pre_balance}")
        normal.back_home ()  # 返回首页
        allure.attach ("选择商品", "选择正常商品")
        normal.up_slither ()  # 上滑选择商品
        normal.rice ()  # 选择商品
        normal.immediately_buy ()  # 点击立即购买
        normal.confirm ()  # 点击确定
        allure.attach ("余额支付", "选择余额支付")
        normal.balance_pay ()  # 点击余额支付
        price = normal.good_price ()  # 获取商品价格
        allure.attach ("获取结算后的商品价格", f"获取商品的价格{price}")
        print (price)
        normal.submit_order ()  # 点击提交订单
        allure.attach ("输入密码", "确定支付")
        normal.input_pay_pwd ("123456")  # 输入支付密码
        normal.pay_sure ()  # 点击确定
        for i in range (3):
            normal.back ()  # 返回上级
        normal.click_my ()  # 点击我的
        back_balance = normal.show_my_balance ()  # 获取结算后的余额
        allure.attach ("断言", f"获取结算后的余额:{back_balance}")
        assert back_balance == (pre_balance - price) # 判断结算后的月是否等于结算前减去商品价格
        normal.close_mobile()
