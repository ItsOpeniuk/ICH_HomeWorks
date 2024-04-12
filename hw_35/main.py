import requests

class Hardware:

    def __init__(self, url):

        self.url = url

    def get_status_code(self):
        r = requests.get(self.url)
        return f'Status code: {r.status_code}'

    def get_text(self):
        r = requests.get(self.url)
        return f'Responce text: {r.text}'

    def get_headers(self):
        r = requests.get(self.url)
        return f'Respoce headers {r.headers}'


if __name__ == '__main__':
    url = 'https://www.google.ru/?client=safari&channel=mac_bm'
    hardware = Hardware(url)
    print(hardware.get_status_code())
    print(hardware.get_text())
    print(hardware.get_headers())
