from scapy.all import ARP, Ether, srp

def scan_devices(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=False)[0]

    devices = []
    for sent, received in result:
        device = {'ip': received.psrc, 'mac': received.hwsrc}
        devices.append(device)

        # Affiche les informations sur l'appareil sur le terminal
        print(f"IP: {device['ip']}, MAC: {device['mac']}")

    return devices

scan_devices("10.114.0.0/16")

