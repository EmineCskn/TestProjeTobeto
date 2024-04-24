from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.common.exceptions import TimeoutException
import pytest
from constants.sifreConstants import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from constants.medyaHesaplarimConstants import *
from selenium.webdriver.common.action_chains import ActionChains

class Test_MedyaHesaplarim():
  def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)

  def teardown_method(self):
        self.driver.quit()
  
  def waitForElelemetVisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
  # def waitForAllElelemetVisible(self,locators,timeout=5):
  #       return WebDriverWait(self.driver,timeout).until(ec.visibility_of_all_elements_located(locators))
  def waitForElelemetInvisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))

  def test_mediaAccount(self):
    emailInput = self.waitForElelemetVisible((By.XPATH,emailInputXpath)) 
    emailInput.send_keys(validEmail)
    passwordInput =self.waitForElelemetVisible((By.XPATH,passwordInputXpath))
    passwordInput.send_keys(validPassword)
    girisButton = self.waitForElelemetVisible((By.CSS_SELECTOR,girisYapButtonCss))
    girisButton.click()
    sleep(7)
    menuButton = self.waitForElelemetVisible((By.CSS_SELECTOR, menuButtonCss))
    menuButton.click()
    profilimButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilimButtonCss))
    profilimButton.click()
    profilDuzenleButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilDuzenleCss))
    profilDuzenleButton.click()

    medyaHesaplarimButton = self.waitForElelemetVisible((By.CSS_SELECTOR, medyaHesaplarimButtonCss))
    medyaHesaplarimButton.click()

    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    linkedinButton= dropdown.find_element(By.XPATH, dropdownLinkedinXpath)
    linkedinButton.click()
    
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(linkedinUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()

    succesAccountAdded = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessage))
    assert succesAccountAdded.text == succesAccountAddedMessageText
    sleep(5)
    
    linkedinAccaunt = self.waitForElelemetVisible((By.XPATH,linkedinAccauntXpath))
    assert linkedinAccaunt.text == linkedinButton.text

    maxAccountMessage = self.waitForElelemetVisible((By.XPATH,maxAccountMessageXpath))
    assert maxAccountMessage.text == maxAccountMessageText

  def test_blankChooseBox(self):
    emailInput = self.waitForElelemetVisible((By.XPATH,emailInputXpath)) 
    emailInput.send_keys(validEmail)
    passwordInput =self.waitForElelemetVisible((By.XPATH,passwordInputXpath))
    passwordInput.send_keys(validPassword)
    girisButton = self.waitForElelemetVisible((By.CSS_SELECTOR,girisYapButtonCss))
    girisButton.click()
    sleep(7)
    menuButton = self.waitForElelemetVisible((By.CSS_SELECTOR, menuButtonCss))
    menuButton.click()
    profilimButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilimButtonCss))
    profilimButton.click()
    profilDuzenleButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilDuzenleCss))
    profilDuzenleButton.click()


    medyaHesaplarimButton = self.waitForElelemetVisible((By.CSS_SELECTOR, medyaHesaplarimButtonCss))
    medyaHesaplarimButton.click()

    
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(linkedinUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()

    blankChooseMessage = self.waitForElelemetVisible((By.CLASS_NAME,blankBoxClasName))
    assert blankChooseMessage.text == blankBoxText
  
  def test_blankUrlBox(self):
    emailInput = self.waitForElelemetVisible((By.XPATH,emailInputXpath)) 
    emailInput.send_keys(validEmail)
    passwordInput =self.waitForElelemetVisible((By.XPATH,passwordInputXpath))
    passwordInput.send_keys(validPassword)
    girisButton = self.waitForElelemetVisible((By.CSS_SELECTOR,girisYapButtonCss))
    girisButton.click()
    sleep(7)
    menuButton = self.waitForElelemetVisible((By.CSS_SELECTOR, menuButtonCss))
    menuButton.click()
    profilimButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilimButtonCss))
    profilimButton.click()
    profilDuzenleButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilDuzenleCss))
    profilDuzenleButton.click()

    medyaHesaplarimButton = self.waitForElelemetVisible((By.CSS_SELECTOR, medyaHesaplarimButtonCss))
    medyaHesaplarimButton.click()

    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    linkedinButton= dropdown.find_element(By.XPATH, dropdownLinkedinXpath)
    linkedinButton.click()
  
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()

    blankUrlMessage = self.waitForElelemetVisible((By.CLASS_NAME,blankBoxClasName))
    assert blankUrlMessage.text == blankBoxText
  
  def test_threeMediaAccount(self):
    emailInput = self.waitForElelemetVisible((By.XPATH,emailInputXpath)) 
    emailInput.send_keys(validEmail)
    passwordInput =self.waitForElelemetVisible((By.XPATH,passwordInputXpath))
    passwordInput.send_keys(validPassword)
    girisButton = self.waitForElelemetVisible((By.CSS_SELECTOR,girisYapButtonCss))
    girisButton.click()
    sleep(7)
    menuButton = self.waitForElelemetVisible((By.CSS_SELECTOR, menuButtonCss))
    menuButton.click()
    profilimButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilimButtonCss))
    profilimButton.click()
    profilDuzenleButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilDuzenleCss))
    profilDuzenleButton.click()

    medyaHesaplarimButton = self.waitForElelemetVisible((By.CSS_SELECTOR, medyaHesaplarimButtonCss))
    medyaHesaplarimButton.click()

    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    linkedinButton= dropdown.find_element(By.XPATH, dropdownLinkedinXpath)
    linkedinButton.click()
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(linkedinUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()

    succesAccountAdded = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessage))
    assert succesAccountAdded.text == succesAccountAddedMessageText
    sleep(3)
    

    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    githubButton= dropdown.find_element(By.XPATH, dropdownGithubXpath)
    githubButton.click()
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(gitHubUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()

    succesAccountAdded = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessage))
    assert succesAccountAdded.text == succesAccountAddedMessageText
    sleep(3)
    

    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    twitterButton= dropdown.find_element(By.XPATH, dropdownTwitterXpath)
    twitterButton.click()
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(twitterUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()

    succesAccountAdded = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessage))
    assert succesAccountAdded.text == succesAccountAddedMessageText
    sleep(3)
    
    linkedinAccaunt = self.waitForElelemetVisible((By.XPATH,linkedinAccauntXpath))
    assert linkedinAccaunt.text == linkedinText
    sleep(1)

    githubAccount = self.waitForElelemetVisible((By.XPATH,githubAccauntXpath))
    assert githubAccount.text == githubText
    sleep(1)

    twitterAccaunt = self.waitForElelemetVisible((By.XPATH,twitterAccauntXpath))
    assert twitterAccaunt.text == twitterText
    sleep(1)

    assert  self.waitForElelemetInvisible((By.NAME,socialMediaButtonName))
    assert  self.waitForElelemetInvisible((By.NAME,socialMediaUrlName))

  def test_deleterMediaAccount(self):
    emailInput = self.waitForElelemetVisible((By.XPATH,emailInputXpath)) 
    emailInput.send_keys(validEmail)
    passwordInput =self.waitForElelemetVisible((By.XPATH,passwordInputXpath))
    passwordInput.send_keys(validPassword)
    girisButton = self.waitForElelemetVisible((By.CSS_SELECTOR,girisYapButtonCss))
    girisButton.click()
    sleep(5)
    menuButton = self.waitForElelemetVisible((By.CSS_SELECTOR, menuButtonCss))
    menuButton.click()
    profilimButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilimButtonCss))
    profilimButton.click()
    profilDuzenleButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilDuzenleCss))
    profilDuzenleButton.click()

    medyaHesaplarimButton = self.waitForElelemetVisible((By.CSS_SELECTOR, medyaHesaplarimButtonCss))
    medyaHesaplarimButton.click()

    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    linkedinButton= dropdown.find_element(By.XPATH, dropdownLinkedinXpath)
    linkedinButton.click()
    
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(linkedinUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()
    sleep(3)

    popupClosed = self.waitForElelemetVisible((By.XPATH,popupCloseButtonXpath))
    popupClosed.click()

    deleteButton = self.waitForElelemetVisible((By.XPATH ,deleteBtnXpath))
    deleteButton.click()
    
    allertMessage1 = self.waitForElelemetVisible((By.XPATH,allertMessage1Xpath))
    assert allertMessage1.text == allertMessage1Text

    allertMessage2 = self.waitForElelemetVisible((By.XPATH,allertMessage2Xpath))
    assert allertMessage2.text == allertMessage2Text

    hayirButton = self.waitForElelemetVisible((By.CSS_SELECTOR,allertBtnHayirCss))
    evetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,allertBtnEvet))
    

    hayirButton.click()
    sleep(1)

    deleteButton.click()
    evetButton.click()

    succesAccountDelete = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessage))
    assert succesAccountDelete.text == succesAccountDeleteMessageText
    sleep(5)



    
    

  
