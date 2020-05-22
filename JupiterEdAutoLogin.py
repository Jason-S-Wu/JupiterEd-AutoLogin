import time
from selenium import webdriver


#login
name = input("Name or ID: ")
type(name)
password = input("Password: ")
type(password)
school = input("School: ")
type(school)
city = input("City: ")
type(city)
state = input("State: ")
type(state)

#constant
#name = 'Name or ID'
#password = 'password'
#school = 'School'
#city = 'city'
#state  = 'xx_xx'

#login
driver = webdriver.Chrome(executable_path=r"./driver/chromedriver.exe")
driver.get("https://login.jupitered.com/login/")
driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[3]/div[2]/div/div[2]").send_keys(name)
driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[3]/div[3]/div[2]/input").send_keys(password)
driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[3]/div[8]/div[1]/div[2]").send_keys(school)
driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[3]/div[8]/div[2]/div[1]/div[2]").send_keys(city)
time.sleep(1)
driver.execute_script(f"document.getElementsByName('region1')[0].value = '{state}'")
time.sleep(1)
driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[4]/div[3]/div").click()

#main loop
def loop():
    while True:
        time.sleep(60)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div[2]").click()
        time.sleep(60)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div[3]").click()
        time.sleep(60)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div[4]").click()
        time.sleep(60)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div[2]").click()
        time.sleep(60)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div[3]").click()
        time.sleep(60)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div[4]").click()
        time.sleep(60)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div[13]").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[3]/div[2]/div/div[2]").send_keys(name)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[3]/div[3]/div[2]/input").send_keys(password)
        driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[4]/div[3]/div").click()
    return
loop()