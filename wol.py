import sys
import socket

def macbytes(mac):
  ret = mac.replace(":", "");
  ret = ret.replace("-", "");
  return ret.lower().decode("hex")

port = 9
args = sys.argv
if len(args) != 3:
  print """
  Sends a WOL "magic packet" to a broadcast address

  Usage: python wol.py <broadcast-ip> <mac-address>
  Example: python wol.py 192.168.0.255 00:0D:61:08:22:4A
  """
else:
  addr = args[1]
  mac = args[2]

  soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  soc.sendto("\xff"*6 + macbytes(mac)*16, (addr, port))

  print "Magic packet sent."
