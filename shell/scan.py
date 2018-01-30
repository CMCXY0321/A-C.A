# coding=UTF-8
import socket
import threading

screenLock = threading.Semaphore(value = 1)

def connScan (tgtHost, tgtPort):
  try:
    connSkt = socket.socket(socket.AF_INET,
    socket.SOCK_STREAM)
    connSkt.connect((tgtHost, tgtPort))
    connSkt.send('ViolentPython\r\n')
    results = connSkt.recv(100)
    screenLock.acquire()

    print('[+]%d/tcp open' % tgtPort)
    print('[+] ' + str(results))

  except:
    screenLock.acquire()
    print('[-]%d/tcp closed' % tgtPort)

  finally:
    screenLock.release()
    connSkt.close()

def portScan (tgtHost, tgtPorts):
  try:
    tgtIP = socket.gethostbyname(tgtHost)
  except:
    print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
    return

  try:
    tgtName = socket.gethostbyaddr(tgtIP)
    print('\n[+] Scan Results for:' + tgtName[0])
  except:
    print('\n[+] Scan Results for:' + tgtIP)
    socket.setdefaulttimeout(1)

  for tgtPort in tgtPorts:
    print('Scanning port' + str(tgtPort))
    t = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
    t.start()

portScan("metrics.hemaos.com", [80, 443, 3389, 1433, 23, 445])
