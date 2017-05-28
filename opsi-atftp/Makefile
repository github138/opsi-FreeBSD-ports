PORTNAME=	opsi-atftpd
PORTVERSION=	0.7
DISTVERSIONSUFFIX=6
CATEGORIES=	ftp
MASTER_SITES=	https://github.com/opsi-org/opsi-atftpd/archive/
DISTNAME=	${PORTVERSION}.dfsg-${DISTVERSIONSUFFIX}

COMMENT=	Advanced tftp server and client

WRKSRC=		${WRKDIR}/${PORTNAME}-${PORTVERSION}.dfsg-${DISTVERSIONSUFFIX}

USE_RC_SUBR=	atftpd
GNU_CONFIGURE=	yes

PLIST_FILES=	bin/atftp sbin/atftpd man/man1/atftp.1.gz man/man8/atftpd.8.gz

.include <bsd.port.mk>
