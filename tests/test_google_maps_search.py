import os
from datetime import datetime

import pytest
from appium import webdriver

from helpers.capabilities import get_google_maps_options
from pages.google_maps_page import GoogleMapsPage
from pages.place_detail_page import PlaceDetailPage


@pytest.fixture
def driver():
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=get_google_maps_options(),
    )

    driver.terminate_app("com.google.android.apps.maps")
    driver.activate_app("com.google.android.apps.maps")

    yield driver

    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"reports/final_screen_{timestamp}.png")
    driver.quit()


def test_google_maps_search(driver):
    google_maps_page = GoogleMapsPage(driver)
    place_detail_page = PlaceDetailPage(driver)

    google_maps_page.search_for("Packeta Group")

    detail_text = place_detail_page.get_place_name()
    address_text = place_detail_page.get_place_address()

    assert "Packeta Group" in detail_text or "Packeta s.r.o." in detail_text
    assert "Českomoravská 2408, 190 00 Praha 9-Libeň" in address_text