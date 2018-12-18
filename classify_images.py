#!/usr/bin/env python3
from classifier import classifier

def classify_images(images_dir, petlabel_dic, model):
    """
    Creates classifier labels with classifier function, compares labels, and 
    creates a dictionary containing both labels and comparison of them to be
    returned.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images in this function. 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by pretrained CNN models (string)
      petlabel_dic - Dictionary that contains the pet image(true) labels
                     that classify what's in the image, where its key is the
                     pet image filename & its value is pet image label where
                     label is lowercase with space between each word in label 
      model - pretrained CNN whose architecture is indicated by this parameter,
              values must be: resnet alexnet vgg (string)
     Returns:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and 
                    classifer labels and 0 = no match between labels
    """
    results_dic = {}
    for filename, label in petlabel_dic.items():
        result = classifier(images_dir + filename, model)
        result = result.strip().lower()
        found_idx = result.find(label)
        if found_idx < 0:
            results_dic[filename] = [label, result, 0]
        elif (
        (found_idx == 0 or result[found_idx - 1] == " ") and
        (len(label) == len(result) or result[found_idx + len(label):
        found_idx + len(label) + 1] in (" ", ","))
        ):
            results_dic[filename] = [label, result, 1]
        else:
            results_dic[filename] = [label, result, 0]
    return results_dic

petlabel_dic = {'Great_pyrenees_05367.jpg': 'great pyrenees', 'Great_pyrenees_05435.jpg': 'great pyrenees'}
print(classify_images('pet_images/', petlabel_dic, 'vgg'))
