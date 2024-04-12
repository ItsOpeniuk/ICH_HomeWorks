import re
class HighlightText:

    def __init__(self, text, words):
        self.text = text
        self.words = words

    def highlight_keywords(self):
        flags = re.IGNORECASE
        for word in self.words:
            pattern = re.compile(fr'\b{word}\b', flags=flags)
            finded_words = pattern.findall(self.text)
            for word in set(finded_words):
                self.text = self.text.replace(word, f'*{word}*')
        return self.text


if __name__ == '__main__':
    text = "This is a sample text. We need to highlight Python and programming. Python, Programming"
    keywords = ["python", "programming"]
    highlight_text = HighlightText(text, keywords)
    print(highlight_text.highlight_keywords())



