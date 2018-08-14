from PIL import Image
import os
import uuid
from sys import argv
import colorama
import glob


# Flags
dir__ = False 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def create_thumbnail(path, size):
    filename, ext = os.path.splitext(path)
    uid = uuid.uuid4()
    img = Image.open(path)
    img.thumbnail(size)
    img.save('{}_thumb_{}{}'.format(filename, uid, ext), 'JPEG')


def main():
    colorama.init()
    # thumbnail
    size = [128, 128]
    # first element is script name
    _argv = argv[1:] 
    
    # si se consulto ayuda
    try:
        h = _argv.index('-h')
        print(bcolors.HEADER + 'Ayuda no implementada' + bcolors.ENDC)
        return True
    except ValueError:
        pass
    
    # ¿se evalua un directorio?
    try:
        dir__ = _argv.index('-d')
        _argv.pop(dir__)
        dir__ = True
    except ValueError:
        dir__ = False

    # extra tags
    i = 0
    r = []
    for tag in _argv:
        if tag[:2] == '-s':
            size = list(map(lambda x: int(x), tag[2:].split('x')))
            r.append(i)

        elif tag[:2] == '-w':
            size[0] = int(tag[2:])
            r.append(i)

        elif tag[:2] == '-h':
            size[1] = int(tag[2:])
            r.append(i)

        i += 1

    # remove tags
    j = 0
    for i in r:
        _argv.pop(i - j)
        j += 1

    path = None
    if len(_argv) == 1:
        path = _argv[0]

    else:
        print(bcolors.FAIL + 'Error faltan parametros' + bcolors.ENDC)
        print(size)
        print(bcolors.WARNING + '|'.join(argv[1:]) + bcolors.ENDC)

    if dir__:
        for path_ in glob.glob(path + '*.jpg'):
            create_thumbnail(path_, size)
    else:
        create_thumbnail(path, size)

if __name__ == '__main__':
    main()

