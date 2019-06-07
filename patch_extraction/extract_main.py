from extract_patches_split import capextract
from multiprocessing import Pool, cpu_count
from itertools import product
from shutil import copyfile
import pickle
from random import shuffle, sample
import os
from glob import glob

slides = ["patient_010_node_4", "patient_017_node_2", "patient_017_node_4",
          "patient_020_node_2", "patient_020_node_4", "patient_022_node_4",
          "patient_034_node_3", "patient_042_node_3", "patient_044_node_4",
          "patient_046_node_4", "patient_051_node_2", "patient_073_node_1",
          "patient_075_node_4", "patient_092_node_1", "patient_096_node_0",
          "tumor_011", "tumor_031", "tumor_034", "tumor_039", "tumor_047", "tumor_055", "tumor_061"]

slides_dir = "~/Downloads/patients_lesions/"
patches_dir = "~/Repositories/WSI-analysis/dataset_patches/"
destination_path = "~/Repositories/WSI-analysis/dataset_patches_level32/"


def get_patch_list(positive):
    patch_file = 'pospaths.txt' if positive else 'negpaths.txt'
    patches = []
    with (open(patches_dir + wsi + '/level' + str(level) + '/' + patch_file, "rb")) as openfile:
        while True:
            try:
                patches.extend(pickle.load(openfile))
            except EOFError:
                break
        return patches


def copy_n_rand_patches(patch_list, dest, n, pos):
    if n >= len(patch_list):
        for i in range(len(patch_list)):
            copyfile(patch_list[i], dest +
                     patch_list[i].split('/')[2] + '_' + pos + '_' + str(i)+'.jpg')
    else:
        for i, file in enumerate(sample(patch_list, n)):
            copyfile(file, dest+file.split('/')[2] + '_' + pos + '_' + str(i)+'.jpg')

level = 3
positive_patches = []
negative_patches = []
for wsi in slides:
      capextract(slides_dir + wsi + ".tif", slides_dir + "lesion_annotations/" + wsi + ".xml",level = level)
      positive_patches += get_patch_list(True)
      negative_patches += get_patch_list(False)


### Copy n random extracted patches by class
copy_n_rand_patches(positive_patches, destination_path+"positive/", 2300, "pos")
copy_n_rand_patches(negative_patches, destination_path+"negative/", 2300, "neg") 

####  multithread execution
# slides_paths = [slides_dir + wsi + ".tif" for wsi in slides]
# slides_annos = [slides_dir + "lesion_annotations/" +
#                 wsi + ".xml" for wsi in slides]
# p = Pool(processes = cpu_count()-2)
# p.starmap(capextract, product(slides_paths,slides_annos))
# p.close()
# p.join()

### other ways to copy patches around
# positive_patches = [y for x in os.walk("/~/Master/datasets/camelyon_17_16_level0/negative") for y in glob(os.path.join(x[0], '*.jpeg'))]
# negative_patches = [y for x in os.walk("~/Master/datasets/camelyon_17_16_level0/positive") for y in glob(os.path.join(x[0], '*.jpeg'))]
# copy_n_rand_patches(positive_patches, "~/Master/datasets/camelyon_17_16_level0_n/positive/", 60000,"pos")
# copy_n_rand_patches(negative_patches, "~/Master/datasets/camelyon_17_16_level0_n/negative/", 60000,"neg")