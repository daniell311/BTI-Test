

import itertools

nilai = []
print("Soal(Masukkan nilai-nilai tiap pertanyaan yang dipisah dengan koma, maksimal 10 pertanyaan)")
numbers = list(map(int, input("Masukkan Nilai Tiap Pertanyaan: ").split(',')))
nilai.append(numbers)
target = int(input("Masukkan Nilai T = "))

result = [seq for i in range(len(numbers), 0, -1)
          for seq in itertools.combinations(numbers, i)
          if sum(seq) == target]

print("Jumlah Semua Kombinasi(K) = ", len(result))
print("Daftar Kombinasi ")
print("Kombinasi Ke-", *result, sep="\n")
