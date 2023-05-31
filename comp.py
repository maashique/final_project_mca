from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path


def main(product):

    product = product
    rateFk, rateAz, source1, source2, proName, proAm, r1, r2, d1, d2, d3 = '', '', '', '', '', '', 'T', 'T', '', '', ''
    img1, img2, newRate, newLink, newPro = '', '', '', '', ''
    rateDu, sourceDu, proDu, desDu, imgDu, resDu = '', '', '', '', '', ''
    url1 = "https://www.flipkart.com"
    url2 = "https://www.amazon.in"
    url3 = f"http://127.0.0.1:2000/customerallproducts?search={product}"

    wait_imp = 10
    CO = webdriver.ChromeOptions()
    CO.add_argument('--headless')

    # CO.add_argument('window-size=1200x600')
    CO.add_experimental_option('useAutomationExtension', False)
    CO.add_argument('--ignore-certificate-errors')
    CO.add_argument('--start-maximized')
    wd = webdriver.Chrome(
        r'D:\\Final Project\\pricePrediction\\ppApp\\chromedriver.exe', options=CO)

    try:
        wd.get(url1)
        wd.implicitly_wait(wait_imp)

        search1 = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys(product)
        button1 = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form').submit()

        link1 = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a')

        print(link1.get_attribute('href'))

        # source1 = "https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRAH33S3&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=3bdbc1fe-fb28-4b87-b9dd-5cfa9bca72f7.MOBF944E5FTGHNCR.SEARCH&ppt=sp&ppn=sp&ssid=dh4th365ow0000001584871616021&qH=0b3f45b266a97d70"
        # source2 = "https://www.amazon.in/OnePlus-Nord-Shadow-128GB-Storage/dp/B0B3CQBRB4/ref=lp_1389401031_1_10?th=1"

        rateFlip = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div')
        rateFk = rateFlip.text
        proDet = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
        proName = proDet.text
        # print(rateFk, proName)
        forD1 = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[3]/ul/li[1]')
        d1 = forD1.text
        forD2 = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[3]/ul/li[2]')
        d2 = forD2.text
        forD3 = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[3]/ul/li[3]')
        d3 = forD3.text
        forImg1 = wd.find_element(
            "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[1]/div[1]/div/div/img')
        img1 = forImg1.get_attribute('src')
        source1 = link1.get_attribute('href')

        # create a webdriver object for chrome-option and configure
        # wait_imp = 10
        # CO = webdriver.ChromeOptions()
        # CO.add_experimental_option('useAutomationExtension', False)
        # CO.add_argument('--ignore-certificate-errors')
        # CO.add_argument('--start-maximized')
        # wd = webdriver.Chrome(
        #     r'C:\\PROJECTS 2022\\ST Thomas\\PricePrediction\\testing\\chromedriver.exe', options=CO)
        # print("*************************************************************************** \n")
        # print("                     Starting Program, Please wait ..... \n")

        # print("Connecting to Flipkart")
        # wd.get(source1)
        # wd.implicitly_wait(wait_imp)
        # # f_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
        # f_price = wd.find_element(
        #     "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div')

        # pr_name = wd.find_element(
        #     "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span')
        # product = pr_name.text
        # r_price = f_price.text
        # print("Price available at Flipkart is: "+r_price[1:])
        # print(r_price[1:])
        # print(" ---> Successfully retrieved the price from Flipkart \n")
        time.sleep(2)
    except:
        try:
            link1 = wd.find_element(
                "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]')

            print(link1.get_attribute('href'))

            rateFlip = wd.find_element(
                "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[3]/div[1]/div[1]')
            rateFk = rateFlip.text
            proDet = wd.find_element(
                "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[2]')
            proName = proDet.text
            source1 = link1.get_attribute('href')
            forImg1 = wd.find_element(
                "xpath", '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[1]/div[1]/div/div/img')
            img1 = forImg1.get_attribute('src')
            time.sleep(2)
        except:
            r1 = 'F'
    try:
        wd.get(url2)
        wd.implicitly_wait(wait_imp)

        search2 = wd.find_element(
            "xpath", '//*[@id="twotabsearchtextbox"]').send_keys(product)
        button2 = wd.find_element(
            "xpath", '//*[@id="nav-search-bar-form"]').submit()

        cks = [4, 5, 6, 7, 8]

        newLink = ''
        newRate = ''
        newPro = ''

        link3 = wd.find_element(
            "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a')
        source3 = link3.get_attribute('href')
        rateAma3 = wd.find_element(
            "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]/span[2]')
        rateAz3 = rateAma3.text
        proAma3 = wd.find_element(
            "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')

        proAm3 = proAma3.text

        print(f"3 -{proAm3}")
##################################################################################
        link4 = wd.find_element(
            "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a')
        source4 = link4.get_attribute('href')
        rateAma4 = wd.find_element(
            "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span/span[2]/span[2]')
        rateAz4 = rateAma4.text
        proAma4 = wd.find_element(
            "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')

        proAm4 = proAma4.text
        print(f"4 -{proAm4}")
##################################################################################
        print(product.lower() in proAm3.lower())
        print(product.lower() in proAm4.lower())
        if (product.lower() in proAm3.lower()):
            newLink = source3
            newRate = rateAz3
            newPro = proAm3
            print("worked 3")
        elif (product.lower() in proAm4.lower()):
            newLink = source4
            newRate = rateAz4
            newPro = proAm4
            print("worked 4")
        else:
            raise Exception()
        # forImg2 = wd.find_element(
        #     "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
        # img2 = forImg2.get_attribute('src')
        time.sleep(2)
    except:
        try:
            wd.get(url2)
            wd.implicitly_wait(wait_imp)

            search2 = wd.find_element(
                "xpath", '//*[@id="twotabsearchtextbox"]').send_keys(product)
            button2 = wd.find_element(
                "xpath", '//*[@id="nav-search-bar-form"]').submit()

            cks = [4, 5, 6, 7, 8]

            newLink = ''
            newRate = ''
            newPro = ''
            link4 = wd.find_element(
                "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[3]/div[1]/a')
            newLink = link4.get_attribute('href')
            rateAma4 = wd.find_element(
                "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[3]/div[1]/a/span[1]/span[1]')
            newRate = rateAma4.text
            proAma4 = wd.find_element(
                "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[1]/h2/a/span')

            newPro = proAma4.text
            # forImg2 = wd.find_element(
            #     "xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
            # img2 = forImg2.get_attribute('src')
            time.sleep(2)
        except:
            r2 = 'F'
   
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
    # Final display
    # print("#------------------------------------------------------------------------#")
    # print(
    #     "Price for [{}] on all websites, Prices are in INR \n".format(product))
    # print("Price available at Flipkart is: "+rateFk)
    # print("Price available at Amazon is: "+rateAz)
    return (product, rateFk, newRate, source1, newLink, proName, newPro, r1, r2, img1, img1, d1, d2, d3, rateDu, sourceDu, proDu, desDu, imgDu, resDu)
