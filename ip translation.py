#!/usr/bin/env python
import ipaddress as ip

CLASS_C_ADDR = input("Masukan IP yang akan Digunakan : ")

if __name__ == '__main__':
    not_configed = True
    while not_configed:
        prefix = input("Masukan Prefix yang diinginkan (24-30): ")
        prefix = int(prefix)
        if prefix not in range(23, 31):
            raise Exception("Prefix harus berada antara 24-30")
        net_addr = CLASS_C_ADDR + '/' + str(prefix)
        print("Network menggunakan IP :%s " %net_addr)
        try:
            network = ip.ip_network(net_addr)
        except:
            raise Exception("Gagal untuk membuat objek")
        print("Prefix ini memberikan %s IP address pada setiap Subnet" %(network.num_addresses))
        print("Konfigurasi Jaringan Menghasilkan")
        print("\t network address: %s" %str(network.network_address))
        print("\t netmask: %s" %str(network.netmask))
        print("\t broadcast address: %s" %str(network.broadcast_address))
        first_ip, last_ip = list(network.hosts())[0], list(network.hosts())[-1] 
        print("\t host IP addresses: from %s to %s" %(first_ip, last_ip))
        ok = input("Apakah konfigurasi ini sudah tepat [y/n]? ")
        ok = ok.lower()
        if ok.strip() == 'y':
            not_configed = False
