#!/usr/bin/python3

# A python File crypter
# Developed by Elieroc
# Start of project : 19/10/2020
# Actual version : 1.0

import pyAesCrypt

def encrypt(file, password, bufferSize):
    pyAesCrypt.encryptFile(file, "Enc - " + file, password, bufferSize)

def decrypt(file, password, bufferSize):
    pyAesCrypt.decryptFile(file, "Dec - " + file, password, bufferSize)

choice = str(input("Crypter (|C|) ou Décrypter (|D|) ? "))

file = str(input("Nom du fichier : "))
password = str(input("Mot de passe : "))
bufferSize = 64 * 1024

if choice == "C":
    encrypt(file, password, bufferSize)
    print("Le fichier a bien été crypté !")
elif choice == "D":
    decrypt(file, password, bufferSize)
    print("Le fichier a bien été decrypté !")
else:
    print("Choisir une option valable : C ou D")
