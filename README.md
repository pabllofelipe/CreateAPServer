# SOFTWAY4IoT-CreateAPServer

Dependencies
```
$ apt install python-dev
$ apt install hostapd
$ apt install iproute2
$ apt install iw
$ apt install haveged (optional)
```

Install [**create_ap**](https://github.com/sw4iot/create_ap) tool
```
git clone https://github.com/sw4iot/create_ap.git
cd create_ap
make install
```

Install **CreateAPServer** tool
```
git clone https://github.com/LABORA-INF-UFG/SOFTWAY4IoT-CreateAPServer.git CreateAPServer
cd CreateAPServer
make install
```

----
Obs.: try running the following before starting create_ap:
```
nmcli r wifi off
rfkill unblock wlan
```
