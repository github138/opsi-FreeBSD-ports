PORTNAME=	wimlib
PORTVERSION=	1.11.0
CATEGORIES=	ftp
MASTER_SITES=	https://wimlib.net/downloads/

COMMENT=	the open source Windows Imaging (WIM) library

LIB_DEPENDS=	libxml2.so:textproc/libxml2 \
		libntfs-3g.so:sysutils/fusefs-ntfs

USES=		gmake
GNU_CONFIGURE=  yes

#WRKSRC=		${WRKDIR}/${PORTNAME}-${PORTVERSION}.dfsg-${DISTVERSIONSUFFIX}

pre-fetch:
	@${ECHO_CMD}
	@${ECHO_CMD} "Please make sure fusefs-ntfs > 2016.7.28 is used!"
	@${ECHO_CMD}
	@sleep 5

.include <bsd.port.mk>
