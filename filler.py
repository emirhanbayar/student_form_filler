from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
from studentclass import Student
import pandas as pd
from selenium.webdriver.common.keys import Keys

class eokul:
    def __init__(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.acts = webdriver.ActionChains(self.browser)
    
    def LogIn(self):
        self.browser.get("https://eokulyd.meb.gov.tr/")
        self.browser.find_element_by_xpath("//*[@id='information']/div/div/a[1]").click()
        time.sleep(30)
    
    def Assign(self, student):
        self.browser.get("https://eokulyd.meb.gov.tr/IlkOgretim/OGR/IOG01001.aspx")
        self.browser.find_element_by_xpath('//*[@id="OGRMenu1_txtTC"]').send_keys(student.student_id)
        self.browser.find_element_by_xpath('//*[@id="OGRMenu1_btnAra"]').click()
        self.browser.find_element_by_xpath('//*[@id="IOG02000"]/tbody/tr[2]/td').click()

        accom = self.browser.find_element_by_xpath('//*[@id="ddlKiminleOturuyor"]')
        select = Select(accom)
        select.select_by_visible_text(student.accom) 
        
        rent = self.browser.find_element_by_xpath('//*[@id="ddlEvKirami"]')
        select = Select(rent)
        select.select_by_visible_text(student.rent)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlOdasiVarmi"]')).select_by_visible_text(student.room)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlEvNeIleIsiniyor"]')).select_by_visible_text(student.heat)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlOkulaNasilGeliyor"]')).select_by_visible_text(student.transp)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlCalisiyormu"]')).select_by_visible_text(student.work)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlBaskaKalanVarmi"]')).select_by_visible_text(student.outstay)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlGecirdigiKaza"]')).select_by_visible_text(student.accident)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlGecirdigiAmeliyat"]')).select_by_visible_text(student.oper)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlKullandigiCihaz"]')).select_by_visible_text(student.protez)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlGecirdigiHastalik"]')).select_by_visible_text(student.illpass)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlSurekliHastalik"]')).select_by_visible_text(student.illness1)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlSurekliIlac"]')).select_by_visible_text(student.drug)

        self.browser.find_element_by_xpath('//*[@id="txtKardesSayisi"]').clear()
        self.browser.find_element_by_xpath('//*[@id="txtKardesSayisi"]').send_keys(student.broth)

        Select(self.browser.find_element_by_xpath('//*[@id="ddlDigerSurekliHas"]')).select_by_visible_text(student.illness2)

        self.browser.find_element_by_xpath('//*[@id="txtKisiSayisi"]').clear()
        self.browser.find_element_by_xpath('//*[@id="txtKisiSayisi"]').send_keys(student.family_number)

        time.sleep(1)

        self.browser.find_element_by_xpath('//*[@id="IOMToolbarActive1_kaydet_b"]/img').click()

        time.sleep(1)

gir = eokul()
gir.LogIn()

dataset = pd.read_excel("data.xlsx")
dataset = dataset.iloc[:, [1, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]].values


for data in dataset:    
    student = Student(data)
    gir.Assign(student)