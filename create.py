import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "/Users/peter/Documents/Github/"
browser = webdriver.Chrome()
browser.get("http://github.com/login")

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def create():
    folderName = str(sys.argv[1])
    createFolder("../" + str(sys.argv[1]) + "/")
    python_button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    python_button.send_keys("pette1999")
    python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
    python_button.send_keys("Meiguo1969")
    python_button = browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[4]")[0]
    python_button.submit()
    python_button = browser.find_elements_by_xpath("/html/body/div[1]/header/div[7]/details/summary")[0]
    python_button.click()
    python_button = browser.find_elements_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/a[1]")[0]
    python_button.click()
    python_button = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    python_button.send_keys(folderName)
    python_button = browser.find_element_by_css_selector("button.first-in-line")
    python_button.submit()

    # browser.get("https://github.com/pette1999/" + folderName + "/settings")
    # browser.find_element_by_tag_name('body').send_keys(Keys.END)
    # python_button = browser.find_element_by_css_selector("#options_bucket > div:nth-of-type(9) > ul > li:nth-of-type(4) > details > summary")
    # python_button.click()
    # python_button = browser.find_elements_by_xpath("//*[@id='options_bucket']/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input")[0]
    # python_button.send_keys(folderName)
    # python_button = browser.find_elements_by_xpath("//*[@id='options_bucket']/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button")[0]
    # python_button.submit()


if __name__ == "__main__":
    create()
