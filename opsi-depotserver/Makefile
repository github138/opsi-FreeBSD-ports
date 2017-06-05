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

RUN_DEPENDS=    ${PYTHON_PKGNAMEPREFIX}opsiconfd>0:${PWD}/../py-opsiconfd \
		${PYTHON_PKGNAMEPREFIX}opsipxeconfd>0:${PWD}/../py-opsipxeconfd \
		opsi-utils>0:${PWD}/../opsi-utils

RUN_DEPENDS+=	${PYTHON_PKGNAMEPREFIX}ldap>0:net/py-ldap \
		${PYTHON_PKGNAMEPREFIX}MySQLdb>0:databases/py-MySQLdb \
		${PYTHON_PKGNAMEPREFIX}sqlalchemy11>0:databases/py-sqlalchemy11

LIB_DEPENDS=	libnewt.so:devel/newt

OPTIONS_DEFINE=	SAMBA
SAMBA_DESC=	Install Samba
SAMBA_USES=	samba

USE_PACKAGE_DEPENDS=yes

PKGUPGRADE=	${PKGDIR}/pkg-install

MAINTAINER=	youremail@example.com
COMMENT=	opsi depotserver

post-extract:
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/opsi-setup
	${REINPLACE_CMD} -e 's|/usr/bin|${PREFIX}/bin|g' ${WRKSRC}/opsi-set-rights
	${REINPLACE_CMD} -e "s|/samba/smb.conf|/smb4.conf|g" ${WRKSRC}/opsi-setup

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/opsi-setup ${STAGEDIR}${PREFIX}/bin	
	${INSTALL_SCRIPT} ${WRKSRC}/opsi-set-rights ${STAGEDIR}${PREFIX}/bin	

.include <bsd.port.mk>
