from selenium import webdriver
import time
import pandas as pd

class eokul:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome("chromedriver.exe")
        self.username = username
        self.password = password
        self.acts = webdriver.ActionChains(self.browser)
    
    def LogIn(self):
        self.browser.get("https://eokulyd.meb.gov.tr/")
        self.browser.find_element_by_xpath("//*[@id='information']/div/div/a[1]").click()
        time.sleep(20)
        self.browser.get("https://eokulyd.meb.gov.tr/IlkOgretim/OGR/IOG01001.aspx")
    
    def Assign(self, student_id, boy, kilo):
        self.browser.find_element_by_xpath('//*[@id="OGRMenu1_txtTC"]').send_keys(student_id)
        self.browser.find_element_by_xpath('//*[@id="OGRMenu1_btnAra"]').click()
        self.browser.find_element_by_xpath('//*[@id="IOG02000"]/tbody/tr[2]/td').click()
        self.browser.find_element_by_xpath('//*[@id="txtBoy"]').send_keys(boy)

        self.browser.find_element_by_xpath('//*[@id="txtKilo"]').send_keys(kilo)
        self.browser.find_element_by_xpath('//*[@id="IOMToolbarActive1_kaydet_b"]/img').click()

gir = eokul("15019760784", "123456+Ab")
gir.LogIn()

dataset = pd.read_excel("1h sınıf listesi.xlsx")
dataset = dataset.iloc[:-1, [0,2,3]].values
for student in dataset:
    student_id = student[0]
    boy = student[1]
    kilo = int(student[2])
    gir.Assign(student_id, boy, kilo)
