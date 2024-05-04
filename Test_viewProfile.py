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
  
  def test_profilimgoruntulemetesti(self):
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

    lastnamefirstname = self.waitForElelemetVisible((By.XPATH,lastnamefirstnameXpath))
    textName = self.driver.execute_script("return arguments[0].textContent", lastnamefirstname)
    assert textName == lastnamefirstnameText , "Metin beklenen değere eşit değil"
    email = self.waitForElelemetVisible((By.XPATH,emailXpath)) 
    assert email.text == emailText
    dogumTarihi = self.waitForElelemetVisible((By.XPATH, birthDateXpath)) 
    assert dogumTarihi.text == birthDateText
    telNo = self.waitForElelemetVisible((By.XPATH, phoneNumberXpath)) 
    assert telNo.text == phoneNumberText

    self.driver.execute_script("window.scrollTo(0,200)")
    aboutMeHeader = self.waitForElelemetVisible((By.XPATH, aboutMeHeaderXpath))
    assert aboutMeHeader.text == aboutMeHeaderText
    text_under_header_element = self.waitForElelemetVisible((By.XPATH, underHeaderAboutMeXpath))
    assert text_under_header_element.text == aboutMeText

    competencyHeader = self.waitForElelemetVisible((By.CSS_SELECTOR, competencyHeaderCss))
    assert competencyHeader.text == competencyHeaderText
    text_under_header_element_c = self.waitForElelemetVisible((By.XPATH, competencyCXpath))
    assert text_under_header_element_c.text == competencyCText

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
    
    foreingLanguageEnglish = self.waitForElelemetVisible((By.XPATH, foreingLanguagesNameXpath))
    foreingLanguagesDegree = self.waitForElelemetVisible((By.XPATH,foreingLanguagesDegreeXpath))
    assert foreingLanguageEnglish.text == foreingLanguagesNameText
    assert foreingLanguagesDegree.text == foreingLanguagesDegreeText
    
    
    sleep(5)
    pngIcon = self.waitForElelemetVisible((By.XPATH, pngIconXpath))
    assert pngIcon.is_displayed(), "PNG elementi görüntülenemiyor"

    
    window_before =self.driver.window_handles[0]
    # Belirli bir CSS seçicisiyle belirtilen elementin metin içeriğini kontrol edin
    mediaAccountHeader = self.waitForElelemetVisible((By.CSS_SELECTOR, mediaAccountHeaderCss))
    assert mediaAccountHeader.text == mediaAccountHeaderText, f"Medya hesap başlığı beklenen metinle uyuşmuyor: {mediaAccountHeaderText}"
    
    linkedinIcon = self.waitForElelemetVisible((By.CLASS_NAME, LinkedinIconClass))
    assert linkedinIcon.is_displayed(), "Linkedin elementi görüntülenemiyor"
    linkedinIcon.click()
    
      # Yeni sayfanın URL'sini alın
    linkedinUrl = self.driver.current_url
    
      # Bekleyin (isteğe bağlı)
    sleep(5)
    window_after = self.driver.window_handles[1]
    self.driver.switch_to.window(window_after)
      # Doğrulama: Yeni sayfanın URL'sini kontrol edin
    assert linkedinUrl == expectedLinkedinUrl, f"Link tıklandıktan sonra beklenen URL {expectedLinkedinUrl} değil, gerçek URL {linkedinUrl}"
    sleep(5)
    self.driver.close()
    self.driver.switch_to.window(window_before)
  
    
    # profilimButton = self.waitForElelemetVisible((By.CSS_SELECTOR,profileButtonCss))
    # profilimButton.click()
    sleep(2)
    successModalAssesementTest = self.waitForAllElelemetVisible((By.XPATH,assesmentTestXpath))
    assesmentTest=[]
    for i in successModalAssesementTest:
      assesmentTest.append(i.text)
    assesmentTestClean = [i.replace("\n", " ") for i in assesmentTest]
    
    assert analysisReportItem1 in assesmentTestClean

    analysisReportIcon = self.waitForElelemetVisible((By.XPATH, seeIconAnalysisReportXpath))
    self.driver.execute_script("arguments[0].click();", analysisReportIcon)

    assert self.waitForElelemetVisible((By.CLASS_NAME,analysisReportTextClassName)).is_displayed()

    sleep(2)
    profilimButton2 = self.waitForElelemetVisible((By.CSS_SELECTOR,profileButton2Css))
    self.driver.execute_script("arguments[0].click();", profilimButton2)
    sleep(2)
    

    levelTestList = self.waitForAllElelemetVisible((By.XPATH,levelTestsXpath))
    testList=[]
    for i in levelTestList:
      testList.append(i.text)
    
    testListClean1 = [i.replace("\n", ", ") for i in testList]

    assert levelTestItem1 in testListClean1
    assert len(testList)== 2

    
    






      # Tobeto Iste Basari Modelim kismi altinda kullanicinin cozdugu "iste basari modeli" degerlendirme testi sonuclarinin gorundugunu dogrulayin.
      # Tobeto Iste Basari Modeli Analiz Raporunun goruntulemek icin goz butonuna tiklayin.
      # Tobeto Seviye Testlerim kismi altinda daha önce çozulen seviye testlerinin goruntulendigini dogrulayin
      # Yetkinlik Rozetlerim kismi altinda kullanicinin kazandigi rozetlerin sergilendigini dogrulayin.
      # Aktivite Haritam kisminda kullanicinin aktivitelerinin bir takvim seklinde tutuldugunu ve her gune ait aktivitelerin gorundugunu dogrulayin.
      # Aktivite haritasi altinda bir renk cetveli oldugunu dogrulayin.
      # Egitim Hayatim ve Deneyimlerim kisminda kullanicinin aldigi egitimlerin ve edindigi deneyimlerin bilgisinin tutuldugu bir zaman cizelgesi oldugunu dogrulayin.
    
    
  
