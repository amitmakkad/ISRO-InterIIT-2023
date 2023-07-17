for i in `seq 0 1 1638`
do
	python demo.py --input /home/cynaptics/isro/lte/cut_tmc/${i}.png --model /home/cynaptics/isro/lte/save/_train_edsr-baseline-lte/epoch-last.pth --scale 16 --output /home/cynaptics/isro/lte/tmc_pred_cut/${i}.png --gpu 0
done
