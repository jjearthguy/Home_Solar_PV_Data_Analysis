########## Libraries ##########
import json
import requests

########## SolarEdge API ##########
### API Documentation
# https://knowledge-center.solaredge.com/sites/kc/files/se_monitoring_api.pdf
# Limitations
#  - 300 parallel requests each day for each site from the same source IP
#  - Max of 3 concurrent API calls from the same source IP

### Solar edge site
url = "https://monitoringapi.solaredge.com/"

### API Key from SolarEdge
key = "KOFTNIN0DHCCNHL2WQ1ISTMG9UH4GF7D"
params = {'api_key': key}

### SolarEdge Site Number
site = "1963565"

### Email and text messages
# https://medium.com/testingonprod/how-to-send-text-messages-with-python-for-free-a7c92816e1a4

### Site Overview Test
# siteOverview = "https://monitoringapi.solaredge.com/site/" + site + "/overview.json"
siteOverview = url + "site/" + site + "/details?api_key=" + key
response = requests.get(siteOverview)
data = response.json()
print('\n',data)
# print('\n')

### Site Energy Call
siteEnergy = url + "site/" + site + "/dataPeriod?api_key" + key
response = requests.get(siteEnergy)
data = response.json()
print('\n',data)

### Site Power Call
sitePower = ""

### Data parse code
# try:
#     # GET request
#     response = requests.get(siteOverview, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         print(f"Request failed with status code {response.status_code}")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")