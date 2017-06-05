--- tftp_io.c.orig	2004-02-19 09:30:00.000000000 +0800
+++ tftp_io.c	2010-10-11 13:01:28.000000000 +0800
@@ -103,7 +103,8 @@
      tftphdr.th_block = htons(block_number);
 
      result = sendto(socket, &tftphdr, 4, 0, (struct sockaddr *)sa,
-                     sizeof(*sa));
+		     sizeof(*sa));
+
      if (result < 0)
           return ERR;
      return OK;
@@ -142,7 +143,8 @@
      }
      /* send the buffer */
      result = sendto(socket, buffer, index, 0, (struct sockaddr *)sa,
-                     sizeof(*sa));
+		     sizeof(*sa));
+
      if (result < 0)
           return ERR;
      return OK;
@@ -171,6 +173,7 @@
 
      result = sendto(socket, tftphdr, size, 0, (struct sockaddr *)sa,
                      sizeof(*sa));
+
      if (result < 0)
           return ERR;
      return OK;
@@ -192,7 +195,8 @@
      tftphdr->th_block = htons(block_number);
 
      result = sendto(socket, data, size, 0, (struct sockaddr *)sa,
-                     sizeof(*sa));
+		     sizeof(*sa));
+
      if (result < 0)
           return ERR;
      return OK;
@@ -214,7 +218,6 @@
 
      struct msghdr msg;         /* used to get client's packet info */
      struct cmsghdr *cmsg;
-     struct in_pktinfo *pktinfo;
      struct iovec iov;
      char cbuf[1024];
 
