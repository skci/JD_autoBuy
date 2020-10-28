from selenium import webdriver
import datetime
from time import sleep


def login():
    driver.get('https://www.jd.com/')

    '''点击登录按钮'''
    driver.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()

    '''点击微信登录'''
    driver.find_element_by_xpath('//*[@id="kbCoagent"]/ul/li[2]/a/span').click()
    print('Loading', end='')

    '''通过检测登录状态，判断是否进入购物车'''
    while True:
        try:
            if driver.find_element_by_xpath('//*[@id="J_user"]/div/div[1]/div[2]/p[2]/a[3]'):
                driver.get('https://cart.jd.com/cart.action')
                break
        except:
            sleep(0.2)
            print('.', end='')
    print('\n')

def buy(times, submit):
    '''第二个参数用于中断循环'''

    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > times:

            '''点击结算'''
            while submit:
                try:
                    if driver.find_element_by_xpath(
                            '//*[@id="cart-floatbar"]/div/div/div/div[2]/div[4]/div[1]/div/div[1]/a/b'):
                        driver.find_element_by_xpath(
                            '//*[@id="cart-floatbar"]/div/div/div/div[2]/div[4]/div[1]/div/div[1]/a/b').click()
                        break
                except:
                    print('找不到结算!')

            '''点击提交'''
            while submit:
                try:
                    if driver.find_element_by_xpath('//*[@id="order-submit"]/b'):
                        driver.find_element_by_xpath('//*[@id="order-submit"]/b').click()
                        submit = False
                        break
                except:
                    print('找不到提交!')


if __name__ == '__main__':

    '''输入抢购时间'''
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    times = input('输入抢购时间，例如：' + t + '\n')

    '''打开浏览器'''
    driver = webdriver.Chrome(r'D:\code\Python\PycharmProjects\TB\chromedriver.exe')
    driver.set_window_size(1300, 750)

    '''执行操作'''
    login()
    buy(times, True)
