from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import winsound
import smtplib
from email.mime.text import MIMEText


# 使用QQ登录
def login():
    global driver
    options = EdgeOptions()
    # 使用的是新版edge，这是edge驱动
    driver = webdriver.Edge(executable_path='G:\\edgedriver\\MicrosoftWebDriver.exe')
    driver.minimize_window()
    post_url = 'https://yqtb.hust.edu.cn/infoplus/form/18136721/render'

    driver.get(post_url)
    sleep(5)
    qq_login = driver.find_element_by_xpath('//*[@id="u_content_2"]/div/a[1]')
    qq_login.click()
    sleep(5)
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="ptlogin_iframe"]'))
    avatar = driver.find_element_by_xpath('//*[@id="img_out_1528751774"]')
    avatar.click()
    sleep(5)
    driver.get(post_url)
    return driver


def send_email():
    mail_host = 'smtp.qq.com'
    mail_user = '1528751774'
    # 邮箱的授权码
    mail_pass = '*****************'
    # 发送者邮箱
    sender = '*********@qq.com'
    # 接收者邮箱
    receivers = ['*********@qq.com', '*********@qq.com', '*********@qq.com', '*********@qq.com']
    text = '有疫苗了，赶紧打开微校园预约！！！'
    message = MIMEText(text, 'plain', 'utf-8')
    message['Subject'] = '预约疫苗提醒'
    message['From'] = sender
    message['To'] = receivers
    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_host, 25)
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(sender, receivers, message.as_string())
        smtp.quit()
        print('发送成功！！！')
        # 播放30s的音乐进行提醒
        winsound.PlaySound('123.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        sleep(30)
    except:
        print('发送失败！！！')


def main():
    global driver
    driver = None
    count = 0
    # 目标日期
    aim = ['星期日', '星期三', '星期四', '星期五']
    flag = False
    while True:
        if count % 10 == 0:
            if driver is not None:
                driver.close()
            try:
                driver = login()
            except Exception as e:
                print(e)
                continue
        try:
            sleep(5)
            select1_el = driver.find_element_by_id('V1_CTRL162')
            ActionChains(driver).click(driver.find_element_by_id('select2-V1_CTRL162-container')).perform()
            sleep(5)
            ul = driver.find_element_by_xpath('//*[@id="select2-V1_CTRL162-results"]')
            li = ul.find_elements_by_xpath('li')
            for item in li:
                if item.text.split(' ')[-1] in aim:
                    print('有了')
                    send_email()
                    flag = True
                    break
            else:
                print('第', count + 1, '次查看，没有疫苗！！！')
        except Exception as e:
            print(e)
            print('出现错误，刷新重试')
            driver.refresh()
            continue
        if flag:
            if driver is not None:
                driver.close()
            break
        driver.refresh()
        count += 1
        sleep(60 * 3)


if __name__ == '__main__':
    driver = None
    main()
