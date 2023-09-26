![20230606_194919](https://github.com/martinmmi/redtally_docs/assets/118231543/41d16b50-8dd0-446e-b311-2db1340b968b)

# Welcome to official redtally support

## Introduction
Here you will find my official support for redtally. I develooped it durring and after my work at the east-german television crew durring my masters.
Its a small device where you can transmit tallys over long range via loraWAN-Technology. The Interfaces of this device are supported by relay closing contact and via TSL. For TSL, unconfortly supported controllers are the ross carbonite series. I planed to implement more interfaces, if the demand is there. 

## Applications und Use-cases for the device
If you have a situation, where the production depends from a wireless connectivity, that solution is a perfect compromises between availability, independence and technical accuracy. A usesample is to use the redtally solution for a undended drone operator.

![image](https://github.com/martinmmi/redtally_docs/assets/118231543/e6170ac3-c57e-4a25-af0b-8f77c0a12d58)


## Technical Aspects
### Hardware
For the project i used to different microcontroller for it. The LilyGO-T-ETH-POE on the left site for the basestation and the LilyGO-LORA32 V2.1 one the right site for the tally-recipints. 
![image](https://github.com/martinmmi/redtally_docs/assets/118231543/43e292a9-aa7e-4fd7-8a1d-74053a3c38d3)
For everything i designed und printed a 3d-case for a perfect use. Its only possible to use max. 4 recipints at the same time. You can turn it on with a switch on the left site. The reset button is only to clear the EEPROM / the lora-transmission settings. The basestation is powered via a usb-c cable or easy via PoE (IEEE 802.3af). 

### Software
For a maximum useage I implement few different functions on a webserver. You can access to them via the ip-adress on the display of the basestation. Make sure that the local ip-parameters in your network fit with the redtally solution. If there are in the same network, you have the access to follow functions:
- overview of connected tallys
- input mode of gpio or tsl
- assigment of channels
- energy save mode
- discover time
- lora transmission values
- user credentials
- network operation mode (dhcp or manual)
- static ip configuration
- wlan and wlan credentials
- tsl application port
- tsl-udp diagramm support
- post authenification via sha-keying

### Communication Pattern
![image](https://github.com/martinmmi/redtally_docs/assets/118231543/c72ac58c-95e3-4d46-8063-0e43385acab2)

![image](https://github.com/martinmmi/redtally_docs/assets/118231543/eb5f3abf-4db6-4825-ad8c-441ccd8c2efd)



## Throubleshooting
*The device didnt starts.* Are you shure that the accumulator is already charged?




