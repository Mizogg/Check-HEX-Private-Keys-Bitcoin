# hexmk.py Make a list of privatekeys in HEX format. 20/06/2021
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
from bit import *
from bit.format import bytes_to_wif
import atexit
from time import time
from datetime import timedelta, datetime
import random
import multiprocessing

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")

print(colour_cyan + "\hexmk.py---" + colour_red + "---------mizogg.co.uk---------" + colour_cyan + "---hexmk.py"  + colour_reset)


x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336


def spawn():
    count=1
    total=0
    while True: 
        C=Key.from_int(random.randint(x,y)) 
        C1=Key.from_int(random.randint(x+1,y))
        C2=Key.from_int(random.randint(x+2,y))  
        C3=Key.from_int(random.randint(x+3,y))
        C4=Key.from_int(random.randint(x+4,y))
        C5=Key.from_int(random.randint(x+5,y))
        C6=Key.from_int(random.randint(x+6,y))  
        C7=Key.from_int(random.randint(x+7,y))
        C8=Key.from_int(random.randint(x+8,y))
        C9=Key.from_int(random.randint(x+9,y))
        C10=Key.from_int(random.randint(x+10,y))  
        C11=Key.from_int(random.randint(x+11,y))
        C12=Key.from_int(random.randint(x+12,y))
        C13=Key.from_int(random.randint(x+13,y))
        C14=Key.from_int(random.randint(x+14,y))  
        C15=Key.from_int(random.randint(x+15,y))
        C16=Key.from_int(random.randint(x+16,y))
        C17=Key.from_int(random.randint(x+17,y))
        C18=Key.from_int(random.randint(x+18,y))  
        C19=Key.from_int(random.randint(x+19,y))
        C20=Key.from_int(random.randint(x+20,y))
        C21=Key.from_int(random.randint(x+21,y))
        C22=Key.from_int(random.randint(x+22,y))  
        C23=Key.from_int(random.randint(x+23,y))
        C24=Key.from_int(random.randint(x+24,y)) 
        C25=Key.from_int(random.randint(x+25,y))
        C26=Key.from_int(random.randint(x+26,y))  
        C27=Key.from_int(random.randint(x+27,y))
        C28=Key.from_int(random.randint(x+28,y))
        C29=Key.from_int(random.randint(x+29,y))
        C30=Key.from_int(random.randint(x+30,y))  
        C31=Key.from_int(random.randint(x+31,y))
        C32=Key.from_int(random.randint(x+32,y))
        C33=Key.from_int(random.randint(x+33,y))
        C34=Key.from_int(random.randint(x+34,y))  
        C35=Key.from_int(random.randint(x+35,y))
        C36=Key.from_int(random.randint(x+36,y))
        C37=Key.from_int(random.randint(x+37,y))
        C38=Key.from_int(random.randint(x+38,y))  
        C39=Key.from_int(random.randint(x+39,y))
        C40=Key.from_int(random.randint(x+40,y))
        C41=Key.from_int(random.randint(x+41,y))
        C42=Key.from_int(random.randint(x+42,y))  
        C43=Key.from_int(random.randint(x+43,y))
        C44=Key.from_int(random.randint(x+44,y))
        C45=Key.from_int(random.randint(x+45,y))
        C46=Key.from_int(random.randint(x+46,y))  
        C47=Key.from_int(random.randint(x+47,y))
        C48=Key.from_int(random.randint(x+48,y))
        C49=Key.from_int(random.randint(x+49,y))
        C50=Key.from_int(random.randint(x+50,y))
        C51=Key.from_int(random.randint(x+51,y))
        C52=Key.from_int(random.randint(x+52,y))
        C53=Key.from_int(random.randint(x+53,y))
        C54=Key.from_int(random.randint(x+54,y))
        C55=Key.from_int(random.randint(x+55,y))
        C56=Key.from_int(random.randint(x+56,y))
        C57=Key.from_int(random.randint(x+57,y))
        C58=Key.from_int(random.randint(x+58,y))
        C59=Key.from_int(random.randint(x+59,y))
        C60=Key.from_int(random.randint(x+60,y))
        C61=Key.from_int(random.randint(x+61,y))
        C62=Key.from_int(random.randint(x+62,y))
        C63=Key.from_int(random.randint(x+63,y))
        C64=Key.from_int(random.randint(x+64,y))
        count+=1
        total+=65
        f=open("hex.txt","a")
        f.write(C.to_hex()+'\n'+C1.to_hex()+'\n'+C2.to_hex()+'\n'+C3.to_hex()+'\n'+C4.to_hex()+'\n'+C5.to_hex()+'\n'+C6.to_hex()+'\n'+C7.to_hex()+'\n'+C8.to_hex()+'\n'+C9.to_hex()+'\n'+C10.to_hex()+'\n'+C11.to_hex()+'\n'+C12.to_hex()+'\n'+C13.to_hex()+'\n'+C14.to_hex()+'\n'+C15.to_hex()+'\n'+C16.to_hex()+'\n'+C17.to_hex()+'\n'+C18.to_hex()+'\n'+C19.to_hex()+'\n'+C20.to_hex()+'\n'+C21.to_hex()+'\n'+C22.to_hex()+'\n'+C23.to_hex()+'\n'+C24.to_hex()+'\n'+C25.to_hex()+'\n'+C26.to_hex()+'\n'+C27.to_hex()+'\n'+C28.to_hex()+'\n'+C29.to_hex()+'\n'+C30.to_hex()+'\n'+C31.to_hex()+'\n'+C32.to_hex()+'\n'+C33.to_hex()+'\n'+C34.to_hex()+'\n'+C35.to_hex()+'\n'+C36.to_hex()+'\n'+C37.to_hex()+'\n'+C38.to_hex()+'\n'+C39.to_hex()+'\n'+C40.to_hex()+'\n'+C41.to_hex()+'\n'+C42.to_hex()+'\n'+C43.to_hex()+'\n'+C44.to_hex()+'\n'+C45.to_hex()+'\n'+C46.to_hex()+'\n'+C47.to_hex()+'\n'+C48.to_hex()+'\n'+C49.to_hex()+'\n'+C50.to_hex()+'\n'+C51.to_hex()+'\n'+C52.to_hex()+'\n'+C53.to_hex()+'\n'+C54.to_hex()+'\n'+C55.to_hex()+'\n'+C56.to_hex()+'\n'+C57.to_hex()+'\n'+C58.to_hex()+'\n'+C59.to_hex()+'\n'+C60.to_hex()+'\n'+C61.to_hex()+'\n'+C62.to_hex()+'\n'+C63.to_hex()+'\n'+C64.to_hex()+'\n')
        f.close()

        print (colour_green + 'Running Scan : ' + str (count) + '  :  ' + colour_cyan + 'hexmk.py ' + '  :  ' + colour_red + 'Private HEX saved : ' + str (total) + ' : ' + colour_cyan + seconds_to_str(), end='\r' + colour_reset)

if __name__ == '__main__':
  for i in range(1):
    p = multiprocessing.Process(target=spawn)
    p.start()

