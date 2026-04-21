# Title       : Critical Flight
## Difficulty  : Very Easy
## Points      : 900

### Your team has assigned you to a mission to investigate the production files of Printed Circuit Boards for irregularities. This is in response to the deployment of nonfunctional DIY drones that keep falling out of the sky. The team had used a slightly modified version of an open-source flight controller in order to save time, but it appears that someone had sabotaged the design before production. Can you help identify any suspicious alterations made to the boards?

## Requirements
1. Download the Scenario Files
2. Install Kicad 10.0

## Solutions
1. Open Kicad Applications then click gerber viewer
2. Click on file then choose Open Gerber Plot File(s)
3. Choose all file in flight_control_board
4. On the right side, Uncheck all of the layer except HadesMicro-B_Cu.gbr and HadesMicro-ln1_Cu.gbr
5. Arrange the flag and you got it!

## Flag
HTB{533_7h3_1nn32_w02k1n95_0f_313c720n1c5#$@}