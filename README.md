# opsi (open pc server integration) the open source client management system FreeBSD ports
	
	WORK
		- opsi-depotserver
		- python-opsi
		- opsiconfd
		- opsipxeconfd
		- opsi-setup
		- opsi-product-updater
		- configed
		- opsi-linux-bootimage
		- pxe boot
		- netboot
		- hwinvent
		- rc.d scripts
		
	TODO
		- detect upgrade
		
		
		- testing

### install:

```
pkg install -y python py27-twisted py27-pycrypto duplicity py27-netifaces py27-openssl py27-pyparsing py27-magic py27-pip py27-psutil py27-service_identity  py27-ldap py27-MySQLdb py27-sqlalchemy11 py27-python-rrdtool

pkg install -y gettext-tools zsync asciidoc bash newt sudo samba46
```

#### wimlib
```
pkg install -y  gmake e2fsprogs-libuuid fusefs-libs libublio pkgconf
```

#### if dhcp server is needed
```
pkg install -y isc-dhcp43-server
```

#### optional:
zeroconf
```
pkg install -y py27-dbus py27-avahi
```

#### with mysql-server:
```
pkg install -y mysql56-server
```

#### install ports:
make sure your ports tree is updated

`portsnap fetch update`

```
cd opsi-depotserver && make clean install; cd ..
cd opsi-configed && make clean install; cd ..
cd wimlib && make clean install; cd ..
```

#### create adminuser
```
pw adduser adminuser -G opsiadmin,pcpatch
passwd adminuser
smbpasswd -a adminuser
```

#### use MySQL backend
```
opsi-setup --configure-mysql
```

	do not forget to edit /usr/local/etc/opsi/backendManager/dispatch.conf to use mysql

### start services
	make sure the following services are running ( service [name] start )
	isc-dhcpd
		your subnet should be configured in /usr/local/etc/dhcpd.conf befor

	samba_server

	optional dbus and avahi
		dbus
		avahi-daemon

### to init the configuration after first install
```
opsi-setup --init-current-config --auto-configure-dhcpd --auto-configure-samba
opsi-setup --set-rights
```

### set pcpatch password
```
opsi-admin -d task setPcpatchPassword
```

### after an update run
```
opsi-setup --update-from unknown
opsi-setup --set-rights  /usr/local/etc/opsi
opsi-setup --set-rights /tftpboot
```

### Install/Update opsi-products
```
opsi-product-updater -vv -i
```

### start opsi services
```
service atftpd start
service opsiconfd start
service opsipxeconfd start
```

`go to https://<opsidepotserver>:4447`

also see http://uib.de/de/opsi-dokumentation/dokumentationen/
