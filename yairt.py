from PIL import Image
import os
import uuid
from sys import argv
import colorama



# Flags
dir__ = False 
wx__ = False
hx__ = False


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




def main():
    colorama.init()
    size = 128, 128
    _argv = argv[1:] #first element is script name
    try:
        dir__ = _argv.index('-d')
        _argv.pop(dir__)
        dir__ = True
    except ValueError:
        dir__ = False

    #if len(map())

    #
    # if dir__ == -1:
    #    _argv.pop(dir__)
    #    dir__ = True

    path = None
    if len(_argv) == 1:
        path = argv[0]
    else:
        print(bcolors.FAIL + "Error faltan parametros" + bcolors.ENDC)
        print(bcolors.WARNING + '|'.join(argv[1:]) + bcolors.ENDC)


    #filename, ext = os.path.splitext(path)
    #uid = uuid.uuid4()
    #img = Image.open(path)
    #img.thumbnail(size)
    #img.save('{}_thumb_{}.{}'.format(filename, uid, ext), 'JPEG')


if __name__ == '__main__':
    main()

