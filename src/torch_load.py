import torch
import os
import cv2
import glob

model = torch.hub.load('/home/ubuntu/YoloV7', 'custom', 'best15.pt',
                       force_reload=True, trust_repo=True)


COIN_CONFIDENCE = 0.70
OUTPUT_DIR = 'outputTorchTrain'

image_path_ = glob.glob('/home/ubuntu/YoloV7/imagePrueba.jpg')
out_path = '/home/ubuntu/YoloV7'

os.makedirs(OUTPUT_DIR, exist_ok=True)
results = model(image_path_)
df = results.pandas().xyxy[0]
image = cv2.imread(image_path_)
for i, row in df.iterrows():
    if row['class'] == 0 and row['confidence'] > COIN_CONFIDENCE:
        coin_bbox = [int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])]
        coin_image = image[coin_bbox[1]:coin_bbox[3], coin_bbox[0]:coin_bbox[2]]
        cv2.imwrite(f'{out_path}/1_coin.jpg', coin_image)
print('Done..')