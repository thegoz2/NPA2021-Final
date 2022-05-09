from ncclient import manager
import xml.dom.minidom
import requests 
import time
m = manager.connect(
    host="10.0.15.109",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
    )


netconf_loopback = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
           
            </Loopback>
        </interface>
    </native>
</filter>
"""
access_token = 'MTIxZGQ1NWUtNTliYi00Y2U0LTg3NmYtMjc2ODJjMTM5ZjJmOGMyZjAyNDEtYTg4_P0A1_4a252141-f787-4173-a4c9-bde69c553a24' 
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNjUwODkzMjAtY2QxOS0xMWVjLWE1NGUtNGQ2MmNhMWM4YmVl"
url = 'https://webexapis.com/v1/messages'
headers = {     'Authorization': 'Bearer {}'.format(access_token),     
            'Content-Type': 'application/json' } 
parampostUP = {'roomId': room_id, 'markdown':"Loopback62070150 - Operational status is UP"} 
parampostDOWN = {'roomId': room_id, 'markdown':"Loopback62070150 - Operational status is DOWN"} 
paramget ={'roomId': room_id}
def bot():
    while (True):
        resget = requests.get(url, headers=headers, params=paramget) 
        newtext = resget.json().get('items')[0].get('text') 
        print("Received message:",newtext)
        if newtext == "62070150":
            netconf_reply = m.get_config(source="running", filter=netconf_loopback)
            if "<shutdown/>" in str(netconf_reply):
                respost = requests.post(url, headers=headers, json=parampostDOWN)
            else:
                respost = requests.post(url, headers=headers, json=parampostUP)

        # netconf_filter = """
        # <filter>
        #  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
        # </filter>
        # """
        # netconf_reply = m.get_config(source="running", filter=netconf_filter)
        # print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())




        # print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    sleep(1)

bot()




