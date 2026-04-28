from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class GoogleMapsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    def search_for(self, search_text: str):
        search_box = self.find_search_box()

        search_box.click()
        search_box.clear()
        search_box.send_keys(search_text)

        self.select_search_suggestion(search_text)


    def find_search_box(self):
        try:
            search_box = WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().resourceId("com.google.android.apps.maps:id/search_omnibox_text_box")'
                    )
                )
            )

            search_box.click()

            return WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().resourceId("com.google.android.apps.maps:id/search_omnibox_edit_text")'
                    )
                )
            )

        except TimeoutException:
            raise AssertionError("Search box was not found.")


    def select_search_suggestion(self, search_text: str):
        try:
            typed_suggest_container = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().resourceId("com.google.android.apps.maps:id/typed_suggest_container")'
                    )
                )
            )

            suggestion = typed_suggest_container.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().className("android.widget.TextView").text("{search_text}")'
            )

            suggestion.click()
            return

        except TimeoutException:
            self.driver.press_keycode(66)