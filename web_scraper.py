import requests
from bs4 import BeautifulSoup

def save_webpage_text_to_file():
    # Запрашиваем у пользователя URL адрес сайта
    url = input("Введите URL адрес сайта: ")

    try:
        # Отправляем запрос на страницу
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный ответ

        # Создаем объект BeautifulSoup для разбора страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлекаем текст со страницы
        page_text = soup.get_text()

        # Указываем имя файла, в который сохраним текстщкы
        filename = 'webpage_text.txt'

        # Сохраняем текст в файл
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(page_text)

        print(f'Текст страницы успешно сохранён в файле {filename}')
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при попытке получить доступ к URL: {e}")

# Вызов функции для сохранения содержимого сайта
save_webpage_text_to_file()