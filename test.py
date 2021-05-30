from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import winsound
import smtplib
from email.mime.text import MIMEText


winsound.PlaySound('123.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
sleep(5)
