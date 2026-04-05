# Title       : It's Oops PM
## Difficulty  : Very Easy
## Points      : 850

### With the location of the underground bunker secured, the crew embarks on the next phase of their plan: assessing the feasibility of creating an underground tunnel to bypass the super mutant camp. They secure samples of water, soil, and air near the area. Scouring the wasteland for salvageable equipment, they stumble upon a dilapidated research facility where they find a cache of environmental sensors. Examining these sensors, the crew discovers they communicate with a satellite and contain a crypto-processor that encrypts their transmissions. After hand-drawing the diagrams and emulating the silicon chip's logic with VHDL, they uncover what appears to be a backdoor in the embedded logic that only triggers when a specific input is given to the system. Determined to exploit this, they turn to their tech specialist. Can you connect to the satellite and activate it?

## Requirements
1. Spawn Docker, You will get IP and Port
2. Download the Scenario Files

## Solutions
1. Scan the IP address with nmap; sudo nmap -sS IP
2. You will notice that 2 port open (i got port 31038 and 31337)
3. Then connect with NetCat; nc IP PORT
4. You will get the output 
```
The input must be a binary signal of 16 bits

Input   : 
```
5. Open backdoor.vhdl
6. You see there's binary code in line 13 (i got 1111111111101001)
7. If you input the binary, you will get output:
```
Input   : 1111111111101001
Output  : 0110001111100001

You triggered the backdoor here is the flag: HBT{flag}
```

## Flag
HTB{4_7yp1c41_53cu23_TPM_ch1p}