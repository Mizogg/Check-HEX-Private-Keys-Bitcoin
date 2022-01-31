import secp256k1 as ice
import multiprocessing
from multiprocessing import pool, Event, Process, Queue, Value, cpu_count
import random, codecs, time, sys, smtplib
from time import sleep
from rich.console import Console
gmail_user = 'youremal@gmail.com'
gmail_password = 'yourpassword'
console = Console()
console.clear()

console.print("\n[yellow]💰-----------------💰 HUNT4BITCOIN ICEHEX with Python 💰----------------------💰[/yellow]")
console.print("[yellow]   🤖🤖🤖 Made by Mizogg  🤖🤖🤖[/yellow]")
console.print("[yellow]    🤩 With iceland2k14 secp256k1 https://github.com/iceland2k14/secp256k1  🤩 [/yellow]")
console.print("[yellow]💰-----------------💰 HUNT4BITCOIN  ICEHEX with Python 💰----------------------💰[/yellow]")
console.print("[purple]         ⏳Starting search... Please Wait ⏳[/purple]")

print('Bitcoin Addresses Loading Please Wait: ')
filename ='80000.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)

print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))

with open("hex.txt", "r") as file1:
    line_count1 = 0
    for line in file1:
        line != "\n"
        line_count1 += 1
print('HEX PASSWORD LIST LOADING>>>>')
print('Total HEX  Loaded:', line_count1)

mylist = []


with open('hex.txt', newline='', encoding='utf-8') as f1:
    for line in f1:
        mylist.append(line.strip())

count = 0
total=0
remaining=line_count1
for i in range(0,len(mylist)):
    count += 1
    total+=4
    remaining-=1
    HEX = mylist[i]
    seed = int(HEX, 16)
    wifc = ice.btc_pvk_to_wif(HEX)
    wifu = ice.btc_pvk_to_wif(HEX, False)
    caddr = ice.privatekey_to_address(0, True, int(seed)) #Compressed
    uaddr = ice.privatekey_to_address(0, False, int(seed))  #Uncompressed
    P2SH = ice.privatekey_to_address(1, True, int(seed)) #p2sh
    BECH32 = ice.privatekey_to_address(2, True, int(seed))  #bech32
    #ethaddr = ice.privatekey_to_ETH_address(int(seed)) # ETH Address
    
    if caddr in add or uaddr in add or P2SH in add or BECH32 in add :
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', seed,'\nPrivatekey (hex): ', HEX, '\nPrivatekey Uncompressed: ', wifu, '\nPrivatekey compressed: ', wifc, '\nPublic Address 1 Uncompressed: ', uaddr, '\nPublic Address 1 Compressed: ', caddr, '\nPublic Address 3 P2SH: ', P2SH, '\nPublic Address bc1 BECH32: ', BECH32)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(seed))
        f.write('\nPrivatekey (hex): ' + HEX)
        f.write('\nPrivatekey Uncompressed: ' + wifu)
        f.write('\nPrivatekey compressed: ' + wifc)
        f.write('\nPublic Address 1 Compressed: ' + caddr)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr)
        f.write('\nPublic Address 3 P2SH: ' + P2SH)
        f.write('\nPublic Address bc1 BECH32: ' + BECH32) 
        f.close()

    else:
        print('Scan Number : ', str(count), 'Total Wallets Checked : ', str (total), 'Remaining:  ', str(remaining),  end='\r')
        #print('\nPrivatekey (dec): ', seed,'\nPrivatekey (hex): ', HEX, '\nPrivatekey Uncompressed: ', wifu, '\nPrivatekey compressed: ', wifc, '\nPublic Address 1 Uncompressed: ', uaddr, '\nPublic Address 1 Compressed: ', caddr, '\nPublic Address 3 P2SH: ', P2SH, '\nPublic Address bc1 BECH32: ', BECH32)