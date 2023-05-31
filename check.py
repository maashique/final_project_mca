from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path


def main(product):

    product = product
    rateFk, rateAz, source1, source2, proName, proAm, r1, r2, d1, d2, d3 = '', '', '', '', '', '', 'T', 'T', '', '', ''
    img1, img2, newRate, newLink, newPro = '', '', '', '', ''
    rateDu, sourceDu, proDu, desDu, imgDu, resDu = '', '', '', '', '', 'T'
    url1 = "https://www.flipkart.com"
    url2 = "https://www.amazon.in"
    url3 = f"http://127.0.0.1:2000/customerallproducts?search={product}"

    wait_imp = 10
    CO = webdriver.ChromeOptions()
    # CO.add_argument('--headless')

    # CO.add_argument('window-size=1200x600')
    CO.add_experimental_option('useAutomationExtension', False)
    CO.add_argument('--ignore-certificate-errors')
    CO.add_argument('--start-maximized')
    wd = webdriver.Chrome(
        r'C:\\PROJECTS 2022\\ST Thomas\\pricePrediction\\ppApp\\chromedriver.exe', options=CO)

    try:
        wd.get(url3)
        wd.implicitly_wait(wait_imp)

        link1 = wd.find_element(
            "xpath", '/html/body/div[2]/div[2]/div/div/div/div[2]/ul/li/div/form/fieldset/a')
        print(link1.get_attribute('href'))
        rateFlip = wd.find_element(
            "xpath", '/html/body/div[2]/div[2]/div/div/div/div[2]/h3[1]')
        rateDu = rateFlip.text
        proDet = wd.find_element(
            "xpath", '/html/body/div[2]/div[2]/div/div/div/div[2]/h3[1]')
        proDu = proDet.text
        # print(rateFk, proName)

        forD3 = wd.find_element(
            "xpath", '/html/body/div[2]/div[2]/div/div/div/div[2]/h3[2]')
        desDu = forD3.text
        forImg1 = wd.find_element(
            "xpath", '/html/body/div[2]/div[2]/div/div/div/div[1]/i/img')
        imgDu = forImg1.get_attribute('src')
        sourceDu = link1.get_attribute('href')
        time.sleep(2)
    except:
        resDu = 'F'

    print(rateDu, sourceDu, proDu, desDu, imgDu, resDu)


main('pp')
