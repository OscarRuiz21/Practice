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

with open(args.archivo, 'r') as file:
    
    if args.argumento2 == "read":
        content = file.read()
        print(content)
    else:
        pattern = args.argumento2
        for line in file:
            if pattern in line:
                print(line)






