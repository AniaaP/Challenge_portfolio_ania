from pages.base_page import BasePage


class Dashboard(BasePage):

    main_page_menu = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_menu = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_menu = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_button = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    contact_button = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"

    pass