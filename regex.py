import os
import re
os.system("cls")

# Abrir archivo (Lectura = r, escritura = w, a = agregar al final y r+)
with open("Archivo.txt", "r") as f:
    content = f.read()

print(content)   

pattern = r'\ba\w+'
matches = re.findall(pattern, content)

print(matches)

if (matches):
    print('Si tiene con a')
else:
    print('No tiene inicios con a')

pattern2 = r'\bal\w+' 
matches2 = re.findall(pattern2, content)
print(matches2[:])

pattern3 = r'\s'
matches3 = re.split(pattern3, content)
print(matches3)
  
matches4 = re.search(pattern2, content)
print(matches4.group()) 

pattern5 = r'\d+'
matches5 = re.findall(pattern5, content)
print(matches5)

pattern6 = r'\n'
matches6 = re.split(pattern6, content)
print(matches6)
print(matches6[1])
print(matches6[2])

pattern7 = '[a-b]\w+' #'[a-b]\w+' or '[abc]\w+' or '[a-bA-B]\w+' or '[123]\+w'
matches7 = re.findall(pattern7, content)
print(matches7)

pattern8 = r'Hola'
matches8 =  re.sub(pattern8, 'Hello', content)
print(matches8)

pattern9 = r'ac?[2-6][0-9]|ab?[2-6][0-9]'
matches9 = re.findall(pattern9, content)
print(matches9)