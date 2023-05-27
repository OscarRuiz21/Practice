# Modulo Argparse
import os
import argparse
# os.system("cls")

parser = argparse.ArgumentParser(description='Calculadora, suma/resta/multiplica a y b')
                                 #prefix_chars='+')
parser.add_argument('-a', '--numero_a', type=int, help='Parametro a')
parser.add_argument('-b', '--numero_b', type=int, help='Parametro_b')
parser.add_argument('-o', '--operacion', 
                    type=str, 
                    help='Operacion, puede ser: suma, resta, multiplicacion (Suma default)', 
                    default='suma',
                    required=False)

args = parser.parse_args()

print(vars(args))
if args.operacion == 'suma':
    print('El valor de la suma es:',args.numero_a + args.numero_b)
elif args.operacion == 'resta':
    print('El valor de la resta es:',args.numero_a - args.numero_b)
elif args.operacion == 'multiplicacion':
    print('El valor de la multiplicacion es:',args.numero_a * args.numero_b)
