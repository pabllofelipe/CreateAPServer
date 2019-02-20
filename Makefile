PREFIX=/opt/sw4iot/CreateAPServer
SERVICE=sw4iot_ap_server.service
SOCK=sw4iot_ap_server.sock
RUN=/run/sw4iot

all:
	@echo "Run 'make install' for installation."
	@echo "Run 'make uninstall' for uninstallation."

install:
	# create opt directory
	mkdir -p $(PREFIX)
	# 
	cp -R ap_server $(PREFIX)/
	cp requirements.txt $(SERVICE) wsgi.py $(PREFIX)/
	# cp service to systemd
	cp $(PREFIX)/$(SERVICE) /etc/systemd/system/
	# install dependencies
	python3 -m venv $(PREFIX)/venv
	$(PREFIX)/venv/bin/pip install -r requirements.txt
	# 
	systemctl stop $(SERVICE)
	systemctl start $(SERVICE)
	systemctl enable $(SERVICE)
	systemctl daemon-reload
	mkdir -p $(RUN)
	ln -s $(PREFIX)/$(SOCK) $(RUN)/$(SOCK)

uninstall:
	# disable and remove service
	systemctl stop $(SERVICE)
	systemctl disable $(SERVICE)
	rm /etc/systemd/system/$(SERVICE)
	systemctl daemon-reload
	# remove opt directory
	rm -rf $(PREFIX)
	rm $(RUN)/$(SOCK)
