#!/bin/bash
for i in `seq 0 32 4096`
do
   for j in `seq 0 32 4096`
   do
      python demo.py --input /home/cynaptics/isro/lte/slice5/slice5/${i}_${j}.png --model /home/cynaptics/isro/lte/save/_train_edsr-baseline-lte/epoch-last.pth --scale 16 --output /home/cynaptics/isro/lte/slice5/preds/${i}_${j}.png --gpu 0
   done
done
