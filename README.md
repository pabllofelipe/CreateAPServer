#SOFTWAY4IoT-CreateAPServer

Install **create_ap** tool
```
git clone https://github.com/phelipealves/create_ap.git
cd create_ap
make install
apt install haveged
```

Install **CreateAPServer** tool
```
git clone https://github.com/LABORA-INF-UFG/SOFTWAY4IoT-CreateAPServer.git create_ap_server
cd create_ap_server
make install
```

----
Obs.: try running the following before starting create_ap:
```
nmcli r wifi off
rfkill unblock wlan
```