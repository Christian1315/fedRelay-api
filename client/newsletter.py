
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

mailchimp = MailchimpMarketing.Client()

mailchimp.set_config({
  "api_key": "61ef1f76dccd299600db1d4ef5744bb3-us14",
  "server": "us14"
})

list_id = "d5e394c3c4"

member_info = {
    "email_address": "flore@gmail.com",
    "status": "subscribed",
    "merge_fields": {
      "FNAME": "Prudence",
      "LNAME": "McVankab"
    }
  }

try:
  response = mailchimp.lists.add_list_member(list_id, member_info)
  print("response: {}".format(response))
except ApiClientError as error:
  print("An exception occurred: {}".format(error.text))
  