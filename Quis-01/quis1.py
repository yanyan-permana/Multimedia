nilai = input("Inputkan nilaimu: ")
if int(nilai) >= 90:
    grade = "A"
    keterangan = "Lulus"
elif int(nilai) >= 80:
    grade = "B+"
    keterangan = "Lulus"
elif int(nilai) >= 70:
    grade = "B"
    keterangan = "Lulus"
elif int(nilai) >= 60:
    grade = "C+"
    keterangan = "Lulus"
elif int(nilai) >= 50:
    grade = "C"
    keterangan = "Tidak Lulus"
elif int(nilai) >= 40:
    grade = "D"
    keterangan = "Tidak Lulus"
else:
    grade = "E"
    keterangan = "Tidak Lulus"

print("Grade: %s" % grade)
print("Ketrangan: %s" % keterangan)
