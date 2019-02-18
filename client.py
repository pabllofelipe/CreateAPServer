import requests
import requests_unixsocket

requests_unixsocket.monkeypatch()

path = "/home/phelipe/Documents/git/sw4iot/SOFTWAY4IoT-CreateAPServer/".replace('/', '%2F')
r = requests.get('http+unix://{}sw4iot_ap_server.sock/ap_running'.format(path))
print(r.status_code, r.json())

# r = requests.delete('http+unix://{}sw4iot_ap_server.sock/stop_ap/{}'.format(path, 'wlan_s10'))
# print(r.status_code, r.content)


