import requests
import json
import conf


def pedir_token(usuario, clave):
url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

data = {
    "aaaUser" : {
        "attributes" : {
            "name" : "usuario",
            "pwd" : "clave"
        }
    }
}

cabecera = {"content-type":"application/json" }


requests.packages.urllib3.disable_warnings()
respuesta = requests.post(url,json.dumps(data),headers=cabecera, verify= False)
respuesta_json=respuesta.json()
print(respuesta.json())

API_Token = respuesta_json["indat"][0]["aaaLogin"]["attributes"]["token"]
print("hola")
return token

token = pedir_token(conf.usuario,conf.clave)
print("token: "+token)
# GET https://apic-ip-address/api/classtopSystem.json"
url1 = "https://sandboxapicdc.cisco.com/api/class/topSystem.json"
cabecera = {
  "content-Type": "application/json"
}
WebToken = {
  "APIC-Cookie": pedir_token(conf.usuario,conf.clave)
}

try:
    respuesta1 = requests.get(url1, headers=cabecera, cookies=WebToken,verify=False)
except Exception as err:
   print ("Error al pedir el API")
   exit (1)


respuesta1 = requests.get(url, headers=cabecera, cookies=WebToken,verify=False)
print(respuesta1.jason())

for i in range(0,int(respuesta1.json()["totalCount"]))
    #print("ip : " + respuesta1.json()["imdata"]["i"]["topSystem"]["attributes"]["address"])
    ip_local = respuesta1.json()["imdata"]["i"]["topSystem"]["attributes"]["address"]
    mac_fabric = respuesta1.json()["imdata"]["i"]["topSystem"]["attributes"]["address"]
    estado = respuesta1.json()["imdata"]["i"]["topSystem"]["attributes"]["state"]
    print("IP: "+ip_local+" / "+mac_fabric+" / "+estado)

print(respuesta1.request.url)
print(respuesta1.request.method)
print(respuesta1.request.headers["Cookies"])

print(respuesta1.headers["server"])
