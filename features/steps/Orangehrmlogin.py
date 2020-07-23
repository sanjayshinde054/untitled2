import behave
from selenium import webdriver


@behave.given(u'launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\Sam\\Downloads\\chromedriver.exe")


@behave.when(u'open orangehrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@behave.when(u'Enter username "{user}" and password "{pwd}"')
def step_imp(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@behave.when(u'click on login button')
def step_impl(context):
    context.driver.find_element_by_name("Submit").click()


@behave.then(u'user must successfully login to the dashboard')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    assert text == "Dashboard"
    context.driver.close
