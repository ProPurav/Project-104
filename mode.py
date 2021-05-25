from collections import Counter
import csv

with open('SOCR-HeightWeight.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
#sorting data to get height of people
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

# getting the mode
data = Counter(new_data)
mode_data_for_range = {
                    "50-60":0,
                    "60-70":0,
                    "70-80":0
                    }

for height,occurences in data.items():
    if 50 < float(height) < 60: 
        mode_data_for_range["50-60"] += occurences
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurences
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurences

mode_range, mode_occurences = 0,0
for range,occurences in mode_data_for_range.items():
    if occurences > mode_occurences:
      mode_range, mode_occurences = [int(range.split("-")[0]), int(range.split("-")[1])], occurences
mode = float((mode_range[0]+mode_range[1])/2)
print(f"Mode is - > {mode:2f}")