import requests
import json
import conf

def pedir_token(usuario, clave):
    url = "https://10.10.20.14/api/aaaLogin.json"
    data = {
        "aaaUser": {
            "attributes": {
                "name": usuario,
                "pwd": clave
            }
        }
    }
    cabecera = {
        "Content-Type": "application/json"
    }

    requests.packages.urllib3.disable_warnings()
    respuesta = requests.post(url, data=json.dumps(data), headers=cabecera, verify=False)
    respuesta_json = respuesta.json()
    token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    return token

token = pedir_token(conf.usuario, conf.clave)
print("Token: " + token)

url1 = "https://10.10.20.14/api/class/topSystem.json"
#GET http://apic-ip-address/api/class/topSystem.json"
cabecera = {
    "Content-Type": "application/json"}
WebToken = {
    "APIC-Cookie": pedir_token(conf.usuario, conf.clave)

}

try:
    respuesta1 = requests.get(url1, headers=cabecera, cookies=WebToken,verify=False)
except Exception as err:
    print("Error al pedir el API")
    exit(1)

respuesta1_json = respuesta1.json()
print(respuesta1_json)

for i in range(0,4):
    print("ip : "+respuesta1.json()["imdata"][i]["topSystem"]["attributes"]["address"])
    ip_local = respuesta1_json["imdata"][i]["topSystem"]["attributes"]["address"]
    mac_fabric = respuesta1_json["imdata"][i]["topSystem"]["attributes"]["fabricMAC"]
    estado = respuesta1_json["imdata"][i]["topSystem"]["attributes"]["state"]
    print("IP:", ip_local, "/", mac_fabric, "/", estado)

print(respuesta1.request.url)
print(respuesta1.request.method)
print(respuesta1.request.headers["Cookie"])

print(respuesta1.headers["Server"])
