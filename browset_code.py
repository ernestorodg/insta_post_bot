from time import sleep
from re import sub
from selenium import webdriver



# # If Selenium can't find, we ask for waiting 5 seconds and repeat
# browser.implicitly_wait(5)

# browser.get('https://www.instagram.com/')


# # Login link obtained with Xpath. May need to be updated.
# login_link = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
# login_link.click()
# sleep(2)

# # Also, CSS Path may need to be updated
# username_input = browser.find_element_by_css_selector(
# 	'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
# password_input = browser.find_element_by_css_selector(
# 	'div.-MzZI:nth-child(3) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')

# username_input.send_keys(user)
# password_input.send_keys(password)


# login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
# login_button.click()



# sleep(5)


# browser.close()

###############################

from time import sleep
from selenium import webdriver

def get_login():
	login_file = open('user.txt','r') 
	login = login_file.readline().split(':')
	user = login[0]
	password = login[1][0:-1]
	login_file.close()
	return (user, password)

user, password = get_login()


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector('div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        password_input = self.browser.find_element_by_css_selector('div.-MzZI:nth-child(3) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").click()
        sleep(2)
        return LoginPage(self.browser)



browser = webdriver.Firefox()
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login(user, password)

def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login("<your username>", "<your password>")

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0

not_now_button = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
sleep(5)
not_now_button = browser.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()
sleep(5)

browser.close()




