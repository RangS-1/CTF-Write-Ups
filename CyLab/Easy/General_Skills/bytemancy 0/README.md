# CyLab CTF
<hr>

## Title: bytemancy 0
## Type: General Skill

### Description
Can you conjure the right bytes? The program's source code can be downloaded<a href="https://challenge-files.picoctf.net/c_candy_mountain/a32ca0e42d9494e3cf81e345699e8ae50415274c00871b1e8594d0fa0ce7078c/app.py">here</a>.

### Solution
1. Launch Instance and you will see detail:
```
Connect to the program with netcat:
$ nc candy-mountain.picoctf.net 54491
```
2. Open WebShell
3. Connect using NetCat ; nc address-you-got.picoctf.net PORT
4. After you enter, you will get prompt:
```
⊹──────[ BYTEMANCY-0 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==>
```
5. You must understand that ASCII Decimal of 101 is "e". If you didn't know, you can check the Ascii-Table.png. 
6. So, enter "eee" three times
```
==> eee
```
7. After that, you will get the flag that you can submit

### Flag
picoCTF{pr1n74813_ch4r5_62360bfd}