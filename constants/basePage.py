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


class basePage():
     def __init__(self,driver):
         self.driver=driver

     def waitForElelemetVisible(self,locator,timeout=15):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

     def waitForElelemetInvisible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(ec.invisibility_of_element_located(locator))
     def waitForAllElelemetVisible(self,locators,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.visibility_of_all_elements_located(locators))
     
     def elementClikable(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(ec.element_to_be_clickable(locator))
     
     def webelementListString(self,locator):
        elements = self.driver.find_elements(*locator)
        list=[]
        for i in elements:
         list.append(i.text)
        return list
         
     