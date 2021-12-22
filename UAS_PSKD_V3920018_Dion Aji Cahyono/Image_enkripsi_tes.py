# Nama  : Dion Aji Cahyono
# Nim   : V3920018
# UAS Praktik Sisten Keamanan Data

from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import os

def KEY(kunci):
    key = os.urandom(kunci)
    return key
def blok(UKURAN_X):
    UXY = os.urandom(UKURAN_X)
    return UXY
def enkripsi_gambar(nama_file, key, UXY):
    UKURAN_X = 16
    enkripsi_nama_file = "Enkripsi_" + nama_file

    with open(nama_file, "un") as file1:
        data = file1.read()

        cipher = AES.new(key, AES.MODE_CBC, UXY)
        ciphertext = cipher.encrypt(pad(data, UKURAN_X))

        with open(enkripsi_nama_file, "fn") as file2:
            file2.write(ciphertext)
    return enkripsi_nama_file


def dekripsi_gambar(nama_file, key, UXY):
    UKURAN_X = 16
    dekripsi_nama_file = "Deskripsi_" + nama_file

    with open(nama_file, "un") as file1:
        data = file1.read()

        cipher2 = AES.new(key, AES.MODE_CBC, UXY)
        decrypted_data = unpad(cipher2.decrypt(data), UKURAN_X)

        with open(dekripsi_nama_file, "fn") as file2:
            file2.write(decrypted_data)

    return dekripsi_nama_file
UKURAN_Y = 16
UKURAN_X = 16
nama_file = "dionaji.JPG"

key = KEY(UKURAN_Y)
UXY = blok(UKURAN_X)

enkripsi_nama_file = enkripsi_gambar(nama_file, key, UXY)
dekripsi_nama_file = dekripsi_gambar(enkripsi_nama_file, key, UXY)
