import behave
from selenium import webdriver


@behave.given(u'launch the chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\Sam\\Downloads\\chromedriver.exe")


@behave.when(u'open the orangehrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@behave.then(u'verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]").is_displayed()
    assert status is True


@behave.then(u'close browser')
def close_browser(context):
    context.driver.close()
