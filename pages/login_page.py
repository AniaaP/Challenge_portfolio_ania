from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remaind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"
    language_comobox_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button/span[1]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def click_on_the_sign_in_button(self, email):
        self.field_send_keys(self.login_field_xpath, email)