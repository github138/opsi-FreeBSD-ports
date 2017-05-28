# $FreeBSD$

PORTNAME=	opsi-configed_ucs
DISTNAME=	opsi-configed
DISTVERSION=	4.0.7.5.22
DISTVERSIONSUFFIX=	2
MASTER_SITES=	http://download.opensuse.org/repositories/home:/uibmz:/opsi:/opsi40/Univention_4.0/
DISTFILES=	opsi-configed_4.0.7.5.22-2.tar.gz
CATEGORIES=	misc

WRKSRC=		${WRKDIR}/${DISTNAME}-${DISTVERSION}

NO_BUILD=	yes

MAINTAINER=	youremail@example.com
COMMENT=	This package contains the opsi util collection.

#post-extract:
#	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/opsi-*
#	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/opsi-*

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/lib/configed
	${INSTALL_DATA} ${WRKSRC}/*.jar ${STAGEDIR}${PREFIX}/lib/configed

.include <bsd.port.mk>
