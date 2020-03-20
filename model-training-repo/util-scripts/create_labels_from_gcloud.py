import os
import glob
import sys
import warnings
import time
from random import shuffle
​
def polygon_to_center_and_size(poly):
    min_x = 1
    min_y = 1
    max_x = 0
    max_y = 0
​
    for vertex in poly:
        if vertex[0] < min_x:
            min_x = vertex[0]
        if vertex[0] > max_x:
            max_x = vertex[0]
        if vertex[1] < min_y:
            min_y = vertex[1]
        if vertex[1] > max_y:
            max_y = vertex[1]
​
    width    = max_x - min_x
    height   = max_y - min_y
    center_x = width/2 + min_x
    center_y = height/2 + min_y
​
    return '0 ' + ' '.join([str(a) for a in [center_x,center_y,width,height]]) + '\r\n'
    
​
def localize_objects(path):
    """Localize objects in the local image.
    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
​
    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
​
    objects = client.object_localization(
        image=image).localized_object_annotations
    output = []
    for object_ in objects:
        shoe = []
        for vertex in object_.bounding_poly.normalized_vertices:
            if object_.name =='Shoe':
                shoe.append((vertex.x, vertex.y))
        if len(shoe) > 0:
            output.append(shoe)
    return output
​
def main():
    warnings.simplefilter("ignore")
    full_set_path = sys.argv[1]
    output_dir = sys.argv[2]
    images = glob.glob(full_set_path)
    shuffle(images)
    total = len(images)
    for i,image in enumerate(images):
        try:    
            file_name = os.path.basename(image)
            base_file = file_name.split('.')[0]
            if os.path.isfile(os.path.join(output_dir,base_file+'.txt')):
                continue
            data = localize_objects(image)
            with open(os.path.join(output_dir,base_file+'.txt'),'w') as f:
                for poly in data:
                    f.write(polygon_to_center_and_size(poly))
            print(base_file,i/total)
        except (KeyboardInterrupt, SystemExit):
            raise
​
if __name__ == '__main__':
    while True:
        try:
            main()
        except (KeyboardInterrupt, SystemExit):
            raise   
        except:
            time.sleep(30)
​
​