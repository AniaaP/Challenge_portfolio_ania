import os
import time
import unittest

from selenium import webdriver

from pages.add_player import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerForm(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_fill_in_add_player_form(self):
        add_player_form = AddPlayer(self.driver)
        add_player_form.type_in_name('Adam')
        add_player_form.type_in_surname('Kowalski')
        add_player_form.type_in_age('1989-05-20')
        add_player_form.type_in_main_position('bramkarz')
        add_player_form.click_on_the_submit_button()


    @classmethod
    def tearDown(self):
        self.driver.quit()
