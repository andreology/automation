from selenium import webdriver

#selecting and clicking elements
driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('11')
getTotalButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
getTotalButton.click()
#dragging and dropping elements
