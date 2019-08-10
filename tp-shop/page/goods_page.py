from common.base import Base
from common.base import open_mobile


class GoodsPage (Base):
    """
    继承Base类
    封装表现层
    """
    my_loc = ("id", "com.tpshop.malls:id/mine_img")  # 我的
    login_register_loc = ("id", "com.tpshop.malls:id/head_img")  # 登录
    user_loc = ("id", "com.tpshop.malls:id/mobile_et")  # 用户名
    pwd_loc = ("id", "com.tpshop.malls:id/pwd_et")  # 密码
    login_loc = ("id", "com.tpshop.malls:id/login_tv")  # 登录
    homepage_loc = ("id", "com.tpshop.malls:id/home_tv")  # 首页
    commodity_promotion_loc = ("id", "com.tpshop.malls:id/home_menu_promote_layout")  # 商品促销
    good_loc = ("id", "com.tpshop.malls:id/product_pic_img")  # 定位商品
    immediately_buy_loc = ("id", "com.tpshop.malls:id/promptly_buy_tv")  # 立即购买
    comfirm_loc = ("id", "com.tpshop.malls:id/confirm_tv")  # 确定按钮
    choice_address_loc = ("id", "com.tpshop.malls:id/consignee_address_tv")  # 选择收货地址
    balance_loc = ("id", "com.tpshop.malls:id/order_balance_sth")  # 使用余额支付
    submit_order_loc = ("id", "com.tpshop.malls:id/submit_tv")  # 提交订单
    pay_pwd_loc = ("id", "com.tpshop.malls:id/pwd_et")  # 支付密码
    pay_sure_loc = ("id", "com.tpshop.malls:id/sure_tv")  # 支付确认
    my_balance_loc = ("id", "com.tpshop.malls:id/balance_tv")  # 我的余额
    good_price_loc = ("id", "com.tpshop.malls:id/balance_fee_tv")  # 商品价格
    # 非参与活动的商品定位器
    classify_loc = ("id", "com.tpshop.malls:id/category_ll")  # 分类
    art_loc = ("xpath", "//*[@text='艺术']")  # 艺术
    oil_loc = ("xpath", "//*[@text='油画']")  # 油画
    oil_good_loc = ("class name", "android.widget.ImageView")  # 商品
    rice_loc = ("xpath", "//*[@text='荔泉大米']")

    def click_my(self):
        """点击我的"""
        self.click (self.my_loc)

    def click_login_register(self):
        """点击登录/注册"""
        self.click (self.login_register_loc)

    def input_username(self, text):
        """输入用户名"""
        self.send_keys (self.user_loc, text)

    def input_password(self, text):
        """输入密码"""
        self.send_keys (self.pwd_loc, text)

    def click_login(self):
        """点击登录"""
        self.click (self.login_loc)

    def back_home(self):
        """回到首页"""
        self.click (self.homepage_loc)

    def click_commodity_promotion(self):
        """点击商品促销"""
        self.click (self.commodity_promotion_loc)

    def click_good(self):
        """点击商品"""
        good = self.find_elements (self.good_loc)
        good[3].click ()

    def immediately_buy(self):
        """立即购买"""
        self.click (self.immediately_buy_loc)

    def confirm(self):
        """确认按钮"""
        self.click (self.comfirm_loc)

    def balance_pay(self):
        """使用余额支付"""
        self.click (self.balance_loc)

    def submit_order(self):
        """提交订单"""
        self.click (self.submit_order_loc)

    def input_pay_pwd(self, text):
        """输入支付密码"""
        self.send_keys (self.pay_pwd_loc, text)

    def pay_sure(self):
        """支付确认"""
        self.click (self.pay_sure_loc)

    def show_my_balance(self):
        """显示我的余额"""
        balanec = self.find_element (self.my_balance_loc)
        b = balanec.get_attribute ("text")
        b = float (b)
        return b
        # 获取余额,购物开始前获取一次,购物时获取一次货物的余额
        # 购物完成后,在获取一次余额,判断开始-货物=结束

    def classify(self):
        """分类标签"""
        self.click (self.classify_loc)

    def art(self):
        """艺术"""
        self.click (self.art_loc)

    def oil(self):
        """油画"""
        self.click (self.oil_loc)

    def oil_good(self):
        """油画作品"""
        elements = self.find_elements (self.oil_good_loc)
        elements[1].click ()

    def good_price(self):
        """显示商品的价格"""
        price = self.find_element (self.good_price_loc)
        pri = price.get_attribute ("text")
        p = pri[1:]
        p = float (p)
        return p

    def rice(self):
        """点击大米"""
        self.click (self.rice_loc)


if __name__ == '__main__':
    driver = open_mobile ()
    e = GoodsPage (driver)
    e.click_my ()
    e.click_login_register ()
    e.input_username ("17311330120")
    e.input_password ("123456")
    e.click_login ()
    e.back_home ()
    e.click_commodity_promotion ()
    e.click_good ()
    e.immediately_buy ()
    e.confirm ()
    e.balance_pay ()
    e.submit_order ()
