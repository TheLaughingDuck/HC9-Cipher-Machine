import random

"For letter and number conversions"
Alphabet = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
Rotor_len = [29, 31, 33, 34, 35]

class Machine:
    def __init__(self, file="inner_key_nr1.txt"):
        #self.set_inner_keys(file)
        pass
    

    def set_inner_keys(self, file):
        "ROTORS"
        self.Rotor = [15, 17, 8, 12, 0] #PRIMA
        
        "READ the default inner keys"
        Inner_key=open(file, "r").read()
        Inner_key = Inner_key.split("\n--------------------------------------\n")
        
        "PUNCHCARD"
        self.Punchcard = Inner_key[0].split("\n") #Becomes a list of 5 long strings of 0's and 1's
        self.Punchcard = [[int(digit) for digit in section] for section in self.Punchcard]
        
        "ALFABETSBLAD"
        #print(Inner_key)
        self.Alfabetsblad = Inner_key[1].replace(" ", "").split("\n") #Remove spaces and split alphabets
        #print(self.Alfabet)
        self.Alfabetsblad = [convert(self.Alfabetsblad[index]) for index in range(16)] #Convert to numbers


    def random_key(self):
        "ROTORS"
        self.Rotor = [random.randint(0,15) for i in range(5)]
        
        "PUNCHCARD"
        self.Punchcard = [[random.randint(0,1) for i in range(Rotor_len[j])] for j in range(5)]
        
        "ALFABETSBLAD"
        self.Alfabetsblad = []
        for i in range(16):
            left_to_assign = [i for i in range(26)]
            new = [None for i in range(26)]
            
            while len(left_to_assign) > 0:
                letter1 = left_to_assign[random.randint(0, len(left_to_assign)-1)]
                letter2 = left_to_assign[random.randint(0, len(left_to_assign)-1)]
                
                if(letter1 == letter2):
                    left_to_assign.remove(letter1)
                    new[letter1] = letter2 #Same
                else:
                    left_to_assign.remove(letter1)
                    left_to_assign.remove(letter2)
                    
                    new[letter1] = letter2
                    new[letter2] = letter1
            
            self.Alfabetsblad.append(new)
    

    def Encrypt(self, plaintext):
        
        plaintext = convert(plaintext)
        ciphertext = []
        
        "Encrypt every letter in plaintext"
        for letter in plaintext:
            "Spin Rotors"
            self.Rotor = [(self.Rotor[i]+1) % Rotor_len[i] for i in range(len(self.Rotor))]
            
            "Punchcard digits"
            binary = [self.Punchcard[i][self.Rotor[i]] for i in range(5)] #List
            #print(binary)
            
            "XOR and conversion - Takes a word list and turns it into a 5 digit binary number"
            xornumber = 0
            for i in range(4):
                #print("comparing", i, "and", i+1)
                if(binary[i] ^ binary[i+1]): #XOR
                    #print("Apparently binary[", i, "] ^ ", "binary[", i+1, "] = 1", sep="")
                    xornumber += 2**(3-i)
            
            xornumber = (16 - xornumber) % 16
            
            ciphertext.append(self.Alfabetsblad[xornumber][letter])
            
        return(convert(ciphertext))


"General Use Functions"

def convert(obj):
    #print(obj)
    if(type(obj) == str):
        obj = [letter for letter in obj]
        output = [Alphabet.index(obj[index]) for index in range(len(obj))]
    
    if(type(obj[0]) == int):
        obj = [number for number in obj]
        output = ""
        for letter in obj:
            output += Alphabet[letter]
    
    return(output)


primt = Machine()