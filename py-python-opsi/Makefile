# $FreeBSD$

GH_PROJECT=	python-opsi
PORTNAME=	${PYTHON_PKGNAMEPREFIX}${GH_PROJECT}
DISTVERSION=	4.0.7.41
DISTVERSIONSUFFIX=	1
DISTNAME=	${DISTVERSION}-${DISTVERSIONSUFFIX}
DISTFILES=	${DISTVERSION}-${DISTVERSIONSUFFIX}${EXTRACT_SUFX}

MASTER_SITES=	https://github.com/opsi-org/${GH_PROJECT}/archive/
CATEGORIES=	sysutils

WRKSRC=		${WRKDIR}/${GH_PROJECT}-${DISTNAME}

NO_BUILD=	yes

#USE_GITHUB=	yes

USES=		python
USE_PYTHON=     autoplist distutils

#SHEBANG_FILES=	opsi-setup opsi-set-rights

RUN_DEPENDS=	duplicity:sysutils/duplicity \
		${PYTHON_PKGNAMEPREFIX}twisted>0:devel/py-twisted \
		${PYTHON_PKGNAMEPREFIX}openssl>0:security/py-openssl \
		${PYTHON_PKGNAMEPREFIX}pycrypto>0:security/py-pycrypto \
		${PYTHON_PKGNAMEPREFIX}service_identity>0:security/py-service_identity \
		${PYTHON_PKGNAMEPREFIX}magic>0:devel/py-magic \
		${PYTHON_PKGNAMEPREFIX}pip>0:devel/py-pip
#LIB_DEPENDS=	libnewt.so:devel/newt

MAINTAINER=	youremail@example.com
COMMENT=	OPSI org Depotserver

post-extract:
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|'share/|'${PREFIX}/share/|g" ${WRKSRC}/setup.py

#pre-install:

#do-install:
#	${PW} addgroup pcpatch
#	${PW} useradd -G pcpatch opsiconfd
#	${INSTALL_SCRIPT} ${WRKSRC}/opsi-setup ${STAGEDIR}${PREFIX}/bin	
#	${REINPLACE_CMD} -e 's|/usr/bin|${PREFIX}/bin|g' ${WRKSRC}/opsi-set-rights
#	${INSTALL_SCRIPT} ${WRKSRC}/opsi-set-rights ${STAGEDIR}${PREFIX}/bin	

post-install:
	${PYTHON_CMD} -m pip install python-pam
	${PYTHON_CMD} -m pip install -r ${WRKSRC}/requirements.txt
	${MKDIR} ${STAGEDIR}${PREFIX}/etc/opsi/modules
#        ${MKDIR} ${STAGEDIR}${PREFIX}/usr/share/opsiconfd/static
#        ${MKDIR} ${STAGEDIR}${PREFIX}/var/lib/opsiconfd/rrd
#        ${MKDIR} ${STAGEDIR}${PREFIX}/var/log/opsi/opsiconfd

.include <bsd.port.mk>
