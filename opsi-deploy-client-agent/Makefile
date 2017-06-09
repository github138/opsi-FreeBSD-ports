# $FreeBSD$

PORTNAME=	opsi-deploy-client-agent
DISTVERSION=	4.0.7.5
DISTVERSIONPREFIX=	v
MASTER_SITES=	https://github.com/opsi-org/${PORTNAME}/archive/
DISTNAME=	${DISTVERSIONPREFIX}${DISTVERSION}
CATEGORIES=	sysutils

WRKSRC=		${WRKDIR}/${PORTNAME}-${DISTVERSION}

RUN_DEPENDS=	wmi-client>0:net-mgmt/wmi-client

NO_BUILD=	yes

USES=   shebangfix python
SHEBANG_FILES=  opsi-*

MAINTAINER=	m.ehinger@ltur.de
COMMENT=	opsi-deploy-client-agent

post-extract:
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/opsi-*
	${REINPLACE_CMD} -e "s| /usr/| ${PREFIX}/|g" ${WRKSRC}/opsi-*
	${REINPLACE_CMD} -e "s| /usr/local/bin/env| /usr/bin/env|g" ${WRKSRC}/opsi-*
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/opsi-*
	${REINPLACE_CMD} -e "s| /etc/| ${PREFIX}/etc/|g" ${WRKSRC}/opsi-*
	${REINPLACE_CMD} -e "s|/usr/local/etc/hosts|/etc/hosts|g" ${WRKSRC}/opsi-*

do-install:
	${RM}  ${WRKSRC}/opsi-*.bak
	${MKDIR} ${STAGEDIR}/var/lib/opsi/depot/opsi-client-agent
	${INSTALL_SCRIPT} ${WRKSRC}/opsi-deploy-client-agent ${STAGEDIR}/var/lib/opsi/depot/opsi-client-agent

.include <bsd.port.mk>
