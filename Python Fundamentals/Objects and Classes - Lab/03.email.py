class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

user_input = input()

while user_input != "Stop":
    lines = user_input.split(" ")
    email = Email(lines[0], lines[1], lines[2])
    emails.append(email)
    user_input = input()

send_emails = [int(x) for x in input().split(", ")]

for i in send_emails:
    emails[i].sent()

for email in emails:
    print(email.get_info())
