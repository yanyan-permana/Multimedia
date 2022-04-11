# Function kompresi
def kompresi(data):
    hasilKompresi = ""
    hurufSebelumnya = ""
    x = 1

    if not data:
        return ""

    for char in data:
        if char != hurufSebelumnya:
            if hurufSebelumnya:
                hasilKompresi += str(x) + hurufSebelumnya
            x = 1
            hurufSebelumnya = char
        else:
            x += 1
    hasilKompresi += str(x) + hurufSebelumnya
    return hasilKompresi


def dekompresi(data):
    hasilDekompresi = ""
    x = ""

    for char in data:
        if char.isdigit():
            x += char
        else:
            hasilDekompresi += char * int(x)
            x = ""
    return hasilDekompresi


file = open("kompres.txt", "r")
kalimat = file.read()

print("Kalimat: ", kalimat)
print("Masukan pilihan: ")
print("1. Kompresi")
print("2. Dekompresi")

pilihan = input("Pilihan 1/2: ")

# Kompresi
if pilihan == "1":
    hasilNya = kompresi(kalimat)
    print("Hasilnya kompresi: ", hasilNya)

    # Dekompresi
else:
    hasilNya = dekompresi(kalimat)
    print("Hasilnya dekompresi: ", hasilNya)

file.close()

fileKompres = open("kompres.txt", "w")
fileKompres.write(hasilNya)
