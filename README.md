<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/S2PS2.png" width=60% height=60%>

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
<img src="https://github.com/GorGylka/Server2PS2/blob/main/readme_stuff/pico_mini_eth.jpg" width=40% height=40%> 
✅² = Requires Type-C OTG adapter & external 5V power  
❓= Not tested yet   

Building:
- git clone https://github.com/LuckfoxTECH/luckfox-pico
- Merge with my files
- i dont know how to copy hidden files correctly, you need to rename 2 config files as .config
