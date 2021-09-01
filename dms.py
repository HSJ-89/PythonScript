import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from xml.etree import cElementTree as ET
import lxml.etree as etree
def getData(ip):
    response = requests.get("https://{}/login.ows?username=User&password=11111111".format(ip), verify=False)
    if (response.status_code == 200):
        print(ip)
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
    response = requests.get("https://{}/dynaObjRead.xml?O17".format(ip), verify=False)
    if (response.status_code == 200):
        #print("The request was a success!")
        #print(response.text)
        xml2=response.text
        #print(xml)
        # Code here will only run if the request is successful
    elif (response.status_code == 404):
        print("Result not found!")
    return(xml,xml2)
def PrintData(temp1, temp2):
    title=0
    content=0
    roottemp1 = "<h>{}</h>" .format(temp1)
    xml_str1 = etree.fromstring(roottemp1)
    xml_str2=etree.tostring(xml_str1, pretty_print=True).decode()
    xml_root= etree.fromstring(xml_str2)
    signtemp= etree.fromstring(temp2)
    sign_temp=etree.tostring(signtemp, pretty_print=True).decode()
    xml_root2= etree.fromstring(sign_temp)
    #print(sign_temp)
    for page in list(xml_root):
        #print(page)
        title = page.find('Temp_Setting_1').text
        content = page.find('Temp_Setting_2').text
    for page in list(xml_root2):
        #print(page)
        temp = page.find('D').text
        #content = page.find('Temp_Setting_2').text
    print('Temp_Setting_1: %s; Temp_Setting_2: %s; Sign_Temparature: %s' % (title, content, temp))
    
dms = ["10.10.214.53","10.10.209.77","10.10.209.89","10.10.214.69","10.10.205.109","10.10.205.113","10.10.201.65","10.10.208.65","10.10.214.57","10.10.210.61","10.10.209.57","10.10.209.73","10.10.209.85","10.10.207.65","10.10.207.85","10.10.207.89","10.10.210.53","10.10.213.61","10.10.214.65","10.10.215.53","10.10.204.85","10.10.204.89","10.10.212.57","10.10.212.61","10.10.209.53","10.10.209.69","10.10.209.93","10.10.209.97","10.10.215.61","10.10.203.81","10.10.203.85","10.10.203.89","10.10.203.93","10.10.203.97","10.10.203.105","10.10.203.109","10.10.202.57","10.10.201.77","10.10.207.61","10.10.207.69","10.10.207.77","10.10.202.53","10.10.204.69","10.10.215.65","10.10.203.101","10.10.205.61","10.10.209.65","10.10.207.81","10.10.201.61","10.10.208.61","10.10.209.61","10.10.204.65","10.10.216.53","10.10.201.69","10.10.216.57","10.10.215.57","10.10.201.97","10.10.201.105","10.10.201.109","10.10.201.113","10.10.208.57","10.10.213.53","10.10.213.69","10.10.205.57","10.10.204.93","10.10.213.57","10.10.203.61","10.10.203.73","10.10.203.77","10.10.204.61","10.10.201.57","10.10.205.85","10.10.203.69","10.10.208.53","10.10.208.69","10.10.203.65","10.10.205.105","10.10.209.81","10.10.214.61","10.10.204.73","10.10.201.73","10.10.201.81","10.10.201.85","10.10.201.89","10.10.201.93","10.10.201.101","10.10.212.53","10.10.207.53","10.10.207.57","10.10.207.73","10.10.206.53","10.10.206.57","10.10.202.61","10.10.215.69","10.10.215.73","10.10.203.53","10.10.203.57","10.10.205.53","10.10.205.65","10.10.205.69","10.10.205.73","10.10.205.77","10.10.205.81","10.10.205.89","10.10.205.93","10.10.205.97","10.10.205.101","10.10.204.53","10.10.204.57","10.10.204.77","10.10.204.81","10.10.201.53"]
for x in dms:
  temp1,temp2=getData(x)
  #print (temp2)
  PrintData(temp1,temp2)



