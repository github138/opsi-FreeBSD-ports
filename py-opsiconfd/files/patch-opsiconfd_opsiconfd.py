--- opsiconfd/opsiconfd.py.orig	2017-06-07 19:22:04 UTC
+++ opsiconfd/opsiconfd.py
@@ -48,10 +48,20 @@ except ImportError:
 from contextlib import contextmanager
 from datetime import datetime
 from signal import signal, SIGHUP, SIGINT, SIGTERM
+
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
@@ -551,12 +561,25 @@ class OpsiconfdInit(Application):
 		signal(SIGHUP, self.signalHandler)
 
 		if self.config['daemon']:
+			if platform.system().lower().endswith('bsd'):
+				if IReactorDaemonize.providedBy(reactor):
+					reactor.beforeDaemonize()
+
 			daemonize()
 			time.sleep(2)
 
+			if platform.system().lower().endswith('bsd'):
+				if IReactorDaemonize.providedBy(reactor):
+					reactor.afterDaemonize()
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
@@ -638,7 +661,7 @@ class OpsiconfdInit(Application):
 			if pidFromFile:
 				running = False
 				try:
-					for pid in execute("%s -x opsiconfd" % which("pidof"))[0].strip().split():
+					for pid in execute("%s -f opsiconfd" % which("pgrep"))[0].strip().split():
 						if pid == pidFromFile:
 							running = True
 							break
