from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.common.exceptions import TimeoutException
import pytest
import openpyxl
from constants.chatbotConstants import *
import json
import imaplib
import email
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

class Test_ChatbotMesaj():
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def teardown_method(self):
        self.driver.quit()

 
    def test_sendingMessageChatbot(self):
        sorularinizIcinBuradayim = self.waitForElementAvailableForIFrame((By.XPATH,sorularinizIcinBuradayimXpath))
        assert sorularinizIcinBuradayim
        self.driver.switch_to.default_content()
        iframe = self.driver.find_elements(By.TAG_NAME,'iframe')[1]

        # switch to selected iframe
        self.driver.switch_to.frame(iframe)
  
        chatbotIcons = self.waitForElementAvailableForIFrame((By.XPATH,chatbotIconsXpath))
        assert chatbotIcons

    
    def waitForElelemetVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located((locator)))
       
    
    def waitForElementAvailableForIFrame(self,locator,timeout=20):
        return WebDriverWait(self.driver, timeout).until(ec.frame_to_be_available_and_switch_to_it((locator)))












# Tobeto giriş sayfasında sağ alt kosede "Sorulariniz icin buradayim" metin kutusunu ve chatbot ikonunu görüntüleyin.
# Chatbot ikonuna tiklayin Chatbot'un üst kısmında "Tobeto yardım" "Merhaba" yazilarini görüntüleyin.
# Acilan pencerenin altında mesaj gönderilebilen metin kutusuna iletmek istediğiniz mesajı yazın ve gönder butonuna tıklayın.
# Merhabalar, Tobeto'ya hoş geldiniz. Size hitap edebilmek için isminizi ögrenebilir miyim ? şeklinde otomatik mesajları görüntüleyin.
# Otamatik gönderilen Ad- Soyad metin kutusuna adınızı ve soyadınızı girin.
# Yardımcı olunmasını istediğiniz konuyu seçin
# Seçenekleri sırasıyla takip edin ve "Yardımcı olmamı istediğiniz başka bir konu var mı? " sorusunu cevaplayın.
# "Sorun olursa her zaman burdayım. 👋" mesajını görüntüleyin.