import random

from tqdm import tqdm

import time 





print("""
   ___             __   _       ___                                 __  _____                      __          
  / _ | ___  __ __/ /  (_)__   / _ \___ ____ ____    _____  _______/ / / ___/__ ___  ___ _______ _/ /____  ____
 / __ |/ _ \/ // / _ \/ (_-<  / ___/ _ `(_-<(_-< |/|/ / _ \/ __/ _  / / (_ / -_) _ \/ -_) __/ _ `/ __/ _ \/ __/
/_/ |_/_//_/\_,_/_.__/_/___/ /_/   \_,_/___/___/__,__/\___/_/  \_,_/  \___/\__/_//_/\__/_/  \_,_/\__/\___/_/   
                                                                                                              

                                                                                                                               






 """)




lower_letters = "abcdefghijklmnopqrstuvwüäöéàè"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "*"



all = lower_letters + upper_letters + numbers + symbols


length = int(input("Password length : "))



for i in tqdm(range(10)):
    time.sleep(0.5)





# password generating variable

password = "".join(random.sample(all, length))

print() 
print() 
print("Generated Password : " + password)
print() 
print()
print() 
print()
exit_Script = input("If you like to exit type Y")
if exit_Script == "Y":
    exit()

