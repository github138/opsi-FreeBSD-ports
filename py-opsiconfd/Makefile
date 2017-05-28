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

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}ldap>0:net/py-ldap
#RUN_DEPENDS+=	${PYTHON_PKGNAMEPREFIX}OPSI>0:sysutils/py-python-opsi

MAINTAINER=	m.ehinger@ltur.de
COMMENT=	This is the opsi configuration service

post-extract:
	${REINPLACE_CMD} -e "s| /usr/| ${PREFIX}/|g" ${WRKSRC}/data/etc/opsi/opsiconfd.conf
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/setup.py
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/opsiconfd/opsiconfd.py
	${REINPLACE_CMD} -e "s| /etc/| ${PREFIX}/etc/|g" ${WRKSRC}/data/etc/opsi/opsiconfd.conf
	${REINPLACE_CMD} -e "s| /etc/| ${PREFIX}/etc/|g" ${WRKSRC}/scripts/opsiconfd-guard
	${REINPLACE_CMD} -e "s|	/etc/init.d/|	${PREFIX}/etc/rc.d/|g" ${WRKSRC}/scripts/opsiconfd-guard
	${REINPLACE_CMD} -e "s|'/var/|'${PREFIX}/var/|g" ${WRKSRC}/opsiconfd/opsiconfd.py
	${REINPLACE_CMD} -e "s|'share/|'${PREFIX}/share/|g" ${WRKSRC}/setup.py

pre-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/share/opsiconfd/static
	${MKDIR} ${STAGEDIR}${PREFIX}/lib/configed
	${MKDIR} ${STAGEDIR}${PREFIX}/etc/opsi/modules
	${MKDIR} ${STAGEDIR}${PREFIX}/var/lib/opsi/config/clients
	${MKDIR} ${STAGEDIR}${PREFIX}/var/lib/opsi/config/depots
	${MKDIR} ${STAGEDIR}${PREFIX}/var/lib/opsi/config/products

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

post-install:
#	${MKDIR} ${STAGEDIR}${PREFIX}/lib/configed
#	${MKDIR} ${STAGEDIR}${PREFIX}/share/opsiconfd/static
#	(cd ${WRKSRC}/data/shared && ${COPYTREE_SHARE} . ${STAGEDIR}/share/opsiconfd/static)
#        ${MKDIR} ${STAGEDIR}${PREFIX}/var/lib/opsiconfd/rrd
#        ${MKDIR} ${STAGEDIR}${PREFIX}/var/log/opsi/opsiconfd
	@if [ ! -e ${PREFIX}/etc/opsi/opsiconfd.pem ]; then \
		${ECHO_CMD} "Creating certificate.."; \
		umask 077; \
		echo "RANDFILE = /tmp/opsiconfd.rand" 	>  /tmp/opsiconfd.cnf; \
		echo "" 				>> /tmp/opsiconfd.cnf; \
		echo "[ req ]" 				>> /tmp/opsiconfd.cnf; \
		echo "default_bits = 1024" 		>> /tmp/opsiconfd.cnf; \
		echo "encrypt_key = yes" 		>> /tmp/opsiconfd.cnf; \
		echo "distinguished_name = req_dn" 	>> /tmp/opsiconfd.cnf; \
		echo "x509_extensions = cert_type" 	>> /tmp/opsiconfd.cnf; \
		echo "prompt = no" 			>> /tmp/opsiconfd.cnf; \
		echo "" 				>> /tmp/opsiconfd.cnf; \
		echo "[ req_dn ]" 			>> /tmp/opsiconfd.cnf; \
		echo "C=DE"				>> /tmp/opsiconfd.cnf; \
		echo "ST=RP" 				>> /tmp/opsiconfd.cnf; \
		echo "L=Mainz" 				>> /tmp/opsiconfd.cnf; \
		echo "O=uib GmbH" 			>> /tmp/opsiconfd.cnf; \
		echo "CN=`hostname -f`" 		>> /tmp/opsiconfd.cnf; \
		echo "emailAddress=root@loclahost"	>> /tmp/opsiconfd.cnf; \
		echo "" 				>> /tmp/opsiconfd.cnf; \
		echo "[ cert_type ]" 			>> /tmp/opsiconfd.cnf; \
		echo "nsCertType = server" 		>> /tmp/opsiconfd.cnf; \
		dd if=/dev/urandom of=/tmp/opsiconfd.rand count=1 2>/dev/null; \
		openssl req -new -x509 -days 1000 -nodes \
			-config /tmp/opsiconfd.cnf -out ${PREFIX}/etc/opsi/opsiconfd.pem -keyout ${PREFIX}/etc/opsi/opsiconfd.pem; \
		openssl gendh -rand /tmp/opsiconfd.rand 512 >> ${PREFIX}/etc/opsi/opsiconfd.pem; \
		openssl x509 -subject -dates -fingerprint -noout -in ${PREFIX}/etc/opsi/opsiconfd.pem; \
		rm -f /tmp/opsiconfd.rand /tmp/opsiconfd.cnf; \
		${CHMOD} 600 ${PREFIX}/etc/opsi/opsiconfd.pem; \
	fi

	#chown opsiconfd:opsiadmin ${PREFIX}/etc/opsi/opsiconfd.pem || true
	@if [ ! -e ${PREFIX}/etc/opsi/backendManager/dispatch.conf ]; then \
		${ECHO_CMD} "Using default dispatch.conf.."; \
		${CP} ${PREFIX}/etc/opsi/backendManager/dispatch.conf.default ${PREFIX}/etc/opsi/backendManager/dispatch.conf; \
	fi
	@if [ ! -e ${PREFIX}/etc/opsi/backendManager/acl.conf ]; then \
		${ECHO_CMD} "Using default acl.conf.."; \
		${CP} ${PREFIX}/etc/opsi/backendManager/acl.conf.default ${PREFIX}/etc/opsi/backendManager/acl.conf; \
	fi

.include <bsd.port.mk>
