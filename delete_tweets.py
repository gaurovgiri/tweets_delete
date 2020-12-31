from selenium.webdriver import Firefox
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as element_404
import getpass

driver = Firefox()
 
class twitter:  
    def __init__(self,user,passwd):
        self.open = driver.get('https://twitter.com/login')
        self.user = user
        self.passwd = passwd
        user_name = driver.find_element_by_css_selector("div.css-1dbjc4n:nth-child(6) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        pass_word = driver.find_element_by_css_selector("div.css-1dbjc4n:nth-child(7) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
        user_name.send_keys(self.user)
        pass_word.send_keys(self.passwd)
        login = driver.find_element_by_css_selector('div.r-a023e6:nth-child(1)')
        login.click()

    def profile(self):
        driver.get('https://twitter.com/'+self.user)


    def tweets(self):
        self.body = driver.find_element_by_css_selector('body')
        for i in range(10):
            self.body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)
        self.body.send_keys(Keys.HOME)
        self.all_tweets = driver.find_elements_by_css_selector('.r-1ljd8xs > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div > div > article')
        print(self.all_tweets)

    def delete(self):
        tweets = 0
        try:
            while True:
                time.sleep(3)
                for j in range(3):
                    self.all_tweets = driver.find_element_by_css_selector('div.r-18bvks7:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child({0}) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > time:nth-child(1)'.format(j+1))
                    self.all_tweets.click()
                    bar = driver.find_element_by_css_selector('.r-k4xj1c > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(2)')
                    bar.click()
                    delete_button = driver.find_element_by_css_selector('div.r-9qu9m4:nth-child(1)')
                    delete_button.click()
                    confirm = driver.find_element_by_css_selector('.r-1dgebii > div:nth-child(1)')
                    confirm.click()
                    tweets += 1
                    print("a tweet was deleted!")
                driver.refresh()
        except element_404:
            print('No more tweets left to delete')
            print(tweets," tweets deleted!")




            # try:
            #     self.all_tweets = driver.find_element_by_css_selector('div.r-18bvks7:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3) > time:nth-child(1)')
            #     self.all_tweets.click()
            #     bar = driver.find_element_by_css_selector('.r-k4xj1c > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(2)')
            #     bar.click()
            #     delete_button = driver.find_element_by_css_selector('div.r-9qu9m4:nth-child(1)')
            #     delete_button.click()
            #     confirm = driver.find_element_by_css_selector('.r-1dgebii > div:nth-child(1)')
            #     confirm.click()
            #     print(tweets," tweets deleted!")
            #     time.sleep(5)
            # except element_404:
            #     count += 1
            #     self.body.send_keys(Keys.PAGE_DOWN)
            #     print(count-1," tweets skipped")
            #     continue



username = input('Username: ')

try:
    password = getpass.getpass(prompt='Password: ',stream=None)
except Exception as error:
    print("Error", error)

twitter = twitter(username,password)
twitter.profile()
# twitter.tweets()
twitter.delete()
