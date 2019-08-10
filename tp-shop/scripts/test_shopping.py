from page.goods_page import GoodsPage
import pytest
from common.base import open_mobile
import allure
import time

class TestShopping:
    @pytest.allure.severity (pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step (title='促销商品使用余额购物')
    def test_event_good(self):
        """测试活动商品的用例"""
        driver = open_mobile ()
        eventgoods = GoodsPage (driver)  # 实例化活动商品的类
        eventgoods.click_my ()  # 点击
        eventgoods.click_login_register ()  # 点击登录和注册
        eventgoods.input_username ("18000180007")
        eventgoods.input_password ("123456")
        eventgoods.click_login ()  # 点击立即登录
        allure.attach ("登录成功", "进入个人中心")
        time.sleep(3)
        pre_balance = eventgoods.show_my_balance ()  # 显示我的余额
        allure.attach ("获取购物前的余额", f"购物前的账户余额:{pre_balance}")
        eventgoods.back_home ()  # 回到主页
        allure.attach ("点击首页", "跳转到首页")
        eventgoods.click_commodity_promotion ()  # 选择促销商品
        eventgoods.click_good ()  # 选择一件商品
        eventgoods.immediately_buy ()  # 点击立即购买
        eventgoods.confirm ()  # 点击确认提交
        allure.attach ("购买一件商品", "选择")
        eventgoods.balance_pay ()  # 点击余额支付
        allure.attach ("使用余额支付", "购买商品")
        price = eventgoods.good_price ()  # 点击获取商品的价格
        allure.attach ("购买商品后的价格", f"获取商品的价格:{price}")
        eventgoods.submit_order ()  # 点击立即提交
        eventgoods.input_pay_pwd ("123456")  # 输入支付密码
        eventgoods.pay_sure ()  # 确定密码
        allure.attach ("确定支付", "支付成功")
        for i in range (4):
            eventgoods.back ()  # 返回上级
        eventgoods.click_my ()  # 点击我的
        back_balance = eventgoods.show_my_balance ()  # 获取结算后的余额
        allure.attach ("获取结算后的余额", f"获取结算后的余额:{back_balance}")
        assert back_balance == (pre_balance - price)  # 判断结算后的月是否等于结算前减去商品价格
        eventgoods.close_mobile ()