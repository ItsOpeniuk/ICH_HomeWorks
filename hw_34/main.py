import re
class EmailFinder:

    def __init__(self, text):
        self.text = text

    def find_emails(self):
        pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+\.[a-zA-Z]{2,6}")
        return re.findall(pattern, self.text)


if __name__ == "__main__":
    text = "Contact us at info@example.com or support@example.com for assistance."
    finder = EmailFinder(text)
    print(finder.find_emails())