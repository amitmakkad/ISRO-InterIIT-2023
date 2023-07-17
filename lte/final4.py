import image-similarity-measure
from image_similarity_measures.evaluate import evaluation
import numpy as np
fsim=[]
issm=[]
ssim=[]
psnr=[]
for x in os.listdir('/home/cynaptics/isro/lte/val_pred_ohrc/'):
	eval_=evaluation(org_img_path='/home/cynaptics/isro/lte/val_pred_ohrc/'+x, pred_img_path="/home/cynaptics/isro/dark_removed/test/"+x, metrics=["fsim", "psnr","issm","ssim"])
	fsim.append(eval_['fsim']
	issm.append(eval_['issm']
	ssim.append(eval_['ssim']
	psnr.append(eval_['psnr']

print("Average PSNR is {}".format(np.average(psnr)))
print("Average ISSM is {}".format(np.average(psnr)))
print("Average FSIM is {}".format(np.average(psnr)))
print("Average SSIM is {}".format(np.average(psnr)))
