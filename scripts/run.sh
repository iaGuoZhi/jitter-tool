#!/bin/bash

work=../src/jitter
if [ ! -f "$work" ]; then
  echo "File '$work' does not exist. Please compile it before running $0"
  exit 1
fi

running_command="taskset -c 8 $work -c 7 -f -i 300"

function save_info() {
  echo -e "Time: $(date +"%Y-%m-%d %H:%M:%S")" >> $dir/info.txt
  echo -e "Cmdline: $(cat /proc/cmdline)" | fold -w 60 >> $dir/info.txt
  echo -e "Command: $running_command" | fold -w 60 >> $dir/info.txt
}

# make sure results directory exists
if [ ! -d "../results" ]; then
  mkdir "../results"
fi
# create a dir named as timestamp
dir=../results/jitter_$(date +"%Y%m%d%H%M%S")
mkdir -p $dir

cp /proc/interrupts $dir/interrupts_$(date +"%Y%m%d%H%M%S").txt
$running_command > $dir/jitter.txt
cp /proc/interrupts $dir/interrupts_$(date +"%Y%m%d%H%M%S").txt

echo "Result are saved in $dir/jitter.txt"

save_info

python3 ./draw.py $dir
echo "Image are saved in $dir/jitter.png"
