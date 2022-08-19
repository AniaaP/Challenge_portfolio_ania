import time

from pages.base_page import BasePage


def title_of_page(self):
    self.wait_for_element_to_be_clickable(self.add_player_button)
    assert self.get_page_title(self.dashboard_url) == self.expected_title

class Dashboard(BasePage):
    add_player_button = "//*[text()='Add player']"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    element = "//*[@id='__next']/form/div/div[1]/h5"
    element_text = "Scouts Panel"

    head_1 = "//*[@id='__next']/div[1]/header/div/h6"
    main_page_menu = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_menu = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_menu = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_button = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    contact_button = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    last_update_player_name = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    last_updated_report_name = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
    logo_image = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[1]"

    def title_of_page(self):
        pass