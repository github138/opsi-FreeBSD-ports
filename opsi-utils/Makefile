# $FreeBSD$

PORTNAME=	opsi-utils
DISTVERSION=	4.0.7.15
DISTVERSIONSUFFIX=	1
MASTER_SITES=	https://github.com/opsi-org/${PORTNAME}/archive/
DISTNAME=	${DISTVERSION}-${DISTVERSIONSUFFIX}
CATEGORIES=	sysutils

WRKSRC=		${WRKDIR}/${PORTNAME}-${DISTNAME}

NO_BUILD=	yes

USES=	shebangfix python
SHEBANG_FILES=	opsi-*

#RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}ldap:net/py-ldap
#LIB_DEPENDS=	libnewt.so:devel/newt

MAINTAINER=	youremail@example.com
COMMENT=	This package contains the opsi util collection.

post-extract:
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/opsi-*
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/opsi-*

do-install:
	${RM}  ${WRKSRC}/opsi-*.bak
	${MKDIR} ${STAGEDIR}${PREFIX}/bin
	${INSTALL_SCRIPT} ${WRKSRC}/opsi-* ${STAGEDIR}${PREFIX}/bin	

.include <bsd.port.mk>
