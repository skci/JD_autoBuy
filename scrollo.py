from selenium import webdriver

driver = webdriver.Chrome(r'C:\PycharmProjects\TB\chromedriver.exe')
driver.get('https://www.jd.com/')
driver.execute_script('window.scrollTo(window.pageXOffset, document.body.scrollHeight)')