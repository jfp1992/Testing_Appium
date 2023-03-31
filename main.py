import os
import unittest

from appium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

from base_object import BaseObject


class ChessAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/Chess Free.apk'))
        desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_caps['appActivity'] = '.ChessFreeActivity'

        # print(desired_caps)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_single_player_mode(self):
        objects = BaseObject(self.driver)

        objects.button_accept.click()
        objects.button_i_agree.click()
        objects.button_ok.click()
        objects.button_play.click()
        objects.button_continue.click()
        objects.button_single_player.click()
        objects.button_play_game.click()
        objects.button_do_you_wish_to_continue.click()
        objects.button_show_danger.click()

        for i in range(1, 9):
            objects.move_piece(i, 7, i, 5)
            sleep(2)

#—START OF SCRIPT

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)

    unittest.TextTestRunner(verbosity=2).run(suite)
