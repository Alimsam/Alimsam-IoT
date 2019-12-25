from selenium import webdriver
from finger.py import isFinger, characterics
options = webdriver.ChromeOptions()
options.add_argument('#headless')

# browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', options=options)  # 크롬 드라이버 구동
driver.implicitly_wait(3) 

fingerData=""
isFinger=""
# driver.get("http://10.120.73.120:3000/finger") 
driver.get("https://alimsam.herokuapp.com/finger?isFinger=",isFinger,"&fingerData=",fingerData)
driver.implicitly_wait(3) 
driver.find_element_by_xpath('//*[@class="fingerName"]').send_keys('success') 
driver.implicitly_wait(4) 
driver.find_element_by_xpath('//*[@class="submit"]').click()
