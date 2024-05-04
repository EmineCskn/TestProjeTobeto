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
from constants.foreingLanguageConstatn import *
from selenium.webdriver.common.action_chains import ActionChains

class Test_Yabancidillerim():
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

  def test_foreingLanguagesAdded(self):
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
    foreingLanguangeButton = self.waitForElelemetVisible((By.CSS_SELECTOR, yabanciDillerimButtonCss))
    foreingLanguangeButton.click()

    languageButton = self.waitForElelemetVisible((By.NAME,languageButtonName))
    languageButton.click()
    dropdown = self.driver.find_element(By.XPATH,dropdownLanguageXpath)
    sleep(5)
    EnglishButton= dropdown.find_element(By.XPATH,dropdownEnglishXpath)
    EnglishButton.click()

    proficiencyButton = self.waitForElelemetVisible((By.NAME,proficiencyButtonName))
    proficiencyButton.click()
    dropdown = self.driver.find_element(By.NAME,proficiencyButtonName)
    levelButton= dropdown.find_element(By.XPATH,languageLevelXpath )
    levelButton.click()
    saveButton = self.waitForElelemetVisible((By.CSS_SELECTOR,saveButtonCss))
    saveButton.click()

    succesLanguageAdded = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessageCss))
    assert succesLanguageAdded.text == saveSuccesText
    sleep(5)

  def test_blankLanguageChooseBox(self):
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
    foreingLanguangeButton = self.waitForElelemetVisible((By.CSS_SELECTOR, yabanciDillerimButtonCss))
    foreingLanguangeButton.click()


    proficiencyButton = self.waitForElelemetVisible((By.NAME,proficiencyButtonName))
    proficiencyButton.click()
    dropdown = self.driver.find_element(By.NAME,proficiencyButtonName)
    levelButton= dropdown.find_element(By.XPATH,languageLevelXpath )
    levelButton.click()
    saveButton = self.waitForElelemetVisible((By.CSS_SELECTOR,saveButtonCss))
    saveButton.click()

    blankLanguageChoose = self.waitForElelemetVisible((By.XPATH,blankLanguageChooseXpath))
    assert blankLanguageChoose.text == blankLanguageChooseText
    sleep(5)

  def test_blankProficiencyBox(self):
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
    foreingLanguangeButton = self.waitForElelemetVisible((By.CSS_SELECTOR, yabanciDillerimButtonCss))
    foreingLanguangeButton.click()

    languageButton = self.waitForElelemetVisible((By.NAME,languageButtonName))
    languageButton.click()
    dropdown = self.driver.find_element(By.XPATH,dropdownLanguageXpath)
    sleep(5)
    EnglishButton= dropdown.find_element(By.XPATH,dropdownEnglishXpath)
    EnglishButton.click()

    saveButton = self.waitForElelemetVisible((By.CSS_SELECTOR,saveButtonCss))
    saveButton.click()

    blankProficiencyBox = self.waitForElelemetVisible((By.XPATH,blankProficiencyXpath))
    assert blankProficiencyBox.text == blankProficiencyText
    sleep(5)

  def test_deleteForeingLanguages(self):
    Test_Yabancidillerim.test_foreingLanguagesAdded(self)
    deleteMauseHower = self.waitForElelemetVisible((By.XPATH,succesAddedEnglishXpath))
    actions = ActionChains(self.driver)
    actions.move_to_element(deleteMauseHower).perform()
    sleep(5)

    deleteButton = self.waitForElelemetVisible((By.CSS_SELECTOR,deleteEnglishLanguageCss))
    deleteButton.click()
    alert = Alert(self.driver)
    hayirButton = self.waitForElelemetVisible((By.CSS_SELECTOR,allertBtnHayirCss))
    hayirButton.click()
    sleep(5)

    actions = ActionChains(self.driver)
    actions.move_to_element(deleteMauseHower).perform()
    sleep(5)

    deleteButton = self.waitForElelemetVisible((By.CSS_SELECTOR,deleteEnglishLanguageCss))
    deleteButton.click()
    alert = Alert(self.driver)
    evetButton = self.waitForElelemetVisible((By.CSS_SELECTOR,allertBtnEvet))
    evetButton.click()

    succesLanguageDeleted = self.waitForElelemetVisible((By.CSS_SELECTOR,popupMessageCss))
    assert succesLanguageDeleted.text == popupDeleteMessageText
    sleep(5)
    
