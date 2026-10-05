import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_exitoso():
     
 driver = webdriver.Chrome()


 try:
    driver.get ("https://www.saucedemo.com/")

    usuario = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    boton_login = driver.find_element(By.ID,"login-button")

    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
 
    boton_login.click()
    
    assert driver.title == "Swag Labs"

    productos = driver.finde.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0 

    primer_producto = productos[0]

    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert nombre_producto == "Sauce Labs Backpack"
    assert precio_producto == "$29.99"
 finally:
   driver.quit()