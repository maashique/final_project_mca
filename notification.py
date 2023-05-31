from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path


def flip(url):

    wait_imp = 10
    CO = webdriver.ChromeOptions()
    CO.add_argument('--headless')

    # CO.add_argument('window-size=1200x600')
    CO.add_experimental_option('useAutomationExtension', False)
    CO.add_argument('--ignore-certificate-errors')
    CO.add_argument('--start-maximized')
    wd = webdriver.Chrome(
        r'C:\\PROJECTS 2022\\ST Thomas\\pricePrediction\\ppApp\\chromedriver.exe', options=CO)

    try:
        wd.get(url)
        wd.implicitly_wait(wait_imp)

        rateFlip = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[1]')

        rateFk = rateFlip.text
        offFlip = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[3]/div/div[4]/div[1]/div/div[3]/span')

        offFk = offFlip.text
        print(rateFk)
        res = True
        time.sleep(2)
    except:
        res = False
        rateFk = ''
        offFk = ''

    return (rateFk, res, offFk)


def ama(url):

    wait_imp = 10
    CO = webdriver.ChromeOptions()
    CO.add_argument('--headless')

    # CO.add_argument('window-size=1200x600')
    CO.add_experimental_option('useAutomationExtension', False)
    CO.add_argument('--ignore-certificate-errors')
    CO.add_argument('--start-maximized')
    wd = webdriver.Chrome(
        r'C:\\PROJECTS 2022\\ST Thomas\\pricePrediction\\ppApp\\chromedriver.exe', options=CO)

    try:
        wd.get(url)
        wd.implicitly_wait(wait_imp)

        rateAma = wd.find_element(
            "xpath", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
        rateFk = rateAma.text
        offAma = wd.find_element(
            "xpath", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]')
        offFk = offAma.text

        res = True
        time.sleep(2)
    except:
        res = False
        rateFk = ''
        offFk = ''

    return (rateFk, res, offFk)
