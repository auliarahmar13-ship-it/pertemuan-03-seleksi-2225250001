
# Input: nilai akhir dan kehadiran
# Proses: cek syarat kelulusan
# Output: Lulus atau Belum lulus

nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")