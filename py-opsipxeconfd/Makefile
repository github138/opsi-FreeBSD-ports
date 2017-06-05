# $FreeBSD$

GH_PROJECT=	opsipxeconfd
PORTNAME=	 ${PYTHON_PKGNAMEPREFIX}${GH_PROJECT}
DISTVERSION=	4.0.7.5
DISTVERSIONSUFFIX=	3
DISTNAME=	${DISTVERSION}-${DISTVERSIONSUFFIX}
DISTFILES=	${DISTVERSION}-${DISTVERSIONSUFFIX}${EXTRACT_SUFX}

MASTER_SITES=	https://github.com/opsi-org/${GH_PROJECT}/archive/
CATEGORIES=	sysutils

WRKSRC=		${WRKDIR}/${GH_PROJECT}-${DISTNAME}

NO_BUILD=	yes

USES=		python
USE_PYTHON=     autoplist distutils

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}python-opsi>0:${PWD}/../py-python-opsi \
		opsi-linux-bootimage>0:${PWD}/../opsi-linux-bootimage

OPTIONS_DEFINE= ATFTP
OPTIONS_DEFAULT= ATFTP

ATFTP_DESC=  with opsi atftpd
ATFTP_RUN_DEPENDS=	opsi-atftp>0:${PWD}/../opsi-atftp

#USE_PACKAGE_DEPENDS=yes

USE_RC_SUBR=   opsipxeconfd
SUB_LIST=      PYTHON_CMD=${PYTHON_CMD}

SUB_FILES=	opsipxeconfd.conf
PLIST_FILES=	"${PREFIX}/etc/newsyslog.conf.d/opsipxeconfd.conf"

MAINTAINER=	m.ehinger@ltur.de
COMMENT=	This package contains the opsi pxe configuration daemon.

post-extract:
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/scripts/*
	${REINPLACE_CMD} -e "s| /etc/| ${PREFIX}/etc/|g" ${WRKSRC}/data/etc/opsi/*.conf

post-install:
	${RM} -r ${STAGEDIR}${PREFIX}/etc/opsi/systemdTemplates
	${RM} -r ${STAGEDIR}${PREFIX}/etc/logrotate.d
	${RM} -r ${STAGEDIR}${PREFIX}/etc/init.d
	${INSTALL_DATA} ${WRKDIR}/opsipxeconfd.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d/

add-plist-post:
	${REINPLACE_CMD} -e '/etc\/opsi\/systemdTemplates/d' ${TMPPLIST}
	${REINPLACE_CMD} -e '/etc\/logrotate.d/d' ${TMPPLIST}
	${REINPLACE_CMD} -e '/etc\/init.d/d' ${TMPPLIST}


.include <bsd.port.mk>
