import argparse
import re

# Argumentos

parser = argparse.ArgumentParser(description='Aquí se daran los argumentos')
parser.add_argument('-a', "--archivo", 
                    type=str,
                    help='Archivo a leer')
parser.add_argument('--argumento2', 
                    type=str,
                    help='quieres que lea el archivo o busque un patron'
                    )

args = parser.parse_args()

linea_p = []
with open(args.archivo, 'r') as file:

    content = file.read()

    if args.argumento2 == "read":
        print(content)
    else:
        #argument_pattern = args.argumento2
        for linea in file:
            print(linea)

            # pattern = re.compile(args.argumento2)
            # cumple = re.search(pattern, linea)
            if args.argumento2 in linea:
                print(linea)



