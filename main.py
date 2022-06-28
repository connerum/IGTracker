from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

users = []
checked = []



def main():
    handleReader()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    for i in users:
        driver.get("https://instablogs.net/live-instagram-followers-count/")
        clean = driver.find_element(By.XPATH, '//*[@id="search-username"]').clear()
        input = driver.find_element(By.XPATH, '//*[@id="search-username"]').send_keys(i)
        time.sleep(1)
        submit = driver.find_element(By.XPATH, '//*[@id="checbButton"]').click()
        time.sleep(3)
        followers = driver.find_element(By.XPATH, '//*[@id="follower-count"]').text
        checked.append(i + ': ' + followers)
        print(i + ': ' + followers)
    print(checked)
    f = open('LiveFollowCount.txt', 'w')
    for x in checked:
        f.write(x + '\n')
    print('Live Follower Count Complete!')


def handleReader():
    u = open('handles.txt', 'r')
    ulist = u.read().split('\n')
    for n in ulist:
        users.append(n)


if __name__ == '__main__':
    main()


