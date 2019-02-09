#!/usr/bin/env python3

import sys, getopt, random, string

def usage():
    print('Usage: a1.py -i <inputfile>')

def create_otp(cipher_len):
    allchars = string.ascii_letters + string.punctuation + string.digits
    return "".join(random.choice(allchars) for x in range(cipher_len))

def xor_cipher(plaintext, key):
    return "".join(chr(ord(a) ^ ord(b)) for a,b in zip(plaintext, key))

def main(argv):
    plaintext = ""

    try:
        opts, args = getopt.getopt(argv, "s:i:k:",["inputstring=", "inputfile="])
    except getopt.GetoptError:
        print (usage())
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-i", "--inputfile"):
            inputfile = arg
            is_inputfile = True
        elif opt in ("-h", "--help"):
            print (usage())

    #open file
    file = open(inputfile, "r")
    plaintext = file.read()
    print(plaintext)
    #create random one time pad (length of file) - using the otp file
    otp = create_otp(len(plaintext))
    print("otp: ", otp)
    #encrypt plain text with otp using xor cipher
    ciphertext = xor_cipher(plaintext, otp)
    print("ciphertext: ", ciphertext)

    result_file = open("results.txt", "w")
    result_file.write(ciphertext)
    file.close
    result_file.close

if __name__ == "__main__":
    main (sys.argv[1:])
