import requests
import json
# phone = ['phone']
def smssend(phone,message):

    url= 'https://www.fast2sms.com/dev/bulk'
    para = {
        'authorization' : 'fBnh1bU8lH6JraWedSYKZqwsj9CIy7mMkogvp5zVXDPN4E2FQuPCvEny49IjgkTpOKmxfFXVZuDQ3s5Y',
        'sender_id' : 'FastWP',
        'message' : message,
        'language' : 'english',
        'route' : 'p',
        'numbers' : phone
    }

    response = requests.get(url, para)
    dic = response.json()
    print(dic)

# smssend(phone ,'This is test SMS send using python. programmer is SAURABH.')
# 
#     #This SMS send using python. programmer is SAURABH.
# smssend(phone, 'python msg')