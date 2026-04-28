from appium.options.android import UiAutomator2Options


def get_google_maps_options() -> UiAutomator2Options:
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"

    options.app_package = "com.google.android.apps.maps"
    options.app_activity = "com.google.android.maps.MapsActivity"

    options.no_reset = True
    options.new_command_timeout = 120

    return options