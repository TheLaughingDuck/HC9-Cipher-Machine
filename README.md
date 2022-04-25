# HC9-Cipher-Machine
The HC-9 is a portable cipher machine developed by AB Transvertex in the 1950's. In this repository I will build a python script that simulates the machines encyption mechanism.


## Usage
1) Run KryappClass.py either from the document itself or after importing it somewhere.

2) Create an instance of the Machine.
    Choose a name(example: "Mach1") and create the instance with the following command:
    
        Mach1 = Machine()

3) Configure the keys by doing one of the following:

    a) accept the preset keys (do nothing).
    
    b) Randomly generate new keys with the command:

        Mach1.random_key()

    c) Manually set keys yourself.
        First put the two inner keys in a textdocument (example: "inner_keys.txt") Make sure that it is properly formatted. Then choose an outer key (example: "SECRE")  Then call the following commands:
        
        Mach1.set_inner_keys("inner_keys.txt")
        Mach1.Rotor = convert("SECRE")

4) Encrypt a new message (example "HOWDOYOUDO") with the following command:
    
        Mach1.Encrypt("HOWDOYOUDO")

    When encrypting a new message, please note that the machine remembers the new rotor positions. Set a new inner key (example: "CALIB") for every new message using the command:

        Mach1.Rotor = convert("CALIB")
