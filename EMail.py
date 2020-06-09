from mailjet_rest import Client

api_key = 'fb77e9f124e77927acf3e93c29af7e17'
api_secret = '3c54c57fdb06917726ddd0f20eb2f382'

def create_service():
    return Client(auth=(api_key, api_secret), version='v3.1')

def create_message(toemail, toname, subject, body):
    data = {
      'Messages': [
                    {
                            "From": {
                                    "Email": "suhelnaryal@gmail.com",
                                    "Name": "ForeverSafe Authentication"
                            },
                            "To": [
                                    {
                                            "Email": toemail,
                                            "Name": toname
                                    }
                            ],
                            "Subject": subject,
                            "TextPart": body,                           
                    }
            ]
    }
    return data

def send_email(service, data):                       
    return service.send.create(data=data).json()
