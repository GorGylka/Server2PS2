WORK IN PROGRESS  

<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/S2PS2.png" width=50% height=50%>

<h2 align="left">Server2PS2 - Universal PS2 server</h2>

<h3 align="left">Features:</h3>  

- SMB / UDPBD / UDPFS support 
- exFAT 
- MicroSD / USB
- Rapid 12sec. bootup
- Easy installation & clear interface

<h3 align="left">Compatibility</h3>  

| Device | Support | SD | USB | Photo |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Luckfox Pico Mini B | ✅¹ | ✅  | ✅² | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_mini_b.jpg" width=20% height=20%> |
| Luckfox Pico Mini A | ❓¹ | ❌ | ✅² | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_mini_a.jpg" width=20% height=20%> |
| Luckfox Pico Plus | ✅ | ✅ | ✅² | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_plus.jpg" width=40% height=40%> |
| Luckfox Pico WebBee | ✅ | ✅ | ❌ | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_webbee.jpg" width=40% height=40%> |
| rv1103 based P4 PPPwn Dongles | ❓ | ❓ | ✅² | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_pppwn.jpg" width=40% height=40%> |

✅¹ = Requires LAN cable solder  
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_mini_eth.jpg" width=30% height=30%>  
✅² = Requires Type-C OTG adapter / Type-C USB Drive & external 5V power  
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_mini_otg.jpg" width=50% height=50%>  
❓= Not tested yet   

<h2 align="left">MicroSD / USB preparations:</h2>

-Format USB to GUID Partition Table (GPT), exFat, Standart Cluster Size  
(I recommend using [Rufus](https://rufus.ie) than Windows formatting)  
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/format.jpg"> 

-Do standart USB config for PS2 (create CD/DVD folders, add backups, ARTs, e.t.c.)

<h2 align="left">Installation:</h2>  

- Install Drivers [click here to download](https://files.luckfox.com/wiki/Omni3576/TOOLS/DriverAssitant_v5.13.zip).
  
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/driver.jpg">

- download and unzip latest [FW image](https://github.com/GorGylka/Server2PS2/releases)

- Download and extract the SocToolKit flashing tool[Click here to download](https://files.luckfox.com/wiki/Luckfox-Pico/Software/SocToolKit_v1.98_20240705_01_win.zip).

- Run SocToolKit, Then flash FW as shown

<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/flashing.jpg">

- After flashing, disconnect the USB cable. Server side is done!

  <h2 align="left">Configuration:</h2>  

- To get to router config page, you will need to set Static IP
- Connect power to server, LAN cable, Set as shown:
  
| IP | 192.168.1.10 |
| ------------- | ------------- |
| NetMask | 255.255.255.0 |
| Gateway | 192.168.1.1 |  



  <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/netconfig.jpg">

- go to (http://192.168.1.1/cgi-bin/index.cgi) or (http://192.168.1.1)

<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/menu.jpg" width=75% height=75%>

- Check that drives are detected by server, then select the server mode and we're ready to go.

<h2 align="left">PS2 Config:</h2>

<h3 align="left">SMB</h3>  
- Soon

<h3 align="left">UDPBD</h3>  
Soon
<h3 align="left">UDPFS</h3>  
Soon
<h2 align="left">Building</h2>  

- git clone https://github.com/LuckfoxTECH/luckfox-pico   
- Merge with my files   
- i dont know how to copy hidden files correctly, you need to rename 2 config files as .config  
