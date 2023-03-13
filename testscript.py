from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
import time
s = Service("C:\\Users\\Smile\\PycharmProjects\\python\\TestChrome\\Chrome\\chromedriver.exe")

url = "https://www.youtube.com"
# driver = webdriver.Chrome(executable_path="C:\\Users\\Smile\\PycharmProjects\\python\\TestChrome\\Chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

xpath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox'
xpath2 = '/html/body/div[1]/div[2]/form/div[1]/input'
# driver.find_element(xpath).click()
try:
    driver.get(url=url)
    time.sleep(1)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(xpath).send_keys('Изучение Python')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-renderer[1]/ytd-playlist-thumbnail/a/div[1]/ytd-playlist-video-thumbnail-renderer/yt-image/img').click()
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
     driver.close()
     driver.quit()

# your_age = int(input("Введите ваш возраст: "))
#
# if your_age < 18:
#     print("Вы еще маленький")
# elif 18 < your_age < 40:
#     print("Вам позволено")
# elif 40 < your_age < 60:
#     print("Вам не интересен этот контент")
# else:
#     print("Что ты такое")

# a = 10
# n = 0
# while a < 200:
#     print(n, '==', a)
#
#     a += 1
#     n += 1

# Создать переменные (Вывести сделать конкетинацию,вывести в нижнем регистре,вывести в верхнем регистре)
#
# first_name = "pavel"
# Last_name = "kravhcenko"
# full_name = (first_name +" "+ Last_name)
# age = 36

# print(full_name.lower())
# print(full_name.upper())
# print(full_name)
# print(first_name.title() +" "+ str(age) +" "+ Last_name.title())

# Создать 3 списка cars, mas, name = ( вывести 3 имя отдельно) Создать переменную massage
# ( сделать предложение из разных списков)
# names = ['pavel', 'nikita', 'oleg', 'andrei']
# cars = ['BMW', 'Mersedes', 'Audi', 'Golf', 'Mazda']
# mas = ['i like drive my car, and i have', 'My car is WV-', 'I hate this car']
# massage = "My best fried " + " " + names[0].title() + " " + "and he told" + " " + mas[-1] + cars[4]
# print(names[0])
# print(names[-2])
# print(names[1])
# print(massage)

# names.append('viktor')
# pop_name = names.pop(-2)

# del names[0]
# print(names)
# names[-1] = 'Kostik'
# print(names)
# names.sort()
# print(names)
# go_away = 'andrei'
# print (pop_name.title())
# print('This client ' + " "+go_away.title() + " " + "I hate him" )

#
# for car in cars:
#     print(car)
# for name in names:
#     print(name)

