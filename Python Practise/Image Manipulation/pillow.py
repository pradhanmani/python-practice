from PIL import Image, ImageFilter
import os


# from pathlib import Path            #####Used for the Location
# script_dir = Path(__file__).parent  #####Used for the Location

size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        
        i.save('pngs/{}.png'.format(fn))    ###To save all the jpg into png
        
        i.thumbnail(size_700)      ###Changing Resolution
        i.save('700/{}_700{}'.format(fn, fext))
        
        i.thumbnail(size_300)      ###Changing Resolution
        i.save('300/{}_300{}'.format(fn, fext))

image1 = Image.open('img4.jpg')
image1.save('img4.png') ###To save jpg into png

image1.rotate(90).save('img4_mod.jpg')   ###To rotate the photo

image1.convert(mode='L').save('img4_mod.jpg')   ###To change the color

image1.filter(ImageFilter.GaussianBlur(15)).save('img4_mod.jpg')  ###TO BLUR The Image
