#!pip install easyocr

import PIL
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import easyocr

reader = easyocr.Reader(['ru', 'en'])
im = PIL.Image.open("<ПУТЬ К ФАЙЛУ>")

def draw_boxes(image,bounds,color='red',width=5):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0,*p1,*p2,*p3,*p0], fill=color,width=width)
    plt.figure(figsize=(9, 12), dpi=80)
    plt.axis('off')
    plt.savefig('image.jpg', bbox_inches='tight', pad_inches=0)
    #plt.show()
    img = plt.imshow(image, interpolation='nearest') #вывод изображения
    ##удаление осей
    img.set_cmap('hot')
    

bounds = reader.readtext("<ПУТЬ К ФАЙЛУ>", paragraph=True) 
draw_boxes(im,bounds)
