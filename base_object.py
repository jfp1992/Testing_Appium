from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from time import sleep


class BaseObject:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    @property
    def button_accept(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/YesButton")

    @property
    def button_i_agree(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/Button_Accept")

    @property
    def button_ok(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/ContinueButton")

    @property
    def button_play(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/ButtonPlay")

    @property
    def button_continue(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/CrossProm_ExitButton", True)

    @property
    def button_single_player(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/EasyButton", True)

    @property
    def button_play_game(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/NewGameSettings_ContinueButton", True)

    @property
    def button_do_you_wish_to_continue(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/ContinueButton")

    @property
    def button_show_danger(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/ContinueButton")

    @property
    def game_chess_board(self):
        return self.element(By.ID, "uk.co.aifactory.chessfree:id/chess")

    def move_piece(self, from_x, from_y, to_x, to_y):
        board_location_x = self.game_chess_board.location["x"]
        board_location_y = self.game_chess_board.location["y"]

        board_square_size = self.game_chess_board.size["width"] / 8

        from_x = (board_location_x + (board_square_size * from_x)) - (board_square_size / 2)
        from_y = (board_location_y + (board_square_size * from_y)) - (board_square_size / 2)
        to_x = (board_location_x + (board_square_size * to_x)) - (board_square_size / 2)
        to_y = (board_location_y + (board_square_size * to_y)) - (board_square_size / 2)

        self.driver.tap([(from_x, from_y)])
        sleep(0.2)
        self.driver.tap([(to_x, to_y)])

    def wait_for_animation(self, element):
        while True:
            x = element.location['x']
            y = element.location['y']

            sleep(0.1)

            # The following is bad, look away
            # The animation for some menus runs, stops, then runs again.
            if element.location['x'] == x:
                if element.location['y'] == y:
                    sleep(0.200)
                    if element.location['x'] == x:
                        if element.location['y'] == y:
                            break

    def element(self, selector_type, locator, wait_animation=False):
        if wait_animation:
            self.wait_for_animation(self.driver.find_element(selector_type, locator))

        try:
            self.wait.until(EC.element_to_be_clickable, self.driver.find_element(selector_type, locator))
        except:
            print(f"Cannot find '{locator}'")
        return self.driver.find_element(selector_type, locator)
