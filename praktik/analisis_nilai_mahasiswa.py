def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)
def nilai_lulus(data, batas=60):
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
lulus = nilai_lulus(nilai)
print(f"Data : {nilai}")
print(f"Banyak data : {len(nilai)}")
print(f"Total : {sum(nilai)}")
print(f"Rata-rata : {rata_rata(nilai):.2f}")
print(f"Minimum : {min(nilai)}")
print(f"Maksimum : {max(nilai)}")
print(f"Nilai lulus : {lulus}")
print(f"Jumlah lulus : {len(lulus)}")
print(f"Belum lulus : {len(nilai) - len(lulus)}")