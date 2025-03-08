"""
    @ code by ---( Tabbu Arain )---
    @ Github : https://github.com/Tabbu-Arain
    @ WhatsApp : https://wa.me/994402197773
    @ facebook : https://www.facebook.com/TabbuArain
    
"""
import os, sys,time, platform
os.system('clear') 
print('\033[0m [💸] \033[92mFollow Me On Facebook For More Updates And Tricks 🥰✨') 
time.sleep(3)
os.system('xdg-open https://www.facebook.com/TabbuArain')
print('\n\033[0m [\033[92m✓\033[97m] \033[92m Checking For Updates ....\n') 

bit = platform.architecture()[0]
if bit == '64bit':
    import Safeum
elif bit == '32bit':
    print("\033[0m\033[91m Sorry Your Device Is 32bit, This Tool Does Not Support 32Bit, Only For \033[92m64Bit\033[0m ]");exit() 
 
