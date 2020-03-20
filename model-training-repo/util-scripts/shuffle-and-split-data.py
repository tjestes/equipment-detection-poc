import os
from PIL import Image, ImageFilter, ImageEnhance
from time import time
import random
from shutil import copyfile
from math import floor, ceil

t_0 = time()

WKDIR = '/Users/tyler.estes/Documents/finishline/training-videos/manual-outline-cropped-transparent/'
AUGMENTED_DIR = 'augmented-frames'
FINAL_DIR = 'final-frames'
VAL_DIR = 'val'
TRAIN_DIR = 'train'

aug_dir = os.path.join(WKDIR, AUGMENTED_DIR)
final_dir = os.path.join(WKDIR, FINAL_DIR)
train_dir = os.path.join(WKDIR, TRAIN_DIR)
val_dir = os.path.join(WKDIR, VAL_DIR)

# create directories
os.mkdir(final_dir) if not(os.path.exists(final_dir)) else False    # final directory
[os.mkdir(os.path.join(final_dir, shoe)) for shoe in shoe_names if not(os.path.exists(os.path.join(final_dir, shoe)))]   # sub final directories
os.mkdir(train_dir) if not(os.path.exists(train_dir)) else False    # train directory
[os.mkdir(os.path.join(train_dir, shoe)) for shoe in shoe_names if not(os.path.exists(os.path.join(train_dir, shoe)))]   # sub final directories
os.mkdir(val_dir) if not(os.path.exists(val_dir)) else False        # val directory
[os.mkdir(os.path.join(val_dir, shoe)) for shoe in shoe_names if not(os.path.exists(os.path.join(val_dir, shoe)))]   # sub final directories

# set video names and directories
folders_to_ignore = ['.ds_store', AUGMENTED_DIR, FINAL_DIR, TRAIN_DIR, VAL_DIR]
aug_dir_fpaths = [os.path.join(aug_dir, folder) for folder in os.listdir(aug_dir) if label.lower() not in folders_to_ignore]
final_frames = [os.path.join(final_dir, label) for label in os.listdir(final_dir) if label.lower() not in folders_to_ignore]

# sort
aug_dir_fpaths.sort()
final_frames.sort()

# shuffle frames
for path in aug_dir_fpaths:
    label = path.split('/')[-1]
    aug_frames = os.listdir(path)
    aug_frame_path = [os.path.join(path, frame) for frame in aug_frames if '.DS_Store' not in frame]

    random.shuffle(aug_frame_path)

    count = 1
    for f in aug_frame_path:
        if '.DS_Store' not in f:
            dst_path = os.path.join(final_dir, label, '{}_{}.png'.format(label, count))
            copyfile(f, dst_path)

            count += 1

TRAIN_SPLIT = 0.75

for dir in final_frames:
    label = dir.split('/')[-1]
    # set length of dir
    length = len(os.listdir(dir))
    len_train = round(length * TRAIN_SPLIT)

    # get datasets
    frames = [os.path.join(dir, frame) for frame in os.listdir(dir) if frame not in folders_to_ignore]
    frames.sort()
    train_data = frames[:len_train]
    val_data = frames[len_train:]

    # copy train data
    # dst_path = os.path.join(train_dir, label, '/')
    [copyfile(frame, os.path.join(train_dir, label, frame.split('/')[-1])) for frame in train_data if frame not in folders_to_ignore]

    # # copy train data
    # # dst_path = os.path.join(val_dir, label, '/')
    [copyfile(frame, os.path.join(val_dir, label, frame.split('/')[-1])) for frame in val_data if frame not in folders_to_ignore]

    
t_fin = time() - t_0
print('\n Script completed...elapsed time {}'.format(t_fin))

 



