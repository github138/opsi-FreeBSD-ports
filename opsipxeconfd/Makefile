# $FreeBSD$

GH_PROJECT=	opsipxeconfd
PORTNAME=	${PYTHON_PKGNAMEPREFIX}${GH_PROJECT}
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

#RUN_DEPENDS=	atftp:tfp/opsi-atftp

MAINTAINER=	m.ehinger@ltur.de
COMMENT=	This package contains the opsi pxe configuration daemon.

post-extract:
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/scripts/*
	${REINPLACE_CMD} -e "s| /etc/| ${PREFIX}/etc/|g" ${WRKSRC}/data/etc/opsi/*.conf

post-install:
	${MKDIR} ${STAGEDIR}/tftpboot

.include <bsd.port.mk>
