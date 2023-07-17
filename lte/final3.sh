# search_dir=/home/cynaptics/isro/dark_removed/test/lr_test_16x
search_dir=$1
weights_path=$2
output_path=$3
for entry in "$search_dir"/*
do
  f="$(basename $entry)"
  python demo.py --input "$entry" --model $weights_path --scale 16 --output "$output_path$f" --gpu 0
done


