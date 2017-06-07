PORTNAME=	wimlib
PORTVERSION=	1.11.0
CATEGORIES=	ftp
MASTER_SITES=	https://wimlib.net/downloads/

COMMENT=	the open source Windows Imaging (WIM) library

LIB_DEPENDS=	libxml2.so:textproc/libxml2
BUILD_DEPENDS=	fusefs-ntfs>2016.7.28:sysutils/fusefs-ntfs

USE_PACKAGE_DEPENDS=yes

USES=		gmake pkgconfig
GNU_CONFIGURE=  yes

.include <bsd.port.mk>
