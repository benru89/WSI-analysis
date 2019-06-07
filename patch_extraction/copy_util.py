
from shutil import copyfile
import pickle
from random import shuffle, sample
import os
from glob import glob



def copy_n_rand_patches(src_dir, dest, n):    
    for i, file in enumerate(sample(os.listdir(src_dir), n)):
        copyfile(src_dir+file, dest+file)


copy_n_rand_patches("~/Repositories/WSI-analysis/level0/positive/", "~/datasets/camelyon_17_16_level0/", 50000)
copy_n_rand_patches("~/Repositories/WSI-analysis/level0/negative/", "~/datasets/camelyon_17_16_level0/", 50000)
