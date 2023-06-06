import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Counter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(r'C:\Chrome\chromedriver.exe')
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    driver.implicitly_wait(2)
    pytest.driver.find_element(By.ID, "email").send_keys('yaname.test@gmail.com')
    pytest.driver.find_element(By.ID, "pass").send_keys('test2022')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(pytest.driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME,'h1')))
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    pytest.driver.find_element(By.CLASS_NAME, "nav-link").click()

    #time.sleep(5)

    print(".")

    inf = pytest.driver.find_elements(By.CSS_SELECTOR, 'body > div.task2.fill > div > div.\.col-sm-4.left')
    for i in range(len(inf)):
        parts = inf[i].text.split(", ")
        s = parts[0]
        length = len(s)
        integers = []
        i = 0
        while i < length:
            s_int = ''
            while i < length and '0' <= s[i] <= '9':
                s_int += s[i]
                i += 1
            i += 1
            if s_int != '':
                integers.append(int(s_int))
        del integers[0]
        quantity = max(integers)
        print('Количество моих питомцев из статистики сайта', quantity)

    line = pytest.driver.find_elements(By.CSS_SELECTOR, 'td.smart_cell')
    print('Всего моих питомцев (строк с питомцами): ', len(line))
    # Присутствуют все питомцы.
    if quantity == len(line):
        print('!Присутсвуют все питомцы')
    else:
        print('!Одного или нескольких питомцев не хватает')

    images = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > th > img')
    counter = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            counter += 1
    print('Количество питомцев с фотографией: ', counter)
    # Хотя бы у половины питомцев есть фото.
    if quantity / 2 <= counter:
        print('!У', counter, 'питомцев из', quantity, 'есть фото')
    else:
        print('!Фото есть менее чем у половины питомцев')

    names = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr')
    count = 0
    for i in range(len(names)):
        if names[i].text != '':
            count += 1
    print('Количество питомцев с именем: ', count)

    type = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(3)')
    count = 0
    for i in range(len(type)):
        if type[i].text != '':
            count += 1
    print('Количество питомцев с указанием породы: ', count)

    age = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-child(4)')
    coun = 0
    for i in range(len(age)):
        if age[i].text != '':
            coun += 1
    print('Количество питомцев с указанием возраста: ', coun)

#У всех питомцев есть имя, возраст и порода.
    if quantity == counter == coun == count:
        print('!У каждого питомца указано имя, возраст и порода')
    else:
        print('!Из', quantity, 'питомцев: у', counter, 'указано имя, у', coun, 'указан возраст, и у', count,
              'указан тип')
#У всех питомцев разные имена.
    pet_name = []
    for i in range(len(names)):
        p = names[i].text.split(' ')
        pet_name.append(p[0])
    for i in range(len(pet_name) - 1):
        for j in range(i + 1, len(pet_name)):
            if pet_name[i] == pet_name[j]:
                word_list = []
                for word in pet_name:
                    clear_word = ""
                    for letter in word:
                        if letter.isalpha():
                            clear_word += letter.lower()

                    word_list.append(clear_word)
                print('проверка имён на уникальность:',Counter(word_list))
#проверка питомцев на уникальность
    animal_data = []
    for i in range(len(names)):
        animal_data.append(names[i].text.split(' '))
    for i in range(len(animal_data) - 1):
        for j in range(i + 1, len(animal_data)):
            if animal_data[i] == animal_data[j]:
                ani_list = []
                for word in animal_data:
                    clear_word = ""
                    for letter in word:
                        if letter.isalpha():
                            clear_word += letter.lower()

                    ani_list.append(clear_word)
                print('проверка питомцев на уникальность:', Counter(ani_list))



