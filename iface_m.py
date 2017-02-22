import netifaces as ni
def getInterfaceAddress(iface):
        try:
            ni.ifaddresses(iface)
            ip = ni.ifaddresses(iface)[2][0]['addr']
            return ip
        except:
            return "NO IP/IFACE"