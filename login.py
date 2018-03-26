from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from getverificationcode import *
import os

student_id = ''
password = ''

aao_url = 'https://zhjw.neu.edu.cn/'
suitable_window_width = 850
suitable_window_height = 800
sub_shot_site = (450, 462, 505, 481)

chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://zhjw.neu.edu.cn'
driver.get(url)
driver.set_window_size(suitable_window_width, suitable_window_height)
driver.get_screenshot_as_file("shot.png")
image = Image .open('shot.png')
image = image.crop(sub_shot_site)
verification_code = get_verification_code(image)
# print(verification_code)

input_text = driver.find_element_by_id('WebUserNO')
input_text.send_keys(student_id)
input_text = driver.find_element_by_id('Password')
input_text.send_keys(password)
input_text = driver.find_element_by_id('Agnomen')
input_text.send_keys(eval(verification_code))
input_text.submit()

# driver.quit()
os.remove('shot.png')
