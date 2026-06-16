<h2 align="center">Server2PS2 - Universal PS2 server</h2>  

<h3 align="center"> A worthy alternative to the PS2 FAT IDE and complex PS2 70000 IDE mods  </h3>  

<p align="center">
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/S2PS2.png" width=40% height=40%>
</p>  

<h3 align="left">Features:</h3>  

- ```SMB``` / ```UDPBD``` / ```UDPFS``` support 
- ```exFAT``` 
- ```MicroSD``` / ```USB```
- Rapid ⏱️ 12sec. bootup
- Easy setup & clear interface
- Based on accessible, cheap hardware

<h3 align="left">Benchmarks:</h3>  

Device             | PS2 model  | Speed                                                                            
-------------------|------------|----------------------------------------------------------------------------------
USB                | FAT + SLIM 70000  |![x](https://progress-bar.xyz/750?scale=2200&suffix=KB/s&&progress_color=d9534f)  
USB                | SLIM       |![x](https://progress-bar.xyz/900?scale=2200&suffix=KB/s)                         
MX4SIO             | SLIM       |![x](https://progress-bar.xyz/1150?scale=2200&suffix=KB/s)                        
MMCE               | SLIM       |![x](https://progress-bar.xyz/1350?scale=2200&suffix=KB/s)                        
MX4SIO             | FAT + SLIM 70000  |![x](https://progress-bar.xyz/1500?scale=2200&suffix=KB/s)                        
MMCE               | FAT + SLIM 70000  |![x](https://progress-bar.xyz/1700?scale=2200&suffix=KB/s&&progress_color=9ead5a)                        
SMB ⭐               | ALL        |![x](https://progress-bar.xyz/2200?scale=2500&suffix=KB/s&&progress_color=85ad5b)                             
DVD (Target) ✔️| ALL        |![x](https://progress-bar.xyz/3500?scale=2200&suffix=KB/s)                        
UDPFS ⭐             | ALL        |![x](https://progress-bar.xyz/5200?scale=2200&suffix=KB/s)                        
UDPBD ⭐             | ALL        |![x](https://progress-bar.xyz/9400?scale=2200&suffix=KB/s)                        
IDE HDD            | FAT        |![x](https://progress-bar.xyz/21000?scale=2200&suffix=KB/s)                        

<h3 align="left">Compatibility</h3>  

| Device | Support | SD | USB | Photo |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Luckfox Pico Mini B | ✅¹ | ✅  | ✅² | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_mini_b.jpg" width=20% height=20%> |
| Luckfox Pico Mini A | ❓¹ | ❌ | ✅² | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_mini_a.jpg" width=20% height=20%> |
| Luckfox Pico | ❓¹ | ✅ | ✅² | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_orig.jpg" width=40% height=40%> |
| Luckfox Pico Plus | ✅ | ✅ | ✅² | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_plus.jpg" width=40% height=40%> |
| Luckfox Pico WebBee | ✅ | ✅ | ❌ | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_webbee.jpg" width=40% height=40%> |
| rv1103 based P4 PPPwn Dongles | ✅ | ❌ | ✅² | <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_pppwn.jpg" width=40% height=40%> |

❓= Not tested yet   
✅¹ = Requires LAN cable solder  
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_mini_eth.jpg" width=30% height=30%>  
✅² = Requires Type-C OTG adapter / Type-C USB Drive & external 5V power  
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_mini_otg.jpg" width=50% height=50%>  
For P4 Dongle:  
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/p4.jpg" width=50% height=50%>  
Alternative design:  
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/p4v1.jpg" width=50% height=50%>  


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

- Plug Luckfox while holding BOOT, Run SocToolKit, flash FW as shown

<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/flashing.jpg">

- After flashing, disconnect the USB cable. Server side is done!

<h2 align="left">Configuration:</h2>  

<h3 align="left">Simplified setup:</h3>  

On the Luckfox Pico (depending on the model) there are 2 LEDs: ACT and USER  
Blinking of USER LED = server has started, number of blinks indicates server type.  
(Default is SMB SD)  

| LED | Action | Server Type |
| ------------- | ------------- | ------------- |
| 1 Blink | 🔴 | SMB SD |
| 2 Blinks | 🔴🔴 | SMB USB |
| 3 Blinks | 🔴🔴🔴 | UDPBD SD |
| 4 Blinks | 🔴🔴🔴🔴 | UDPBD USB |
| 5 Blinks | 🔴🔴🔴🔴🔴 | UDPFS SD |
| 6 Blinks | 🔴🔴🔴🔴🔴🔴 | UDPFS USB |

After starting, you can cycle through the modes by pressing the ```BOOT``` button  

<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/mode_select.gif">

<h3 align="left">Manual setup:</h3> 

- To get to router config page, you will need to set Static IP
- Connect power to server, LAN cable, Set as shown:
  
| IP | 192.168.1.10 |
| ------------- | ------------- |
| NetMask | 255.255.255.0 |
| Gateway | 192.168.1.1 |  



  <img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/netconfig.jpg">

- go to (http://192.168.1.1/cgi-bin/index.cgi) or (http://192.168.1.1)

<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/menu2.jpg" width=75% height=75%>

- Check that drives are detected by server, then select the server mode.

<h2 align="left">PS2 Config:</h2>

<h3 align="center">Easy Method:</h3>  

<h3 align="left">You will need:</h3>

- FAT32 USB Drive
- 8MB MemoryCard (orig or clone, 64mb and more __not supported__)      
- Ability to run ulaunchELF
- [MemoryCards.zip](https://github.com/GorGylka/Server2PS2/releases/)

-Depending on chosen method place ```FMCBinst(****)``` folder into root FAT32 USB Drive, insert into PS2  
-Run uLaunchELF  
-Run mass:/FMCBinst(****)/FMCBInstaller.elf  
Make sure that the correct MC is inserted into PS2 slot 1, slot 2 is empty  
-Restore MC ( Press ```R1``` ```R1``` ```Down``` ```Down``` ```X``` ), Confirm  
(careful, it will format your MemoryCard)  
-Install FMCB Multi-install ( Press ```L1``` ```L1``` ```Down``` ```X``` ), Confirm  
-Exit, Reboot PS2, Eject USB from PS2  

<h3 align="center">Manual:</h3>  

<h3 align="left">SMB</h3> 

Config in [OPL]( https://github.com/ps2homebrew/Open-PS2-Loader/releases/tag/latest) as a reference:

<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/smb1.jpg" width=50% height=50%>  

<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/smb2.jpg" width=50% height=50%>  


<h3 align="left">UDPBD</h3>  
Soon
<h3 align="left">UDPFS</h3>  
Soon

<h2 align="left">Advanced</h2>  

SSH / SCP: IP ```192.168.1.1``` Login ```root``` Pass: ```luckfox```  
 
<h2 align="left">Building</h2>  

- git clone https://github.com/LuckfoxTECH/luckfox-pico   
- Merge with my files   
- i dont know how to copy hidden files correctly, you need to rename 2 config files as .config  

<h2 align="Center">Big thanks to</h2> 

[Rickgaiser](https://github.com/rickgaiser) , [pcm720](https://github.com/pcm720), [AlSiSan](https://github.com/AlSiSan/) , [Belin02](https://github.com/Belin02) and whole PS2 Community 
