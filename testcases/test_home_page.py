from selenium import webdriver
from Config.app_url import Testdata
import pytest
import time

@pytest.mark.demo
def test_verify_home_page(setup):
    driver = setup
    baseUrl =Testdata.BASE_URL
    driver.get(baseUrl)
    time.sleep(5)
    act_title = driver.title
    print(act_title)
    if act_title == "Paytm.com – Recharge & Utility Payments, Entertainment, Travel, DTH, Wallet & Payments":
        assert True
        driver.close()

    else:
        driver.save_screenshot("..\\Screenshots\\" + "test_homePageTitle1.png")
        driver.close()
        assert False








