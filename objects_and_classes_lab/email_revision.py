class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()

while command != "Stop":
    info = command.split(' ')
    sender = info[0]
    receiver = info[1]
    content = info[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    command = input()

sent_emails = [int(x) for x in input().split(', ')]

for x in sent_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())
