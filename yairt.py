from PIL import Image
import os
import uuid
from sys import argv


def main():
    size = 128, 128

    path = None
    if len(argv) >= 2:
        path = argv[1]
    
    filename, ext = os.path.splitext(path)
    uid = uuid.uuid4()
    img = Image.open(path)
    img.thumbnail(size)
    img.save('{}_thumb_{}.{}'.format(filename, uid, ext), 'JPEG')


if __name__ == '__main__':
    main()

