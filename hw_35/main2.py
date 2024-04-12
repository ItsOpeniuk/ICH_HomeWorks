import requests, re
from collections import Counter
# 2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список
# наиболее часто встречающихся слов на веб-страницах. Для каждого URL-адреса функция должна получить содержимое
# страницы с помощью запроса GET и использовать регулярные выражения для извлечения слов. Затем функция должна подсчитать
# количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.

class WordsCounter:

    pattern = re.compile(r'\b[\wА-Яа-я]+\b', re.IGNORECASE)
    def __init__(self, url_list):

        self.url_list = url_list
        self.word_list = []

    def count_words(self):
        result = {}
        for url in self.url_list:
            try:
                text = requests.get(url).content.decode('ISO-8859-1')
                words_for_url = self.pattern.findall(text)
                result[url] = Counter(words_for_url).most_common(5)
            except requests.RequestException as e:
                print(f"Error fetching data from {url}: {e}")
        return result


if __name__ == '__main__':
    url_list = ['https://www.google.ru/?client=safari&channel=mac_bm', 'https://www.youtube.com',
                'https://mail.google.com/mail/u/0/?ogbl#inbox', 'https://support.apple.com/ru-ru'
                ]
    result = WordsCounter(url_list).count_words()
    print(result)





