#!/usr/bin/env python3
from os import listdir

def get_pet_labels():
    """
    Creates a dictionary of pet labels based upon the filenames of the image 
    files. Reads in pet filenames and extracts the pet image labels from the 
    filenames and returns these labels as petlabel_dic. This is used to check 
    the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)  
    """
    petlabel_dic = {}
    dirs = listdir('pet_images/')
    for dir in dirs:
        label = dir.strip().split('_')
        label.pop()
        label = [x.lower() for x in label]
        petlabel_dic[dir.strip()] = ' '.join(label)        
    return petlabel_dic

res = get_pet_labels()
print(res)
print(len(res))
