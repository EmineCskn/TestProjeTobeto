from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.common.exceptions import TimeoutException
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from constants.mediaAccountConstants import *
from selenium.webdriver.common.action_chains import ActionChains



class Test_MedyaHesaplarim():
  def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)

  def teardown_method(self):
        self.driver.quit()
  
  def waitForElelemetVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
  def waitForElelemetInvisible(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))
  
  def preCondition(self):
    emailInput = self.waitForElelemetVisible((By.XPATH,emailInputXpath)) 
    emailInput.send_keys(validEmail)
    passwordInput =self.waitForElelemetVisible((By.XPATH,passwordInputXpath))
    passwordInput.send_keys(validPassword)
    girisButton = self.waitForElelemetVisible((By.CSS_SELECTOR,girisYapButtonCss))
    girisButton.click()
    sleep(7)
    
    profilimButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilimButtonCss))
    profilimButton.click()
    profilDuzenleButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profilDuzenleCss))
    profilDuzenleButton.click()

    medyaHesaplarimButton = self.waitForElelemetVisible((By.CSS_SELECTOR, medyaHesaplarimButtonCss))
    medyaHesaplarimButton.click()

  def deleteBtn(self):
    deleteMauseHower = self.waitForElelemetVisible((By.XPATH,succesAddedLinkedinXpath))
    actions = ActionChains(self.driver)
    actions.move_to_element(deleteMauseHower).perform()
    sleep(3)

    deleteButton = self.waitForElelemetVisible((By.CSS_SELECTOR ,deleteBtnCss))
    deleteButton.click()

    evetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,allertBtnEvet))
    evetButton.click() 

      

  def test_mediaAddedAccount(self):
    self.preCondition()

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
    
    LinkedinAttribute= self.waitForElelemetVisible((By.CSS_SELECTOR,linkedinAddedUrlCss)).get_attribute(attribute)
    assert linkedinUrlLink in LinkedinAttribute

    maxAccountMessage = self.waitForElelemetVisible((By.XPATH,maxAccountMessageXpath))
    assert maxAccountMessage.text == maxAccountMessageText
    sleep(5)

    self.deleteBtn()

  def test_blankChooseBox(self):
    self.preCondition()
    
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(linkedinUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()

    blankChooseMessage = self.waitForElelemetVisible((By.CLASS_NAME,blankBoxClasName))
    assert blankChooseMessage.text == blankBoxText
  
  def test_blankUrlBox(self):
    self.preCondition()
    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    linkedinButton= dropdown.find_element(By.XPATH, dropdownLinkedinXpath)
    linkedinButton.click()
  
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()

    blankUrlMessage = self.waitForElelemetVisible((By.CLASS_NAME,blankBoxClasName))
    assert blankUrlMessage.text == blankBoxText

  def test_deleteMediaAccount(self):
    self.preCondition()

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
    sleep(2)


    deleteMauseHower = self.waitForElelemetVisible((By.XPATH,succesAddedLinkedinXpath))
    actions = ActionChains(self.driver)
    actions.move_to_element(deleteMauseHower).perform()
    sleep(3)

    deleteButton = self.waitForElelemetVisible((By.CSS_SELECTOR ,deleteBtnCss))
    deleteButton.click()
    
    allertMessage1 = self.waitForElelemetVisible((By.XPATH,allertMessage1Xpath))
    assert allertMessage1.text == allertMessage1Text

    allertMessage2 = self.waitForElelemetVisible((By.XPATH,allertMessage2Xpath))
    assert allertMessage2.text == allertMessage2Text

    hayirButton = self.waitForElelemetVisible((By.CSS_SELECTOR,allertBtnHayirCss))
    hayirButton.click()
    sleep(1)
    
    actions = ActionChains(self.driver)
    actions.move_to_element(deleteMauseHower).perform()
    sleep(3)


    deleteButton.click()
    evetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,allertBtnEvet))
    evetButton.click()

    succesAccountDelete = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessage))
    assert succesAccountDelete.text == succesAccountDeleteMessageText
  
  def test_threeMediaAccount(self):
    self.preCondition()

    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    linkedinButton= dropdown.find_element(By.XPATH, dropdownLinkedinXpath)
    linkedinButton.click()
    
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(linkedinUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()

    
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
    sleep(5)
    

    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    twitterButton= dropdown.find_element(By.XPATH, dropdownTwitterXpath)
    twitterButton.click()
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(twitterUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()
    
    sleep(2)
    succesAccountAdded = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessage))
    assert succesAccountAdded.text == succesAccountAddedMessageText
    sleep(3)
    
    githubAttribute= self.waitForElelemetVisible((By.CSS_SELECTOR,githubAddedUrlCss)).get_attribute(attribute)
    assert gitHubUrlLink in githubAttribute

    twitterAttribute = self.waitForElelemetVisible((By.CSS_SELECTOR,twitterAddedUrlCss)).get_attribute(attribute)
    assert twitterUrlLink in twitterAttribute
    sleep(1)

    assert  self.waitForElelemetInvisible((By.NAME,socialMediaButtonName))
    assert  self.waitForElelemetInvisible((By.NAME,socialMediaUrlName))

    self.deleteBtn()
    
    sleep(2)
    self.deleteBtn()
    sleep(2)
    self.deleteBtn()
    
  def test_updateMediaAccount(self):
    self.preCondition()

    socialMediaButton = self.waitForElelemetVisible((By.NAME,socialMediaButtonName))
    socialMediaButton.click()
    dropdown = self.driver.find_element(By.NAME,dropdownButtonName)
    linkedinButton= dropdown.find_element(By.XPATH, dropdownLinkedinXpath)
    linkedinButton.click()
    
    socialMedyaUrlInput = self.waitForElelemetVisible((By.NAME, socialMediaUrlName))
    socialMedyaUrlInput.send_keys(linkedinUrlLink)
    kaydetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,kaydetButtonCss))
    kaydetButton.click()
    
    sleep(5)

    editButton = self.waitForElelemetVisible((By.CSS_SELECTOR ,editBtnCss))
    editButton.click()
    sleep(2)

    deactiveUpdateButton = self.waitForElelemetVisible((By.XPATH, updateButtonXpath))
    assert  deactiveUpdateButton.is_displayed()
    
    updateHeader = self.waitForElelemetVisible((By.CSS_SELECTOR,updateHeaderCss))
    assert updateHeader.text == updateHeaderText

    newdropdown = self.driver.find_element(By.XPATH,newDropDownButtonXpath)
    githubButton= newdropdown.find_element(By.XPATH, newDropDownGithubXpath)
    githubButton.click()
    socialMedyaUrlInput = self.waitForElelemetVisible((By.XPATH, newSocialMediaUrlXpat))
    socialMedyaUrlInput.clear()
    socialMedyaUrlInput.send_keys(gitHubUrlLink)
    updateButton = self.waitForElelemetVisible((By.XPATH, updateButtonActiveXpath))
    updateButton.click()

    succesUpdateAccount = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessage))
    try:
        assert succesUpdateAccount.text == succesUpdateAccauntPopupText
    except AssertionError as e:
        pytest.fail("Soft assert failed: {}".format(e))
    
    
  



    
    

  
