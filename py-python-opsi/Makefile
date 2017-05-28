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

WRKSRC=		${WRKDIR}/${GH_PROJECT}-${DISTNAME}

NO_BUILD=	yes

USES=		python
USE_PYTHON=     autoplist distutils

RUN_DEPENDS=	duplicity:sysutils/duplicity \
		${PYTHON_PKGNAMEPREFIX}twisted>0:devel/py-twisted \
		${PYTHON_PKGNAMEPREFIX}openssl>0:security/py-openssl \
		${PYTHON_PKGNAMEPREFIX}pycrypto>0:security/py-pycrypto \
		${PYTHON_PKGNAMEPREFIX}service_identity>0:security/py-service_identity \
		${PYTHON_PKGNAMEPREFIX}magic>0:devel/py-magic \
		${PYTHON_PKGNAMEPREFIX}pip>0:devel/py-pip

MAINTAINER=	m.ehinger@ltur.de

post-patch:
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/OPSI/UI.py
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/OPSI/Util/Task/Backup.py
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/tests/manual_tests/test_ui.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Util/File/Opsi/__init__.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Service/Worker.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Util/Task/Certificate.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Backend/Backend.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Backend/BackendManager.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Util/Task/CleanupBackend.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/OPSI/Util/Task/ConfigureBackend/ConfigurationData.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/tests/test_backend_backendmanager.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/tests/test_util_file_opsi_backup.py
	${REINPLACE_CMD} -e 's|"/etc/|"${PREFIX}/etc/|g' ${WRKSRC}/OPSI/System/Posix.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/tests/test_util_task_samba.py
	${REINPLACE_CMD} -e "s|'/var/|'${PREFIX}/var/|g" ${WRKSRC}/OPSI/Backend/File.py
	${REINPLACE_CMD} -e "s|'/var/|'${PREFIX}/var/|g" ${WRKSRC}/OPSI/Util/Task/*.py
	${REINPLACE_CMD} -e 's|"/var/|"${PREFIX}/var/|g' ${WRKSRC}/OPSI/Util/Task/*.py
	${REINPLACE_CMD} -e 's|"/var/|"${PREFIX}/var/|g' ${WRKSRC}/data/backends/*.conf
	${REINPLACE_CMD} -e "s|'/var/|'${PREFIX}/var/|g" ${WRKSRC}/data/backendManager/extend.d/*.conf
	${REINPLACE_CMD} -e "s|'/var/|'${PREFIX}/var/|g" ${WRKSRC}/data/backendManager/extend.d/configed/*.conf
	${REINPLACE_CMD} -e "s|'/var/|'${PREFIX}/var/|g" ${WRKSRC}/tests/*.py
	${REINPLACE_CMD} -e "s|'share/|'${PREFIX}/share/|g" ${WRKSRC}/setup.py

post-install:
	${PYTHON_CMD} -m pip install python-pam
	${PYTHON_CMD} -m pip install -r ${WRKSRC}/requirements.txt
	${INSTALL_DATA} ${WRKSRC}/data/backendManager/extend.d/*.conf ${STAGEDIR}${PREFIX}/etc/opsi/backendManager/extend.d
	${INSTALL_DATA} ${WRKSRC}/data/hwaudit/locales/* ${STAGEDIR}${PREFIX}/etc/opsi/hwaudit

.include <bsd.port.mk>
