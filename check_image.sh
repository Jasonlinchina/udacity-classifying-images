python3 check_images.py -d pet_images/ -a vgg -df dognames.txt > res_vgg.txt &
python3 check_images.py -d pet_images/ -a alexnet -df dognames.txt > res_alexnet.txt &
python3 check_images.py -d pet_images/ -a resnet -df dognames.txt > res_resnet.txt &


