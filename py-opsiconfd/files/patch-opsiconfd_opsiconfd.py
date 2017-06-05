--- opsiconfd/opsiconfd.py.orig	2017-06-01 08:26:58 UTC
+++ opsiconfd/opsiconfd.py
@@ -48,10 +48,19 @@ except ImportError:
 from contextlib import contextmanager
 from datetime import datetime
 from signal import signal, SIGHUP, SIGINT, SIGTERM
+import ctypes
 from ctypes import CDLL

-from twisted.internet import epollreactor
-epollreactor.install()
+import platform
+
+if platform.system().lower().endswith('bsd'):
+	from twisted.internet.interfaces import IReactorDaemonize
+	from twisted.internet import kqreactor
+	kqreactor.install()
+else:
+	from twisted.internet import epollreactor
+	epollreactor.install()
+
 from twisted.internet import reactor

 from OPSI.Application import Application
@@ -551,12 +560,23 @@ class OpsiconfdInit(Application):
		signal(SIGHUP, self.signalHandler)

		if self.config['daemon']:
+			if IReactorDaemonize.providedBy(reactor):
+				reactor.beforeDaemonize()
+
			daemonize()
			time.sleep(2)

+			if IReactorDaemonize.providedBy(reactor):
+				reactor.afterDaemonize()
+
		self.createPidFile()
-		libc = CDLL("libc.so.6")
-		libc.prctl(15, 'opsiconfd', 0, 0, 0)
+
+		if platform.system().lower().endswith('bsd'):
+			libc = CDLL(ctypes.util.find_library("c"))
+			libc.setproctitle('opsiconfd')
+		else:
+			libc = CDLL("libc.so.6")
+			libc.prctl(15, 'opsiconfd', 0, 0, 0)

	def shutdown(self):
		self.removePidFile()
