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

#USE_GITHUB=	yes

USES=		python
USE_PYTHON=     autoplist distutils

#SHEBANG_FILES=	opsi-setup opsi-set-rights

#RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}ldap:net/py-ldap
#LIB_DEPENDS=	libnewt.so:devel/newt

#TODO python-opsi samba-client

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

#post-install:
#	(cd ${STAGEDIR}${PREFIX} \
#	  && ${PYTHON_CMD} ${PYTHON_LIBDIR}/compileall.py \
#	   -d ${PYTHONPREFIX_SITELIBDIR} -f ${PYTHONPREFIX_SITELIBDIR:S;${PREFIX}/;;})

#post-install:
#	${MKDIR} ${STAGEDIR}${PREFIX}/etc/opsi
#        ${MKDIR} ${STAGEDIR}${PREFIX}/usr/share/opsiconfd/static
#        ${MKDIR} ${STAGEDIR}${PREFIX}/var/lib/opsiconfd/rrd
#        ${MKDIR} ${STAGEDIR}${PREFIX}/var/log/opsi/opsiconfd

.include <bsd.port.mk>
