# $FreeBSD$

PORTNAME=	opsi-configed
DISTNAME=	opsi-configed
DISTVERSION=	4.0.7.5.22
DISTVERSIONSUFFIX=	2
http://download.opensuse.org/repositories/home:/uibmz:/opsi:/opsi40/xUbuntu_16.04/opsi-configed_4.0.7.5.22-2.tar.gz
MASTER_SITES=	http://download.opensuse.org/repositories/home:/uibmz:/opsi:/opsi40/Univention_4.0/
DISTFILES=	${PORTNAME}_${DISTVERSION}-${DISTVERSIONSUFFIX}.tar.gz
CATEGORIES=	misc

WRKSRC=		${WRKDIR}/${DISTNAME}-${DISTVERSION}

NO_BUILD=	yes

MAINTAINER=	m.ehinger@ltur.de
COMMENT=	opsi Config Editor - management interface for opsi

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/lib/configed
	${INSTALL_DATA} ${WRKSRC}/*.jar ${STAGEDIR}${PREFIX}/lib/configed

.include <bsd.port.mk>
