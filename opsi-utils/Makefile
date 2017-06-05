# $FreeBSD$

PORTNAME=	opsi-utils
DISTVERSION=	4.0.7.15
DISTVERSIONSUFFIX=	1
MASTER_SITES=	https://github.com/opsi-org/${PORTNAME}/archive/
DISTNAME=	${DISTVERSION}-${DISTVERSIONSUFFIX}
CATEGORIES=	sysutils

WRKSRC=		${WRKDIR}/${PORTNAME}-${DISTNAME}

NO_BUILD=	yes

USES=	shebangfix gettext python
SHEBANG_FILES=	opsi-* build_manpages.sh

BUILD_DEPENDS=	bash:shells/bash \
		asciidoc:textproc/asciidoc

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}python-opsi>0:${.CURDIR}/../py-python-opsi \
		zsync:net/zsync \
		bash:shells/bash

SUB_FILES=	opsi-utils.conf
#PLIST_FILES=	"${PREFIX}/etc/newsyslog.d/opsi-utils.conf" \
#		"@sample ${PREFIX}/etc/opsi/opsi-product-updater.conf"

USE_PACKAGE_DEPENDS=yes

MAINTAINER=	m.ehinger@ltur.de
COMMENT=	This package contains the opsi util collection.

post-extract:
	${REINPLACE_CMD} -e "s|'/usr/|'${PREFIX}/|g" ${WRKSRC}/opsi-*
	${REINPLACE_CMD} -e "s|'/etc/|'${PREFIX}/etc/|g" ${WRKSRC}/opsi-*

do-install:
	${RM}  ${WRKSRC}/opsi-*.bak
	${MKDIR} ${STAGEDIR}${PREFIX}/bin
	${INSTALL_SCRIPT} ${WRKSRC}/opsi-* ${STAGEDIR}${PREFIX}/bin	

	${MKDIR} ${STAGEDIR}${PREFIX}/etc/opsi
	${INSTALL_DATA} ${WRKSRC}/data/opsi-product-updater.conf ${STAGEDIR}${PREFIX}/etc/opsi/opsi-product-updater.conf.sample

	@${ECHO_CMD} "Compiling man pages.."
	cd ${WRKSRC}/ && ${SH} ./build_manpages.sh
	@${ECHO_CMD} "Installing man pages.."
	${INSTALL_MAN} ${WRKSRC}/manpages/compiled/*.1.gz ${STAGEDIR}${MANPREFIX}/man/man1/

	${INSTALL_DATA} ${WRKDIR}/opsi-utils.conf ${STAGEDIR}${PREFIX}/etc/newsyslog.conf.d/

do-install-NLS-on:
.for x in da de es fr ru
	msgfmt -o $RPM_BUILD_ROOT/usr/share/locale/${x}/LC_MESSAGES/opsi-utils.mo gettext/opsi-utils_.po
	@${MKDIR} ${WRKSRC}/gettext/${x}
	${LOCALBASE}/bin/msgfmt -c ${WRKSRC}/gettext/opsi-utils_${x}.po \
		-o ${WRKSRC}/gettext/${x}/${PORTNAME}.mo
	${INSTALL_DATA} ${WRKSRC}/gettext/${x}/*.mo \
		${STAGEDIR}${PREFIX}/share/locale/${x}/LC_MESSAGES/
.endfor


.include <bsd.port.mk>
