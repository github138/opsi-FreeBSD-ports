# $FreeBSD$

GH_PROJECT=	opsiconfd
PORTNAME=	${PYTHON_PKGNAMEPREFIX}${GH_PROJECT}
DISTVERSION=	4.0.7.9
DISTVERSIONSUFFIX=	1
DISTNAME=	${DISTVERSION}-${DISTVERSIONSUFFIX}
DISTFILES=	${DISTVERSION}-${DISTVERSIONSUFFIX}${EXTRACT_SUFX}

MASTER_SITES=	https://github.com/opsi-org/${GH_PROJECT}/archive/
CATEGORIES=	sysutils

WRKSRC=		${WRKDIR}/${GH_PROJECT}-${DISTNAME}

NO_BUILD=	yes

USES=		python
USE_PYTHON=     autoplist distutils

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}psutil>0:sysutils/py-psutil \
		${PYTHON_PKGNAMEPREFIX}service_identity>0:security/py-service_identity

OPTIONS_DEFINE=	ZEROCONF RRDTOOL
OPTIONS_DEFAULT= ZEROCONF RRDTOOL

ZEROCONF_DESC=	with dbus and avahi
RRDTOOL_DESC=	with rrdtool

ZEROCONF_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}dbus>0:devel/py-dbus \
			${PYTHON_PKGNAMEPREFIX}avahi>0:net/py-avahi

RRDTOOL_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}python-rrdtool>0:databases/py-python-rrdtool

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}python-opsi>0:${PWD}/../py-python-opsi

USE_PACKAGE_DEPENDS=	yes

USE_RC_SUBR=	opsiconfd
SUB_LIST=	PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	opsiconfd.conf

PLIST_FILES=	"${PREFIX}/etc/newsyslog.conf.d/opsiconfd.conf"

MAINTAINER=	m.ehinger@ltur.de
COMMENT=	This is the opsi configuration service

post-extract:
	${REINPLACE_CMD} -e "s| /usr/| ${PREFIX}/|g" ${WRKSRC}/data/etc/opsi/opsiconfd.conf
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/opsiconfd/opsiconfd.py
	${REINPLACE_CMD} -e "s| /etc/| ${PREFIX}/etc/|g" ${WRKSRC}/data/etc/opsi/opsiconfd.conf
	${REINPLACE_CMD} -e "s| /etc/| ${PREFIX}/etc/|g" ${WRKSRC}/scripts/opsiconfd-guard
	${REINPLACE_CMD} -e "s|	/etc/init.d/|	${PREFIX}/etc/rc.d/|g" ${WRKSRC}/scripts/opsiconfd-guard
	${REINPLACE_CMD} -e "s|'share/|'${PREFIX}/share/|g" ${WRKSRC}/setup.py

post-install:
	${RM} -r ${STAGEDIR}${PREFIX}/etc/opsi/systemdTemplates
	${RM} -r ${STAGEDIR}${PREFIX}/etc/logrotate.d
	${RM} -r ${STAGEDIR}${PREFIX}/etc/init.d
	${INSTALL_DATA} ${WRKDIR}/opsiconfd.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d/

add-plist-post:
	${REINPLACE_CMD} -e '/etc\/opsi\/systemdTemplates/d' ${TMPPLIST}
	${REINPLACE_CMD} -e '/etc\/logrotate.d/d' ${TMPPLIST}
	${REINPLACE_CMD} -e '/etc\/init.d/d' ${TMPPLIST}

.include <bsd.port.mk>
