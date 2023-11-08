import statistics

data = [100.5, 99.7, 101, 101.3, 99.9, 98.9, 165, 102.2, 98.7, 102.9, 100]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

tinggi_badan = sum(data)
print(f"Jumlah tinggi_badan: {tinggi_badan}")
 
jumlah_tinggi_badan = len(data)
print(f"Jumlah total tinggi badan: {jumlah_tinggi_badan}")
 
mean_value = tinggi_badan / jumlah_tinggi_badan
print(f"Mean: {mean_value}")


sorted_data = sorted(data)
print(f"Data berurut: {sorted_data}")

h = len(sorted_data)
print(f"Jumlah total tinggi badan: {h}")

index_tengah = h//2 

if h % 2 == 0:
    print(f"Jumlah tinggi badan Genap")
    median1 = sorted_data[index_tengah]
    median2 = sorted_data[index_tengah - 1]
    print(f"Nilai tengah: {median1} {median2}")
    median_value = (median1 + median2) / 2
    
else:
    print(f"Jumlah tinggi badan Ganjil")
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