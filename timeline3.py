import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox057b1c295bdc4083a854a943553cf4ac.mailgun.org/messages",
        auth=("api", "key-756b25f61f2ee481e9a951b655a4d29e"),
        data={"from": "mailgun@sandbox057b1c295bdc4083a854a943553cf4ac.mailgun.org",
              "to": ["emmajflyn@hotmail.com", "emma.flynn13@imperial.ac.uk"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
send_simple_message()
  