# Nama  : Dion Aji Cahyono
# Nim   : V3920018
# UAS Praktik Sisten Keamanan Data

import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES


def kunci(kunci):
    key = os.urandom(kunci)
    return key


def blo(blocksize):
    bz = os.urandom(blocksize)
    return bz


def enkripsi_gambbar(nama_file, key, bz):
    Ukuran_X = 16
    enkripsi_file = "Hasil_Enkripsi_" + nama_file

    with open(nama_file, "rb") as file1:
        data = file1.read()

        cipher = AES.new(key, AES.MODE_CBC, bz)
        ciphertext = cipher.encrypt(pad(data, Ukuran_X))

        with open(enkripsi_file, "wb") as file2:
            file2.write(ciphertext)
    return enkripsi_file


def dekripsi_gambbar(nama_file, key, bz):
    Ukuran_X = 16
    dekripsi_file = "Hasil_Deskripsi_" + nama_file

    with open(nama_file, "rb") as file1:
        data = file1.read()

        cipher2 = AES.new(key, AES.MODE_CBC, bz)
        decrypted_data = unpad(cipher2.decrypt(data), Ukuran_X)

        with open(dekripsi_file, "wb") as file2:
            file2.write(decrypted_data)

    return dekripsi_file


Ukuran_kunci = 16
Ukuran_X = 16
nama_file = "dionaji.JPG"

key = kunci(Ukuran_kunci)
bz = blo(Ukuran_X)

enkripsi_file = enkripsi_gambbar(nama_file, key, bz)
dekripsi_file = dekripsi_gambbar(enkripsi_file, key, bz)
