from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.common.exceptions import TimeoutException
import pytest
import openpyxl
from constants.sifreConstants import *
import json
import imaplib
import email
from selenium.webdriver.common.keys import Keys
from Test_constantClas import *
from selenium.webdriver.common.alert import Alert

class Test_Sifre():
      def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)

      def teardown_method(self):
        self.driver.quit()

      def test_invalidMail(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         sifremiUnuttumButton = self.waitForElelemetVisible((By.CSS_SELECTOR,sifremiUnuttumCss))
         sifremiUnuttumButton.click()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(gecersizformatmail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         gecersizformatMailText = self.waitForElelemetVisible((By.CSS_SELECTOR,popupCss))
         assert gecersizformatMailText.text == gecersizformattext
      
      def test_succesPasswordReset(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         sifremiUnuttumButton = self.waitForElelemetVisible((By.CSS_SELECTOR,sifremiUnuttumCss))
         sifremiUnuttumButton.click()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(validemail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         self.driver=webdriver.Chrome()
         self.driver.maximize_window()
         self.driver.get("https://mail.google.com/mail/u/0/#inbox")
         email_giris=self.waitForElelemetVisible((By.ID, "identifierId"))
         sleep(3)
         email_giris.send_keys(validemail)
         email_giris.click()
         sonraki= self.waitForElelemetVisible((By.XPATH, "//div[@id='identifierNext']/div/button/span"))
         sonraki.click()

         password=self.waitForElelemetVisible((By.CSS_SELECTOR,passwordCSS))
         password.send_keys(validPassword)
         simdi_giris_yap=self.waitForElelemetVisible((By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d"))
         simdi_giris_yap.click()
          # İlk mesajı bulmak için bekleyici oluştur
         window_before = self.driver.window_handles[0]
         sleep(1)
         first_message = self.waitForElelemetVisible((By.XPATH, "(//*[@jscontroller='ZdOxDb'])[1]"))
         first_message.click()  # İlk mesaja tıkla

         self.driver.execute_script("window.scrollTo(0,200)")
         sleep(2)
         first_messageLink = self.waitForElelemetVisible((By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/div/div/div/p/span/a"))
         first_messageLink.click()
         sleep(5)

         window_after = self.driver.window_handles[1]
         self.driver.switch_to.window(window_after)
         yeniSifreInput = self.waitForElelemetVisible((By.XPATH,yeniSifreXpath))
         yeniSifreInput.send_keys(yeniSifreBelirleme)
         yeniSifreTekrarInput = self.waitForElelemetVisible((By.XPATH,sifreTekrarXpath))
         yeniSifreTekrarInput.send_keys(yeniSifreBelirleme)
         gonderButon = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss))
         gonderButon.click()
         sleep(7)
         succesResetText = self.waitForElelemetVisible((By.CSS_SELECTOR,popupCss))
         assert succesResetText.text == sifreSifirlamaBasariliText
         sleep(3)
        # bununun yerine yeni password ile giris yapalim


      
      def test_unregisteredMail(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         sifremiUnuttumButton = self.waitForElelemetVisible((By.CSS_SELECTOR,sifremiUnuttumCss))
         sifremiUnuttumButton.click()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(unregisteredMail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         unregisteredText = self.waitForElelemetVisible((By.CSS_SELECTOR,popupCss))
         assert unregisteredText.text == gecersizformattext
       
      def test_notMatchPassword(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         sifremiUnuttumButton = self.waitForElelemetVisible((By.CSS_SELECTOR,sifremiUnuttumCss))
         sifremiUnuttumButton.click()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(validemail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         Test_notMatchPassword().test_linkionaylama()

         try:
          notMatchPasswordText = self.waitForElelemetVisible((By.CSS_SELECTOR,popupCss))
          assert notMatchPasswordText.text == sifreEslesmediText
        
         except TimeoutException:
          pytest.fail("Success message did not appear within 10 seconds")

         

      def waitForElelemetVisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
      

      

    


      # def waitForAllElelemetVisible(self,locators,timeout=5):
      #   return WebDriverWait(self.driver,timeout).until(ec.visibility_of_all_elements_located(locators))
      # def waitForElelemetInvisible(self,locator,timeout=5):
      #   return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))


  
