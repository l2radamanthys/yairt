from PIL import Image
import os
import uuid
from sys import argv

# Flags
dir__ = False 
wx__ = False
hx__ = False


def main():
    size = 128, 128
    _argv = argv[1:] #first element is script name
    dir__ = argv.index('-d')
    if dir__ == -1:
        _argv.pop(dir__)
        dir__ = True

    if len(map())

    #
    # if dir__ == -1:
    #    _argv.pop(dir__)
    #    dir__ = True

    path = None
    if len(argv) >= 1:
        path = argv[0]
    

    filename, ext = os.path.splitext(path)
    uid = uuid.uuid4()
    img = Image.open(path)
    img.thumbnail(size)
    img.save('{}_thumb_{}.{}'.format(filename, uid, ext), 'JPEG')


if __name__ == '__main__':
    main()

