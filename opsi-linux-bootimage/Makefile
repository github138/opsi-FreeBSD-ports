# $FreeBSD$

PORTNAME=	opsi-linux-bootimage
DISTVERSION=	20170508
DISTVERSIONSUFFIX=	1
MASTER_SITES=	http://download.opensuse.org/repositories/home:/uibmz:/opsi:/opsi40/xUbuntu_16.04/
DISTFILES=	${PORTNAME}_${DISTVERSION}-${DISTVERSIONSUFFIX}.tar.gz
CATEGORIES=	misc

WRKSRC=		${WRKDIR}/${PORTNAME}-${DISTVERSION}

NO_BUILD=	yes

MAINTAINER=	m.ehinger@ltur.de
COMMENT=	The opsi linux bootimage is used to run OS-independent tasks over network.

KERNEL_VERSION=4.10.8
MINIROOT_VERSION=20170405

do-install:
	${ECHO_CMD} "# miniroot-version is: ${MINIROOT_VERSION}"
	${ECHO_CMD} "# kernel-version is: ${KERNEL_VERSION}"
	${MKDIR} ${STAGEDIR}/tftpboot/linux/pxelinux.cfg
	${INSTALL_DATA} ${WRKSRC}/syslinux/*.c32 ${STAGEDIR}/tftpboot/linux
	${INSTALL_DATA} ${WRKSRC}/syslinux/pxelinux.0 ${STAGEDIR}/tftpboot/linux
	${INSTALL_DATA} ${WRKSRC}/install* ${STAGEDIR}/tftpboot/linux/pxelinux.cfg
	${INSTALL_DATA} ${WRKSRC}/default.* ${STAGEDIR}/tftpboot/linux/pxelinux.cfg
	${INSTALL_DATA} ${WRKSRC}/miniroot.bz2 ${STAGEDIR}/tftpboot/linux/miniroot-$(MINIROOT_VERSION).bz2
	${INSTALL_DATA} ${WRKSRC}/vmlinuz ${STAGEDIR}/tftpboot/linux/vmlinuz-$(KERNEL_VERSION)
	${INSTALL_DATA} ${WRKSRC}/miniroot-x64.bz2 ${STAGEDIR}/tftpboot/linux/miniroot-x64-$(MINIROOT_VERSION).bz2
	${INSTALL_DATA} ${WRKSRC}/vmlinuz-x64 ${STAGEDIR}/tftpboot/linux/vmlinuz-x64-$(KERNEL_VERSION)
	${INSTALL_DATA} ${WRKSRC}/elilo.* ${STAGEDIR}/tftpboot/linux/pxelinux.cfg
	(cd ${STAGEDIR}/tftpboot/linux && ${LN} -s vmlinuz-${KERNEL_VERSION} install)
	(cd ${STAGEDIR}/tftpboot/linux && ${LN} -s miniroot-${MINIROOT_VERSION}.bz2 miniroot.bz2)
	(cd ${STAGEDIR}/tftpboot/linux && ${LN} -s vmlinuz-x64-${KERNEL_VERSION} install-x64)
	(cd ${STAGEDIR}/tftpboot/linux && ${LN} -s miniroot-x64-${MINIROOT_VERSION}.bz2 miniroot-x64.bz2)
	(cd ${STAGEDIR}/tftpboot/linux && ${LN} -s install-x64x.bz2 install64)
	(cd ${STAGEDIR}/tftpboot/linux/pxelinux.cfg && ${LN} -s default.menu default)

.include <bsd.port.mk>
