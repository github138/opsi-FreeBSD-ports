--- opsiconfd/statistics.py.orig	2017-04-21 13:15:24 UTC
+++ opsiconfd/statistics.py
@@ -44,6 +44,11 @@ try:
 except ImportError:
	objgraph = None

+try:
+	import psutil
+except ImportError:
+	psutil = None
+
 from OPSI.web2 import http, resource
 from OPSI.Logger import Logger
 from OPSI.Types import forceUnicode
@@ -193,9 +198,12 @@ class Statistics(object):
		if cpu > 100:
			cpu = 100

-		with open('/proc/%s/stat' % os.getpid()) as f:
-			data = f.read().split()
-		virtMem = int("%0.0f" % (float(data[22]) / (1024 * 1024)))
+		if psutil:
+			virtMem = int("%0.0f" % (psutil.virtual_memory().total / (1024 * 1024)))
+		else:
+			with open('/proc/%s/stat' % os.getpid()) as f:
+				data = f.read().split()
+			virtMem = int("%0.0f" % (float(data[22]) / (1024 * 1024)))

		return (utime, stime, cpu, virtMem)
