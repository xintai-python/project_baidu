import sys
sys.path.append('/project_baidu')
from public.base import Page
import time

class clock(Page):
    """
    clock in
    """
    url = '/323876'
    #定位器
    login_loc = ('class name', 'UnLogin-icon')
    login_iframe_loc = ('xpath', '//*[@id="login-passport-frame"]')
    password_login_loc = ('xpath', '//*[@id="loginbox"]/div[2]/div[2]/div[3]/div/span[2]')
    user_loc = ('xpath', '//*[@id="loginbox"]/div[3]/div[2]/div[2]/form/div[1]/div/input')
    password_loc = ('xpath', '//*[@id="loginbox"]/div[3]/div[2]/div[2]/form/div[3]/input[1]')
    button_loc = ('xpath', '//*[@id="loginbox"]/div[3]/div[2]/div[2]/form/div[6]/input')

    #Action
    def user_button(self):
        self.click(self.login_loc)
    def login_iframe(self):
        self.switch_to_frame(self.login_iframe_loc)
    def password_login(self):
        self.click(self.password_login_loc)
    def login_username(self, username):
        self.clear_type(self.user_loc, username)
    def login_password(self, password):
        self.clear_type(self.password_loc, password)
    def login_button(self):
        self.click(self.button_loc)

    def user_login(self, username = '13645712660', password = 'lyk.2353'):
        self.open()
        #time.sleep(15)
        self.user_button()
        #time.sleep(2)
        self.login_iframe()
        self.password_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        time.sleep(1)

#定位器
input_error_loc = ('xpath', '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div')



