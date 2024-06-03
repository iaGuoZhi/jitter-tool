file1=$1
file2=$2
col=$3

paste $file1 $file2 -d ' ' | tr '\t' ' ' | awk -F' ' '{printf $1 ""; for (i=2; i<=NF/2; i++) {printf $(i+NF/2)-$i " "}print ""}' | awk -v col=$col '$col != 0 {print $0}'
