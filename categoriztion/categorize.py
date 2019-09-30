import os
import shutil

base_path = '/home/fashi/datasets/17flowers'
dataset_path = os.path.join(base_path, 'jpg')
image_list = sorted(os.listdir(dataset_path))
flower_name = ['daffodil', 'snowdrop', 'lilyVally', 'bluebell', 'crocus', 'iris', 'tiger-lily', 'tulip',
               'fritillary', 'sunflower', 'daisy', "coltis'foot", "dandelion", 'cowslip', 'buttercup',
               'windflower', 'pansy']


for (i, flower) in enumerate(flower_name):
    new_cat_path = os.path.join(base_path, flower)

    if not os.path.exists(new_cat_path):
        os.mkdir(new_cat_path)
    lis = image_list[i*80:i*80+80]
    for (j, image) in enumerate(lis):
        image_path = os.path.join(dataset_path, image)
        new_image_path = os.path.join(new_cat_path, '{}.jpg'.format(j))
        shutil.copy(image_path, new_image_path)

        print("[INFO] copying {} -> {}".format(image_path, new_image_path))
