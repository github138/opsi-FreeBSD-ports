# $FreeBSD$

GH_PROJECT=	python-opsi
PORTNAME=	${PYTHON_PKGNAMEPREFIX}${GH_PROJECT}
DISTVERSION=	4.0.7.41
DISTVERSIONSUFFIX=	1
DISTNAME=	${DISTVERSION}-${DISTVERSIONSUFFIX}
DISTFILES=	${DISTVERSION}-${DISTVERSIONSUFFIX}${EXTRACT_SUFX}

MASTER_SITES=	https://github.com/opsi-org/${GH_PROJECT}/archive/
CATEGORIES=	sysutils

COMMENT=	This package contains the opsi python library.
MAINTAINER=	m.ehinger@ltur.de

WRKSRC=		${WRKDIR}/${GH_PROJECT}-${DISTNAME}

NO_BUILD=	yes

USES=		python gettext-tools
USE_PYTHON=     autoplist distutils

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}twisted>0:devel/py-twisted \
		${PYTHON_PKGNAMEPREFIX}pycrypto>0:security/py-pycrypto \
		duplicity:sysutils/duplicity \
		${PYTHON_PKGNAMEPREFIX}netifaces>0:net/py-netifaces \
		${PYTHON_PKGNAMEPREFIX}openssl>0:security/py-openssl \
		${PYTHON_PKGNAMEPREFIX}pyparsing>0:devel/py-pyparsing \
		${PYTHON_PKGNAMEPREFIX}magic>0:devel/py-magic \
		${PYTHON_PKGNAMEPREFIX}pip>0:devel/py-pip \
		sudo:security/sudo

PLIST_FILES=	"@sample etc/opsi/backendManager/dispatch.conf.default etc/opsi/backendManager/dispatch.conf" \
		"@sample etc/opsi/backendManager/acl.conf.default etc/opsi/backendManager/acl.conf"

USE_PACKAGE_DEPENDS=yes

post-patch:
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/OPSI/UI.py
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/OPSI/Util/Task/Backup.py
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/tests/manual_tests/test_ui.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Util/File/Opsi/__init__.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Service/Worker.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Util/Task/Certificate.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Backend/*.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Util/Task/CleanupBackend.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Util/Task/ConfigureBackend/ConfigurationData.py
	${REINPLACE_CMD} -e 's|'/etc'|'${PREFIX}/etc'|g' ${WRKSRC}/OPSI/Util/Task/ConfigureBackend/DHCPD.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/tests/test_backend_backendmanager.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/tests/test_util_file_opsi_backup.py
	${REINPLACE_CMD} -e 's|"/etc/|"${PREFIX}/etc/|g' ${WRKSRC}/OPSI/System/Posix.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/tests/test_util_task_samba.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Util/Task/*.py
	${FIND} ${WRKSRC}/OPSI/Util/Task/ -type f -name "*.py" -exec ${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" {} \;
	${REINPLACE_CMD} -e 's|"/etc/|"${PREFIX}/etc/|g' ${WRKSRC}/data/backends/*.conf
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/data/backendManager/extend.d/*.conf
	${REINPLACE_CMD} -e "s|'share/|'${PREFIX}/share/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|/samba/smb.conf|/smb4.conf|g" ${WRKSRC}/OPSI/Util/Task/ConfigureBackend/ConfigurationData.py
	${REINPLACE_CMD} -e "s|/samba/smb.conf|/smb4.conf|g" ${WRKSRC}/OPSI/Util/Task/Samba.py
	${REINPLACE_CMD} -e "s|/dhcp3/dhcpd.conf|/dhcpd.conf|g" ${WRKSRC}/data/backends/dhcpd.conf
	${REINPLACE_CMD} -e "s|sudo service dhcp3-server |service isc-dhcpd |g" ${WRKSRC}/data/backends/dhcpd.conf
#	${MKDIR} ${PREFIX}/etc/opsi
#	${MKDIR} /var/lib/opsi


post-install:
	${PYTHON_CMD} -m pip install python-pam
#	${PYTHON_CMD} -m pip install -r ${WRKSRC}/requirements.txt
#.if !exists( /usr/bin/python )
#	${LN} -s ${PYTHON_CMD} /usr/bin/python
#.endif

add-plist-post:
	${REINPLACE_CMD} -e '/^etc\/opsi\/backendManager\/acl\.conf\.default/d' ${TMPPLIST}
	${REINPLACE_CMD} -e '/^etc\/opsi\/backendManager\/dispatch\.conf\.default/d' ${TMPPLIST}

.include <bsd.port.mk>
