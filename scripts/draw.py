import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math
import sys

script = sys.argv[0]

if not len(sys.argv) == 2:
    sys.exit(f'Usage: python3 {script} work_dir')
work_dir = sys.argv[1]

csv_filename = f'{work_dir}/jitter.txt'
png_filename = f'{work_dir}/jitter.png'
info_filename = f'{work_dir}/info.txt'

min_data=[]
max_data=[]
idx=[]
i=0
header_n=50
with open(csv_filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        i+=1
        if (i <= header_n):
            continue
        idx.append(i)
        min_data.append(int(row[0]))
        max_data.append(int(row[1]))


# Compute average,median,minimal,maximum values
avg_min = round(sum(min_data)/len(min_data),2)
med_min = sorted(min_data[:])[len(min_data) // 2]
min_min = sorted(min_data[:])[0]
max_min = sorted(min_data[:])[-1]
avg_max = round(sum(max_data)/len(max_data),2)
med_max = sorted(max_data[:])[len(max_data) // 2]
min_max = sorted(max_data[:])[0]
max_max = sorted(max_data[:])[-1]

try:
    with open(info_filename, 'r') as file:
        info = file.read()
    info += '\n'
except Exception as e:
    info = ''

info+=f'Average min jitter: {avg_min}\n'
info+=f'Median min jitter: {med_min}\n'
info+=f'Minimal min jitter: {min_min}\n'
info+=f'Maximal min jitter: {max_min}\n\n'
info+=f'Average max jitter: {avg_max}\n'
info+=f'Median max jitter: {med_max}\n'
info+=f'Minimal max jitter: {min_max}\n'
info+=f'Maximal max jitter: {max_max}\n'

fig = plt.figure(figsize=(15, 5))
gs = gridspec.GridSpec(1, 2, width_ratios=[10, 5])
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])

# First image
ax1.set_title('Jitter distribution')
ax1.plot(idx, min_data, 's', linestyle='', label='Min', color='green')
ax1.plot(idx, max_data, 'x', linestyle='', label='Max', color='blue')
ax1.set_xlabel('Run number')
ax1.set_ylabel('Cycle')
ax1.grid(True)

ax2.text(0.5, 0.5, info, fontsize=10, ha='center', va='center')
ax2.axis('off')

plt.savefig(png_filename)
