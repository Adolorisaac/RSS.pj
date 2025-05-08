import requests
import xml.etree.ElementTree as ET 
user_RSS = input("Enter Your RSS URL")
response = requests.get (user_RSS)
print(response.text)
root = ET.fromstring(response.text)
for item in root.findall(".//item"):
    title = item.find("title"). text 
    description = item.find("description").text 
    Link = item.find ("link").text 
print ( "\n Title:", title)
print ("\n description:", description)
print ("\n link:", Link ) 
