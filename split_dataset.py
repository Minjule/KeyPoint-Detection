import os
import shutil
import random

main_dataset_dir = 'dataset/images'
labels_dir  = 'dataset/labels'

train_images_dir = 'output/train/images'
train_labels_dir = 'output/train/labels'

val_images_dir = 'output/validation/images'
val_labels_dir = 'output/validation/labels'

test_images_dir = 'output/test/images'
test_labels_dir = 'output/test/labels'

for dir_path in [train_images_dir, train_labels_dir, val_images_dir, val_labels_dir, test_images_dir, test_labels_dir]:
    os.makedirs(dir_path, exist_ok=True)
image_files = os.listdir(main_dataset_dir)
random.shuffle(image_files)

train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

num_files = len(image_files)
train_split = int(train_ratio * num_files)
val_split = int(val_ratio * num_files) + train_split

for i, file in enumerate(image_files):
    src_image = os.path.join(main_dataset_dir, file)
    src_label = os.path.join(labels_dir, file.replace('.jpg', '.txt'))  
    
    if i < train_split:
        dst_image = os.path.join(train_images_dir, file)
        dst_label = os.path.join(train_labels_dir, file.replace('.jpg', '.txt')) 
    elif i < val_split:
        dst_image = os.path.join(val_images_dir, file)
        dst_label = os.path.join(val_labels_dir, file.replace('.jpg', '.txt')) 
    else:
        dst_image = os.path.join(test_images_dir, file)
        dst_label = os.path.join(test_labels_dir, file.replace('.jpg', '.txt'))  
    
    shutil.copy(src_image, dst_image)
    shutil.copy(src_label, dst_label)

print("Dataset split into train, validation, and test sets.")