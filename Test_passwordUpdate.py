from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.common.exceptions import TimeoutException
import pytest
from constants.passwordConstants import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sifre():
      def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)

      def teardown_method(self):
        self.driver.quit()
      
      def waitForElelemetVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
     
      def waitForElelemetInvisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))
      
      def login(self):
         emailInput = self.waitForElelemetVisible((By.XPATH,emailInputXpath)) 
         emailInput.send_keys(validemail)
         passwordInput =self.waitForElelemetVisible((By.XPATH,passwordInputXpath))
         passwordInput.send_keys(randomPassword)
         girisButton = self.waitForElelemetVisible((By.CSS_SELECTOR,girisYapButtonCss))
         girisButton.click()

      def preCondition(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         sifremiUnuttumButton = self.waitForElelemetVisible((By.CSS_SELECTOR,sifremiUnuttumCss))
         sifremiUnuttumButton.click()

      def gmailLogin(self):
         self.driver=webdriver.Chrome()
         self.driver.maximize_window()
         self.driver.get(gmailUrl)
         email_giris=self.waitForElelemetVisible((By.ID, emailBoxId))
         sleep(3)
         email_giris.send_keys(validemail)
         email_giris.click()
         self.waitForElelemetVisible((By.XPATH, afterXpath)).click()
         password=self.waitForElelemetVisible((By.CSS_SELECTOR,passwordCSS))
         password.send_keys(validPassword)
         self.waitForElelemetVisible((By.CSS_SELECTOR, nowLoginCss)).click()

         window_before = self.driver.window_handles[0]
         sleep(1)
         first_message = self.waitForElelemetVisible((By.XPATH, inboxFirstMessageXpath))
         first_message.click()  

         self.driver.execute_script("window.scrollTo(0,200)")
         sleep(2)
         first_messageLink = self.waitForElelemetVisible((By.XPATH, firstMessageLinkXpath))
         first_messageLink.click()
         sleep(5)


      def test_invalidMail(self):
         self.preCondition()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(gecersizformatmail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         gecersizformatMailText = self.waitForElelemetVisible((By.CSS_SELECTOR,popupCss))
         assert gecersizformatMailText.text == gecersizformattext
      
      def test_succesPasswordReset(self):
         self.preCondition()

         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(validemail)
         self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
        
         self.gmailLogin()
         window_after = self.driver.window_handles[1]
         self.driver.switch_to.window(window_after)
         yeniSifreInput = self.waitForElelemetVisible((By.XPATH,yeniSifreXpath))
         yeniSifreInput.send_keys(randomPassword)
         yeniSifreTekrarInput = self.waitForElelemetVisible((By.XPATH,sifreTekrarXpath))
         yeniSifreTekrarInput.send_keys(randomPassword)
         gonderButon = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss))
         gonderButon.click()
         
        
         succesResetText = self.waitForElelemetVisible((By.XPATH,alertXpath))
         assert succesResetText.text == sifreSifirlamaBasariliText
         sleep(5)
         self.login()
      
      
      def test_unregisteredMail(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         self.preCondition()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(unregisteredMail)
         self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()
         unregisteredText = self.waitForElelemetVisible((By.XPATH,alertXpath))
         assert unregisteredText.text == gecersizformattext
       
      def test_notMatchPassword(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)

         self.preCondition()

         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(validemail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()

         self.gmailLogin()
         window_after = self.driver.window_handles[1]
         self.driver.switch_to.window(window_after)
         yeniSifreInput = self.waitForElelemetVisible((By.XPATH,yeniSifreXpath))
         yeniSifreInput.send_keys(randomPassword)
         yeniSifreTekrarInput = self.waitForElelemetVisible((By.XPATH,sifreTekrarXpath))
         yeniSifreTekrarInput.send_keys(uyumsuzSifre)
         gonderButon = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss))
         gonderButon.click()
         

         try:
          notMatchPasswordText = self.waitForElelemetVisible((By.XPATH,alertXpath))
          assert notMatchPasswordText.text == sifreEslesmediText
        
         except TimeoutException:
          pytest.fail("Success message did not appear within 5 seconds")
      

      def test_oldPasswordReset(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         self.preCondition()
         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(validemail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()

         self.gmailLogin()

         window_after = self.driver.window_handles[1]
         self.driver.switch_to.window(window_after)
         yeniSifreInput = self.waitForElelemetVisible((By.XPATH,yeniSifreXpath))
         yeniSifreInput.send_keys(firstOldPassword)
         yeniSifreTekrarInput = self.waitForElelemetVisible((By.XPATH,sifreTekrarXpath))
         yeniSifreTekrarInput.send_keys(firstOldPassword)
         gonderButon = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss))
         gonderButon.click()

         try:
          succesResetText = self.waitForElelemetVisible((By.XPATH,alertXpath))
          assert succesResetText.text == yeniSifreEskisifreAyni
        
         except AssertionError:
          pytest.fail("The expected result and the actual result are not the same")

         

      def test_minSixDigitPassword(self):
         self.driver.execute_script("window.scrollTo(0,300)")
         sleep(2)
         self.preCondition()

         epostaInput = self.waitForElelemetVisible((By.XPATH,ePostaXPath))
         epostaInput.send_keys(validemail)
         sendButton = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss)).click()

         self.gmailLogin()

         window_after = self.driver.window_handles[1]
         self.driver.switch_to.window(window_after)
         yeniSifreInput = self.waitForElelemetVisible((By.XPATH,yeniSifreXpath))
         yeniSifreInput.send_keys(fiveDigitPasswords)
         yeniSifreTekrarInput = self.waitForElelemetVisible((By.XPATH,sifreTekrarXpath))
         yeniSifreTekrarInput.send_keys(fiveDigitPasswords)
         gonderButon = self.waitForElelemetVisible((By.CSS_SELECTOR,gonderCss))
         gonderButon.click()

        
         succesResetText = self.waitForElelemetInvisible((By.XPATH,alertXpath))
         