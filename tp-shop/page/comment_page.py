from common.base import Base
from common.base import open_mobile
from appium import webdriver


class CommentPage (Base):
    """封装评论表现层"""
    my_loc = ("id", "com.tpshop.malls:id/mine_img")  # 我的
    login_register_loc = ("id", "com.tpshop.malls:id/head_img")  # 登录
    user_loc = ("id", "com.tpshop.malls:id/mobile_et")  # 用户名
    pwd_loc = ("id", "com.tpshop.malls:id/pwd_et")  # 密码
    login_loc = ("id", "com.tpshop.malls:id/login_tv")  # 登录
    wait_comment_loc = ("id", "com.tpshop.malls:id/wait_comment_ll")  # 待评论
    pre_comment_loc = ("id", "com.tpshop.malls:id/product_name_tv")  # 评论前
    order_show_loc = ("id", "com.tpshop.malls:id/order_show_btn")  # 评论晒单
    comment_loc = ("id", "com.tpshop.malls:id/comment_content_et")  # 评论内容
    start_line_loc = ("class name", "android.widget.LinearLayout")  # 星星行
    good_lever_loc = ("id", "com.tpshop.malls:id/product_lever_star")  # 商品等级
    start_loc = ("id", "com.tpshop.malls:id/star5_btn")  # 五星
    submit_loc = ("xpath", "//*[@text='提交']")  # 提交
    back_my_loc = ("id", "com.tpshop.malls:id/title_back_rl")  # 回到我的
    already_comment_loc = [425, 110]  # 已评价坐标
    back_comment_loc = ("id", "com.tpshop.malls:id/product_name_tv")  # 评论后的

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

    def wait_comment(self):
        """等待评论"""
        self.click (self.wait_comment_loc)

    def order_show(self):
        """评论晒单"""
        self.click (self.order_show_loc)

    def comment(self, text):
        """评论内容"""
        self.send_keys (self.comment_loc, text)

    def good_level(self):
        """商品等级"""
        element = self.find_element (self.good_lever_loc)
        if element:
            self.click (self.start_loc)

    def play_start(self):
        """打星星"""
        lines = self.find_elements (self.start_loc)
        for line in lines:
            line.click ()

    def submit(self):
        """提交"""
        self.click (self.submit_loc)

    def already_comment(self):
        """已经评价"""
        self.tap_tap (x=self.already_comment_loc[0], y=self.already_comment_loc[1])

    def pre_comment_text(self):
        """获取评价商品的文本"""
        elements = self.find_elements (self.pre_comment_loc)
        text = elements[0].get_attribute ("text")
        return text

    def back_comment_text(self):
        """获取评价后的文本"""
        elements = self.find_elements (self.back_comment_loc)
        return elements


