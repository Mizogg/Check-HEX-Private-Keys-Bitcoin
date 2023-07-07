import secp256k1 as ice
mizogg= '''
                          ___            ___
                         (o o)          (o o)
                        (  V  ) MIZOGG (  V  )
                        --m-m------------m-m--
                      © mizogg.co.uk 2018 - 2023
                           HEX_KEY_CHECK.py

                            PROJECT Mizogg
    '''
print(mizogg)
def save_progress(filename, pvk, addr):
    with open(filename, 'a') as file:
        file.write(f'Address = {addr}\nPrivate Key = {pvk}\n')

def generate_addresses(dec):
    caddr = ice.privatekey_to_address(0, True, dec)
    uaddr = ice.privatekey_to_address(0, False, dec)
    p2sh = ice.privatekey_to_address(1, True, dec)
    bech32 = ice.privatekey_to_address(2, True, dec)
    ethaddr = ice.privatekey_to_ETH_address(dec)
    return caddr, uaddr, p2sh, bech32, ethaddr

BUFFER_SIZE = 8192

def read_file_chunks(file):
    while True:
        data = file.read(BUFFER_SIZE)
        if not data:
            break
        yield data
        
def main(line_count, addfind):
    c = 0
    i = 0
    line_10 = 10000
    with open('hex.txt', 'rb') as f:
        for chunk in read_file_chunks(f):
            lines = chunk.split(b'\n')
            for line in lines:
                if line_10 == i:
                    line_10 += 10000
                text = line.strip().decode('utf-8')
                pvk = text
                dec = int(pvk, 16)
                HEX = "%064x" % dec
                caddr, uaddr, p2sh, bech32, ethaddr = generate_addresses(dec)
                print("pvk:                    ", text)
                print("BTC p2pkh comp:         ", caddr)
                print("BTC p2pkh uncomp:       ", uaddr)
                print("BTC p2sh:               ", p2sh)
                print("BTC bech32:             ", bech32)
                print("ETH:                    ", ethaddr)
                print()
                c += 1
                i += 1
                if caddr in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("BTC p2pkh comp:         ", caddr)
                    print()
                    save_progress('found.txt', HEX, caddr)
                if uaddr in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("BTC p2pkh uncomp:         ", uaddr)
                    print()
                    save_progress('found.txt', HEX, uaddr)
                if p2sh in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("BTC p2sh:               ", p2sh)
                    print()
                    save_progress('found.txt', HEX, p2sh)
                if bech32 in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("BTC bech32:             ", bech32)
                    print()
                    save_progress('found.txt', HEX, bech32)
                if ethaddr[2:] in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("ETH:                    ", ethaddr)
                    print()
                    save_progress('found.txt', HEX, ethaddr)

def main1(line_count, addfind):
    c = 0
    i = 0
    line_10 = 10000
    with open('hex.txt', 'rb') as f:
        for chunk in read_file_chunks(f):
            lines = chunk.split(b'\n')
            for line in lines:
                if line_10 == i:
                    line_10 += 10000
                text = line.strip().decode('utf-8')
                pvk = text
                dec = int(pvk, 16)
                HEX = "%064x" % dec
                caddr, uaddr, p2sh, bech32, ethaddr = generate_addresses(dec)
                print("Cheking BTC, ETH [" + str(line_10) + ']', end='\r')
                c += 1
                i += 1
                if caddr in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("BTC p2pkh comp:         ", caddr)
                    print()
                    save_progress('found.txt', HEX, caddr)
                if uaddr in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("BTC p2pkh uncomp:         ", uaddr)
                    print()
                    save_progress('found.txt', HEX, uaddr)
                if p2sh in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("BTC p2sh:               ", p2sh)
                    print()
                    save_progress('found.txt', HEX, p2sh)
                if bech32 in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("BTC bech32:             ", bech32)
                    print()
                    save_progress('found.txt', HEX, bech32)
                if ethaddr[2:] in addfind:
                    print("          FOUND          ")
                    print("pvk:                    ", text)
                    print("ETH:                    ", ethaddr)
                    print()
                    save_progress('found.txt', HEX, ethaddr)
           

if __name__ == '__main__':     
    addfind = str(input("\n Address to find BTC or ETH =  "))
    with open("hex.txt", "r") as file:
        line_count = 0
        for line in file:
            line != "\n"
            line_count += 1
    display_input = int(input("\n1 - Print only count(fast); \n2 - Print all(slow) \nChoose format and display print: "))
    if display_input == 1:
        main1(line_count, addfind)
        pass
    elif display_input == 2:
        main(line_count, addfind)
        pass              
    else:
        print("ERROR!!! Starting with fast")
        main1(line_count, addfind)
        pass
        