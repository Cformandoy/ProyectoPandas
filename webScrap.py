#Imports

import os
from shutil import rmtree
import time

#Selenium Imports - Realiza el trabajo principal de webScraping
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


#WEBSCRAP
def webScrap():

    #Variables en Duro
    #Usuario Sii
    usuario = "209182793"
    clave   = "Cp209182793"

    #Fechas
    age = "2021"

    #Creacion de variable Temp
    Temp = (os.getcwd() + '/Temp')

    #Borrado de Temp
    if os.path.exists(Temp):
        rmtree(Temp)

    options = webdriver.ChromeOptions()

    options.add_argument('headless')
    
    options.add_argument("--windows-size=1920,1080")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option('useAutomationExtension',False)
    options.add_argument('--no-sanbox')
    options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

    #Setea la ruta de descargas del navegador
    downloads_path = Temp
    params = {'behavior':'allow', 'downloadPath':downloads_path}
    driver.execute_cdp_cmd('Page.setDownloadBehavior',params)

    #Abre el navegador, maximiza ventana
    driver.get("https://zeusr.sii.cl//AUT2000/InicioAutenticacion/IngresoRutClave.html?https://misiir.sii.cl/cgi_misii/siihome.cgi")
    time.sleep(1)
    driver.maximize_window()

    #Login
    #envio de keys
    driver.find_element(By.ID, "rutcntr"    ).send_keys(usuario)
    driver.find_element(By.ID, "clave"      ).send_keys(clave)
    driver.find_element(By.ID, "bt_ingresar").click()

    #Redireccion a pagina
    time.sleep(2)
    driver.get("https://loa.sii.cl/cgi_IMT/TMBCOC_MenuConsultasContrib.cgi?dummy=1461943167534")

    #Busqueda anual
    time.sleep(1)
    driver.find_element(By.NAME, "cbanoinformeanual").send_keys(age)
    time.sleep(1)
    driver.find_element(By.ID, "cmdconsultar124").click()
    time.sleep(2)
    driver.find_element(By.NAME, "CmdXls").click()
    time.sleep(3)


    #Cierra sesion y Cierra el navegador
    driver.get("https://zeusr.sii.cl/cgi_AUT2000/autTermino.cgi")
    time.sleep(1)
    driver.close()