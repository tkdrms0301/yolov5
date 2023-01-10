import yaml

dict_file = {'train':'F:\\yolo\\images\\train' ,
            'val': 'F:\\yolo\\images\\val',
            'nc' : '3',
            'names' : ['helmet','head','person']}

with open('F:\\yolo\\yolov5\\data\\hard_head.yaml', 'w+', encoding='utf-8') as file:
    documents = yaml.dump(dict_file, file)