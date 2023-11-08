import statistics

data = [95, 35, 50, 65, 70, 85, 25, 100, 80, 90, 45, 40, 35, 20, 75, 50, 40, 60, 80, 75]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

nilai_uas = sum(data)
print(f"Jumlah nilai_uas: {nilai_uas}")
 
jumlah_nilai_uas = len(data)
print(f"Jumlah total nilai uas: {jumlah_nilai_uas}")
 
mean_value = nilai_uas / jumlah_nilai_uas
print(f"Mean: {mean_value}")


sorted_data = sorted(data)
print(f"Data berurut: {sorted_data}")

h = len(sorted_data)
print(f"Jumlah total nilai uas: {h}")

index_tengah = h//2 

if h % 2 == 0:
    print(f"Jumlah nilai uas Genap")
    median1 = sorted_data[index_tengah]
    median2 = sorted_data[index_tengah - 1]
    print(f"Nilai tengah: {median1} {median2}")
    median_value = (median1 + median2) / 2
    
else:
    print(f"Jumlah nilai  Ganjil")
    median_value = sorted_data[index_tengah]
    print(f"Nilai tengah: {median_value}")

print(f"Median: {median_value}")

from collections import Counter

counter = Counter(data)
mode_data = dict(counter) 
max_counter = max(list(counter.values())) 
print(f"Max Counter: {max_counter}")

mode_value = []
for k, v in mode_data.items():
    print(f"{k} muncul {v} kali")
    if v == max(list(counter.values())):
        mode_value.append(k)
    
print(f"Mode: {mode_value}")