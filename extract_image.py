import pandas as pd
import os
from PIL import Image

df = pd.read_csv("project-54-at-2023-12-20-08-28-2f8b7c8d.csv")
saved_columns = df[['img', 'kp-1']]

folder_path = 'E:\mtshare\cam04'
image_path = 'images'

os.makedirs(folder_path, exist_ok=True)

def read_extract_images_from_folder(folder_path, saved_columns):
    images = []
    imgs = []
    column_values = saved_columns['img'].tolist()

    for i in range(len(column_values)):
        column_values[i] = column_values[i][-28:]
        
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            if (filename in column_values):
                try:
                    img = Image.open(os.path.join(folder_path, filename))
                    #img.save(os.path.join(image_path, filename))
                    imgs.append(filename)
                    images.append(img)
                    #print(f"Read {filename}")
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
    else:
        print("Folder not found.")
    return images, imgs

#images, img_names = read_extract_images_from_folder(folder_path, saved_columns)
#print(len(images))

print(saved_columns["kp-1"])
# img = Image.open(images[0].filename)
# img.show()
# print(type(images[0]))