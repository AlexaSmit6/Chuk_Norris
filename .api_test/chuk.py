import requests

class Test_new_joke():
    """Создание новой шутки"""""
    def __init__(self):
        pass
    def create_new_random_joke(self):
        url = 'https://api.chucknorris.io/jokes/random'
        print(url)
        result = requests.get(url)
        print("Статус код :" + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Успешно!!! Мы получили новую шутку')
        else:
            print('Провален!!')
        print(result.text)
        check = result.json()
        # check_info = check.get("categories")
        # print(check_info)
        # assert check_info == []
        # print("Категория верна")
        check_value = check.get("value")
        print(check_value)
        name = "Chuck"
        if name in check_value:
            print("Чак присутствует")
        else:
            print("Шутка не про Чака")




random_joke = Test_new_joke()
random_joke.create_new_random_joke()
