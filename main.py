import time

from selenium import webdriver

SITE = "https://planoplan.com/"


def get_driver():
    driver = webdriver.Chrome()
    driver.get(SITE)
    return driver


def elem_click(menu_elem):
    menu_elem.click()
    time.sleep(2)


def btn_click(btn_name):
    driver = get_driver()
    menu_elem = driver.find_element_by_link_text(btn_name)
    elem_click(menu_elem)
    driver.quit()


def catalog_click():
    btn_click("Каталог")


def gallery_click():
    driver = get_driver()
    menu_elem = driver.find_element_by_xpath("//*[@id=\"header\"]/div/div/div[1]/a[3]")
    elem_click(menu_elem)
    driver.quit()


def header_click():
    driver = get_driver()
    menu_elem = driver.find_element_by_class_name("newpp_header__menu-item")
    elem_click(menu_elem)
    driver.quit()


if __name__ == "__main__":
    header_click()
    catalog_click()
    gallery_click()
