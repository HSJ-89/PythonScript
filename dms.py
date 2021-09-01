import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from xml.etree import cElementTree as ET
import lxml.etree as etree
def getData(ip):
    response = requests.get("https://{}/login.ows?username=User&password=11111111".format(ip), verify=False)
    if (response.status_code == 200):
        print("The request was a success!")
        # Code here will only run if the request is successful
    elif (response.status_code == 404):
        print("Result not found!")
    response = requests.get("https://{}/get_temp_status.xml?random=4549".format(ip), verify=False)
    if (response.status_code == 200):
        #print("The request was a success!")
        #print(response.text)
        xml=response.text
        #print(xml)
        # Code here will only run if the request is successful
    elif (response.status_code == 404):
        print("Result not found!")
    return(xml)
def PrintData(xml):
    root = "<h>{}</h>" .format(xml)
    xml_str1 = etree.fromstring(root)
    xml_str2=etree.tostring(xml_str1, pretty_print=True).decode()
    xml_root= etree.fromstring(xml_str2)
#print(xml_str2)
    for page in list(xml_root):
        #print(page)
        title = page.find('Temp_Setting_1').text
        content = page.find('Temp_Setting_2').text
        print('Temp_Setting_1: %s; Temp_Setting_2: %s' % (title, content))
    
dms = ["10.10.214.53","10.10.209.77"]
for x in dms:
  xml2=getData(x)
  PrintData(xml2)



