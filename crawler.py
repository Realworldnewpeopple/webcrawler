import io
import pytesseract
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
from io import BytesIO
try:
    import Image
except ImportError:
    from PIL import Image


def captcha(path):
    return pytesseract.image_to_string(Image.open(path))

def getlink(url,cin):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options, executable_path='./Driver/chromedriver')
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="companyID"]').send_keys(cin)
    element=driver.find_element_by_id('captcha')
    location = element.location
    size = element.size
    png = driver.get_screenshot_as_png() 
    im = Image.open(BytesIO(png)) 
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom)) 
    im.save('./image/screenshot.png') 
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="userEnteredCaptcha"]').send_keys(captcha("./image/screenshot.png"))
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="companyLLPMasterData_0"]').click()
    driver.current_url
    driver.switch_to_window(driver.window_handles[-1])
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    return soup

