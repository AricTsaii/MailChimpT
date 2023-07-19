#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "7e0b89bfe4746beecfaae7f219af3395-us8",
    "server": "us8"
  })

  response = client.lists.get_all_lists()
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))


# In[16]:


import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": "7e0b89bfe4746beecfaae7f219af3395-us8",
        "server": "us8"
})    

    response = client.lists.add_list_member("0d48b3885a", {"email_address": "aric990514@gmail.com", "status": "subscribed"})
    
    print(response)
except ApiClientError as error:
    print("Error: {}".format(error.text))


# In[17]:


import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": "7e0b89bfe4746beecfaae7f219af3395-us8",
        "server": "us8"
})    

    response = client.lists.add_list_member("0d48b3885a", {"email_address": "ryan.ramadhan@ematicsolutions.com", "status": "subscribed"})
    response = client.lists.add_list_member("0d48b3885a", {"email_address": "edwin.melendez@ematicsolutions.com", "status": "subscribed"})
    response = client.lists.add_list_member("0d48b3885a", {"email_address": "christianto@ematicsolutions.com", "status": "subscribed"})

    print(response)
except ApiClientError as error:
    print("Error: {}".format(error.text))


# In[18]:


import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "7e0b89bfe4746beecfaae7f219af3395-us8",
    "server": "us8"
  })

  response = client.campaigns.create({"type": "plaintext"})
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))


# In[20]:


import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "7e0b89bfe4746beecfaae7f219af3395-us8",
    "server": "us8"
  })

  response = client.campaigns.update("9002445e61", {"recipients": {"list_id": "0d48b3885a"}})
  response = client.campaigns.update("9002445e61", {"settings": {"subject_line": "Testing", "from_name": "AricT", "reply_to":"aric990514@gmail.com"}})


  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))


# In[22]:


import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "7e0b89bfe4746beecfaae7f219af3395-us8",
    "server": "us8"
  })
 
  response = client.campaigns.set_content("9002445e61", {"plain_text": "Hi Ematic team, this is Aric"})   
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))


# In[23]:


import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "7e0b89bfe4746beecfaae7f219af3395-us8",
    "server": "us8"
  })

  response = client.campaigns.send("9002445e61")
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))


# In[29]:


import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "7e0b89bfe4746beecfaae7f219af3395-us8",
    "server": "us8"
  })

  response = client.campaigns.get_content("9002445e61")
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))


# In[ ]:




