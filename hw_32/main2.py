from datetime import datetime
class Email:

    def __init__(self, sender, receiver, subject, message, send_date):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.message = message
        self.send_date = send_date


    def __eq__(self, other):
        return datetime.strptime(self.send_date, "%Y-%m-%d") == datetime.strptime(other.send_date,  "%Y-%m-%d")

    def __lt__(self, other):
        return datetime.strptime(self.send_date, "%Y-%m-%d") < datetime.strptime(other.send_date,  "%Y-%m-%d")

    def __str__(self):
        return f"""
        From: {self.sender}
        To: {self.receiver}
        Subject: {self.subject}
        Message: {self.message}
    """

    def __len__(self):
        return len(self.message)

    def __hash__(self):
        return hash((str(self.sender), str(self.receiver), str(self.subject), str(self.message), str(self.send_date)))

    def __bool__(self):
        return bool(self.message)


email1 = Email("john@example.com", "jane@example.com", "Meeting", "Hi Jane, let's have a meeting tomorrow.", "2022-05-10")

email2 = Email("jane@example.com", "john@example.com", "Re: Meeting", "Sure, let's meet at 2 PM.", "2022-05-10")

email3 = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob, how are you?", "2022-05-09")

print(email1)
print(len(email2))  # Вывод: 24
print(hash(email3))  # Вывод: -920444056
print(bool(email1))  # Вывод: True
print(email2 > email3)  # Вывод: True
