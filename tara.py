import os
pkirmizi= '\033[91m'
pyesil = '\033[92m'
pmavi = '\033[96m'#p --> parlak
print(pmavi)
os.system("ifconfig")
print(pyesil+"Baglandiginiz cihazin ip adresini giriniz:")
ip =str(raw_input())
while True:
    print(pkirmizi)
    #os.system("clear")
    os.system("nmap -sn "+str(ip)+"/24")
