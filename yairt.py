import argparse
import os
from PIL import Image
import uuid
from sys import argv
import colorama
import glob




width__ = 200
height__ = 200


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


DESCRIPTION = 'YAIRT Yet another image resize tool'
HELP = {
    '-w': 'define el ancho maximo',
    '-h': 'define el alto maximo',
    '-o': 'archivo o directorio de salida',
    '-d': 'especifica que lo que se analizara es un directorio'
}


def color_print(text, color=''):
    print(color + text + bcolors.ENDC)


def create_thumbnail(path, size):
    filename, ext = os.path.splitext(path)
    uid = uuid.uuid4()
    img = Image.open(path)
    img.thumbnail(size)
    filename = '{}_thumb_{}{}'.format(filename, uid, ext)
    img.save(filename , 'JPEG')
    color_print('Creada: ' + filename, bcolors.OKGREEN) 


def create_uid(name):
    uid = uuid.uuid4()
    return '{}_thumb_{}'.format(name, uid)


def main():
    colorama.init()
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('arg1')
    parser.add_argument('-d', action='store_true', help=HELP['-d'])
    parser.add_argument('-o', default=False, help=HELP['-o'])
    parser.add_argument('-w', default=width__, help=HELP['-w'])
    parser.add_argument('-hh', default=height__, help=HELP['-h'])
    parser.add_argument('-s', default='{}x{}'.format(width__,height__), help=HELP['-h'])

    args = parser.parse_args()
    size = [width__, height__]
    filepath = args.arg1

    if args.o:
        fileout = args.o

    if args.s:
        size = list(map(lambda x: int(x), args.s.split('x')))

    if args.w != False:
        size[0] = int(args.w)

    if args.hh != False:
        size[1] = int(args.hh)

    if args.d:
        if (os.path.isdir(filepath)):
            for path_ in glob.glob(filepath + '*.jpg'):
                create_thumbnail(filepath_, size)
        else:
            color_print('Error "{}" no es un directorio'.format(filepath), bcolors.FAIL)
    else:
        if (os.path.isfile(filepath)):
            create_thumbnail(filepath, size)
        else:
            color_print('Error "{}" no es un archivo'.format(filepath), bcolors.FAIL)


if __name__ == '__main__':
    main()

