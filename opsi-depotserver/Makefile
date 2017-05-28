# $FreeBSD$

PORTNAME=	opsi-depotserver
DISTVERSION=	4.0.7.2
DISTVERSIONSUFFIX=	1
MASTER_SITES=	https://github.com/opsi-org/opsi-depotserver/archive/
DISTNAME=	${DISTVERSION}-${DISTVERSIONSUFFIX}
CATEGORIES=	sysutils

WRKSRC=		${WRKDIR}/${PORTNAME}-${DISTNAME}

NO_BUILD=	yes

USES=	shebangfix python
SHEBANG_FILES=	opsi-setup opsi-set-rights

#RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}ldap:net/py-ldap
LIB_DEPENDS=	libnewt.so:devel/newt

#TODO python-opsi samba-client

#USES=           python:-2.7
#USE_PYTHON=     autoplist distutils

MAINTAINER=	youremail@example.com
COMMENT=	opsi depotserver

post-extract:
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/opsi-setup

do-install:
#	${PW} addgroup pcpatch
#	${PW} useradd -G pcpatch opsiconfd
	${INSTALL_SCRIPT} ${WRKSRC}/opsi-setup ${STAGEDIR}${PREFIX}/bin	
	${REINPLACE_CMD} -e 's|/usr/bin|${PREFIX}/bin|g' ${WRKSRC}/opsi-set-rights
	${INSTALL_SCRIPT} ${WRKSRC}/opsi-set-rights ${STAGEDIR}${PREFIX}/bin	

post-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/var
	${MKDIR} ${STAGEDIR}${PREFIX}/var/lib/opsi/ntfs-images
	${MKDIR} ${STAGEDIR}${PREFIX}/var/lib/opsi/repository
	${MKDIR} ${STAGEDIR}${PREFIX}/var/log/opsi/bootimage
	${MKDIR} ${STAGEDIR}${PREFIX}/var/log/opsi/clientconnect
	${MKDIR} ${STAGEDIR}${PREFIX}/var/log/opsi/instlog
	${MKDIR} ${STAGEDIR}${PREFIX}/var/log/opsi/userlogin
	${MKDIR} ${STAGEDIR}/home/opsiproducts

.include <bsd.port.mk>
