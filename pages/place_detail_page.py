from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PlaceDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def get_place_name(self):
        try:
            business_place_card = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().resourceId("com.google.android.apps.maps:id/business_place_card")')
                )
            )

            element = business_place_card.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.TextView").textContains("Packeta")'
            )

            text = element.text

            return text

        except TimeoutException:
            raise AssertionError("Place detail text was not found.")


    def get_place_address(self):
        if self.is_address_visible():
            try:
                place_page_tabs_container = WebDriverWait(self.driver, 10).until(
                    expected_conditions.presence_of_element_located(
                        (AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().resourceId("com.google.android.apps.maps:id/place_page_tabs_container")')
                    )
                )

                text_view = place_page_tabs_container.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.TextView").textContains("Českomoravská 2408, 190 00 Praha 9-Libeň")'
                )

                text = text_view.text

                return text

            except TimeoutException:
                raise AssertionError("Address was not found.")
        else:
            raise AssertionError("Address was not found.")


    def scroll_down(self):
        size = self.driver.get_window_size()

        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": int(size["width"] * 0.1),
                "top": int(size["height"] * 0.3),
                "width": int(size["width"] * 0.8),
                "height": int(size["height"] * 0.5),
                "direction": "down",
                "percent": 0.7,
            }
        )

    def is_address_visible(self):
        for _ in range(10):
            elements = self.driver.find_elements(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().descriptionContains("Address: ")'
            )

            if elements:
                return True
            else:
                self.scroll_down()

        return False

