import re

def validasi_IP(ip):
    IPV4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    IPV6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

    
    if re.match(IPV4_pattern, ip) and all (0 <= int(part) <= 255 for part in ip.split(".")):
        return "IPV4"
    elif re.match(IPV6_pattern, ip):
        return "IPV6"
    else:
        return "bukan IP address"
    
def cek_ip(N: int, ip_addresses: list) :
    results = []
    for ip in ip_addresses[:N]: 
        results.append(validasi_IP(ip.strip()))
    return results

N = int(input("masukkan jumlah baris inputan teks: "))
input = [input(f"masukkan teks ke-{i+1}: ").strip()for i in range(N)]

for ip in input:
    print(validasi_IP(ip))

