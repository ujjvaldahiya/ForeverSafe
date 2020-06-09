import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'
USEPROD = 'prod'
USESTAGE = 'stage'

class SMS:

    
    def __init__(self, apikey, secretkey, usetype, senderid ):
        self.smsUrl = 'https://www.way2sms.com/api/v1/sendCampaign'
        self.senderidurl = 'https://www.way2sms.com/api/v1/createSenderId'
        self.ApiKey = apikey
        self.SecretKey = secretkey
        self.UseType = usetype
        self.SenderId = senderid
        
    def createsenderid(self):
      req_params = {
      'apikey':self.ApiKey,
      'secret':self.SecretKey,
      'usetype': self.UseType,
      'senderid': self.SenderId
      }
      response = requests.post(self.senderidurl, req_params)
      return json.loads(response.text)
  
    def sendSMS(self, phoneNo, textMessage):
      req_params = {
      'apikey': self.ApiKey ,
      'secret': self.SecretKey,
      'usetype': self.UseType,
      'phone': phoneNo,
      'message':textMessage,
      'senderid': self.SenderId
      }
      response = requests.post(self.smsUrl, req_params)
      return json.loads(response.text)

# get response
'''response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
# print response if you want
print response.text'''