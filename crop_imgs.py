from PIL import Image
import os
from multiprocessing import Pool
from tqdm import tqdm
from functools import partial
from os import cpu_count
import numpy as np

DATA_DIR = "./data/"
OUTPUT_DIR = "./images/"

def resize_image(image_name):
    image_path =  os.path.join(DATA_DIR, image_name)
    im = Image.open(image_path)
    width,height = im.size

    new_width = min(width,height)
    new_height = min(width,height)

    left = int(np.ceil((width - new_width)/2))
    top = int(np.ceil((height - new_height)/2))
    right = int(np.ceil((width + new_width)/2))
    bottom = int(np.ceil((height + new_height)/2))

    im = im.crop((left, top, right, bottom))
    im.save(os.path.join(OUTPUT_DIR, image_name))

paths = os.listdir(DATA_DIR)
with Pool(processes = cpu_count() - 1) as p:
    with tqdm(total=len(paths)) as pbar:
        for v in p.imap_unordered(partial(resize_image), paths):
            pbar.update()
