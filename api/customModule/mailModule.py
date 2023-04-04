from mailjet_rest import Client
api_key = "4c56711e155c22fe395396220da8adf4"
api_secret = "0144c4b3f58241de706deab5cf1a9c55"

mailjet = Client(auth=(api_key, api_secret), version='v3.1')

def deliveryMail(name,colis_sender_email,follow_code,colis_recever_name,subject):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "contact@fedrelay.com",
                    "Name": subject
                },
                "To": [
                    {
                        "Email": colis_sender_email,
                        'Name':colis_recever_name,
                    }
                ],

                "TemplateID": 4647179,
                "TemplateLanguage": True,
                "Subject": subject,
                "Variables": {
                    'name':name,
                    'colis_recever_name':colis_recever_name,
                    'follow_code':follow_code}
            }
        ]
    }

    result = mailjet.send.create(data=data)
    # print(result.status_code)
    # print(result.json())

def signUpMail(email,subject):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "contact@fedrelay.com",
                    "Name": "Inscription"
                },
                "To": [
                    {
                        "Email": email,
                    }
                ],

                "TemplateID": 4646992,
                "TemplateLanguage": True,
                "Subject": subject,
                "Variables": {}
            }
        ]
    }
    
    result = mailjet.send.create(data=data)
    # print(result.status_code)
    # print(result.json())