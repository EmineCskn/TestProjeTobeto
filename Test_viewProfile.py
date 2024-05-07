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
from constants.profileConstants import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class Test_ProfilimGoruntuleme():
  def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)

  def teardown_method(self):
        self.driver.quit()

  def waitForElelemetVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

  def waitForElelemetInvisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))
  def waitForAllElelemetVisible(self,locators,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_all_elements_located(locators))
  
  def webelementListString(self,locator,timeout=5):
        elements =WebDriverWait(self.driver,timeout).until(ec.visibility_of_all_elements_located(locator))
        list=[]
        for i in elements:
         list.append(i.text)
        return list

  def preCondition(self):
      emailInput = self.waitForElelemetVisible((By.XPATH,emailInputXpath)) 
      emailInput.send_keys(validEmail)
      passwordInput =self.waitForElelemetVisible((By.XPATH,passwordInputXpath))
      passwordInput.send_keys(validPassword)
      girisButton = self.waitForElelemetVisible((By.CSS_SELECTOR,loginButtonCss))
      girisButton.click()
      sleep(5)
      profilimButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profileButtonCss))
      profilimButton.click()
      sleep(1)

  
  def test_profilimgoruntulemetesti(self):
    self.preCondition()
    lastnamefirstname = self.waitForElelemetVisible((By.XPATH,lastnamefirstnameXpath))
    textName = self.driver.execute_script("return arguments[0].textContent", lastnamefirstname)
    assert textName == lastnamefirstnameText , "Metin beklenen değere eşit değil"
    assert self.waitForElelemetVisible((By.XPATH,emailXpath)).text == emailText
    assert self.waitForElelemetVisible((By.XPATH, birthDateXpath)).text == birthDateText
    assert self.waitForElelemetVisible((By.XPATH, phoneNumberXpath)).text == phoneNumberText

    self.driver.execute_script("window.scrollTo(0,200)")
    assert self.waitForElelemetVisible((By.XPATH, aboutMeHeaderXpath)).text == aboutMeHeaderText
    assert self.waitForElelemetVisible((By.XPATH, underHeaderAboutMeXpath)).text == aboutMeText
    

    assert self.waitForElelemetVisible((By.CSS_SELECTOR, competencyHeaderCss)).text == competencyHeaderText
    assert self.waitForElelemetVisible((By.XPATH, competencyCXpath)).text == competencyCText

    seeIconCompetency = self.waitForElelemetVisible((By.XPATH, seeIconCompetencyXpath))
    seeIconCompetency.click()
    assert self.waitForElelemetVisible((By.XPATH,allCompetencyHeaderXpath)).text == allCompetencyHeaderText
    btnCloase = self.waitForElelemetVisible((By.CSS_SELECTOR, btnClaoseAllCompetencyCss))
    btnCloase.click()
    
    self.driver.execute_script("window.scrollTo(200,400)")
    assert self.waitForElelemetVisible((By.CSS_SELECTOR, foreingLanguagesHeaderCss)).text == foreingLanguagesHeaderText
    assert self.waitForElelemetVisible((By.XPATH, foreingLanguagesNameXpath)).text == foreingLanguagesNameText
    assert self.waitForElelemetVisible((By.XPATH,foreingLanguagesDegreeXpath)).text == foreingLanguagesDegreeText
    

    self.driver.execute_script("window.scrollTo(400,800)")
    assert self.waitForElelemetVisible((By.CSS_SELECTOR, certificateHeaderCss)).text == certificateHeaderText
    
    assert self.waitForElelemetVisible((By.XPATH, foreingLanguagesNameXpath)).text == foreingLanguagesNameText
    assert  self.waitForElelemetVisible((By.XPATH,foreingLanguagesDegreeXpath)).text == foreingLanguagesDegreeText
    

    sleep(5)
    pngIcon = self.waitForElelemetVisible((By.XPATH, pngIconXpath))
    assert pngIcon.is_displayed(), "PNG elementi görüntülenemiyor"

    
    window_before =self.driver.window_handles[0]
    mediaAccountHeader = self.waitForElelemetVisible((By.CSS_SELECTOR, mediaAccountHeaderCss))
    assert mediaAccountHeader.text == mediaAccountHeaderText, f"Medya hesap başlığı beklenen metinle uyuşmuyor: {mediaAccountHeaderText}"
    
    linkedinIcon = self.waitForElelemetVisible((By.CLASS_NAME, LinkedinIconClass))
    assert linkedinIcon.is_displayed(), "Linkedin elementi görüntülenemiyor"
    linkedinIcon.click()
    
    linkedinUrl = self.driver.current_url
    
    sleep(5)
    window_after = self.driver.window_handles[1]
    self.driver.switch_to.window(window_after)
    assert linkedinUrl == expectedLinkedinUrl, f"Link tıklandıktan sonra beklenen URL {expectedLinkedinUrl} değil, gerçek URL {linkedinUrl}"
    sleep(5)
    self.driver.close()
    self.driver.switch_to.window(window_before)
  
    
    sleep(2)
    successModalAssesementTest = self.webelementListString((By.XPATH,assesmentTestXpath))
    assesmentTestClean = [i.replace("\n", " ") for i in successModalAssesementTest]
    
    assert analysisReportItem1 in assesmentTestClean

    analysisReportIcon = self.waitForElelemetVisible((By.XPATH, seeIconAnalysisReportXpath))
    self.driver.execute_script("arguments[0].click();", analysisReportIcon)

    assert self.waitForElelemetVisible((By.CLASS_NAME,analysisReportTextClassName)).is_displayed()

    sleep(2)
    profilimButton2 = self.waitForElelemetVisible((By.CSS_SELECTOR,profileButton2Css))
    self.driver.execute_script("arguments[0].click();", profilimButton2)
    sleep(2)
    
    

    levelTestList = self.webelementListString((By.XPATH,levelTestsXpath))
    testListClean1 = [i.replace("\n", ", ") for i in levelTestList]
    assert levelTestItem1 in testListClean1
    
    badges = self.waitForAllElelemetVisible((By.CLASS_NAME,badgesimgClassName))
    
    for i in badges:
      assert i.tag_name == tagnameImg,  "Belirtilen öğe bir resim değil"
      assert i.is_displayed()


    weeks = self.waitForAllElelemetVisible((By.CLASS_NAME, weeksClassName))
    assert len(weeks) == 53
    all_weeks = self.waitForAllElelemetVisible((By.TAG_NAME, allWeeksTagname))
    days = []
    for i in all_weeks:
      days.append(i.get_attribute("data-tip"))
    assert oldAktivity in days

    # Renk cetvelini temsil eden elementi tanımlayın (örneğin, bir <div> elementi olabilir)
    colorPalette =self.driver.find_element(By.CLASS_NAME,colorPaleteClassName )  # Örnek CSS sınıfı
    
    # Renk cetvelinin içindeki renk örneklerini bulun
    colorSamples = colorPalette.find_elements(By.TAG_NAME,colorSamplesClassName)
    
    # Beklenen renk örneği sayısı
    expected_sample_count = 5  # Örnek olarak, beş renk örneği var
    
    # Her bir renk örneği için doğrulama yapın
    for colorSample in colorSamples:
        # Her bir renk örneğinin belirli bir sınıfa sahip olduğunu kontrol edin
        if not colorSample.get_attribute("class").startswith("hm"):
            raise NoSuchElementException("Renk örneği beklenen sınıflara sahip değil.")
    
    # Renk örneği sayısını doğrula
    assert len(colorSamples) == expected_sample_count
    
    
    
  
