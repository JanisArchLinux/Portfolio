#Port Scanner 



import sys
import socket
from datetime import datetime

print("""                                               
    /\               | |   (_)   |  __ \         | |                                      
   /  \   _ __  _   _| |__  _ ___| |__) |__  _ __| |_ ___  ___ __ _ _ __  _ __   ___ _ __ 
  / /\ \ | '_ \| | | | '_ \| / __|  ___/ _ \| '__| __/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
 / ____ \| | | | |_| | |_) | \__ \ |  | (_) | |  | |_\__ \ (_| (_| | | | | | | |  __/ |   
/_/    \_\_| |_|\__,_|_.__/|_|___/_|   \___/|_|   \__|___/\___\__,_|_| |_|_| |_|\___|_|""")




target = input(str("Target IP :"))

#Banner
print("_" * 50)
print("Scanning Target" + target)
print("Scaning started at : " + str(datetime.now()))

try:

    for port in range(1,200):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #return open port

        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
            s.close()
except KeyboardInterrupt:
    print("Exiting")
    sys.exit()

except socket.error:
    print("Host not responding")
    sys.exit()

