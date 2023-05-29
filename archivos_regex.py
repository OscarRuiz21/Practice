import re
import argparse

#Ejemplo 1

# Definiendo el patron
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
nombre_pattern = re.compile(r'\b[A-Z]\w+\s\b[A-Z]\w+')

# Configurar el archivo de texto
parser = argparse.ArgumentParser(description='Archivo de texto que necesitamos')
parser.add_argument('-a', '--archivo', 
                    type=str, 
                    help='Dame el archivo de texto que quieres leer',
                    default='email.txt',
                    required=False )
args = parser.parse_args()

with open(args.archivo, 'r') as file:
    content = file.read()
    emails = re.findall(email_pattern, content)
    nombres = re.findall(nombre_pattern, content)
    
    # print('Los emails registrados son:')
    # for i, email in enumerate(emails):
    #     print(f'{i+1}: {email}')

    # print('Los Nombres registrados son:')
    # for i, nombre in enumerate(nombres):
    #     print(f'{i+1}: {nombre}')
    
    registros = {}
    for i, nombre in enumerate(nombres):
        registros[nombre] = emails[i]


for llave, valor in registros.items():
    print(llave, valor)

print('Prueba lista')

        

# Ejemplo final

# Definir los patrones
# commit_pattern = re.compile(r"\b[0-9a-f]{40}\b")
# ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
# email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
# file_pattern = re.compile(r"\b\w+\.(txt|csv|log)\b")
# url_pattern = re.compile(r"\bhttps?://\S+\b")
# version_pattern = re.compile(r"\b\d+(\.\d+){2}\b")
# hostname_pattern = re.compile(r"\b[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\b")
# log_pattern = re.compile(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] (.+)")

# # Abrir el archivo de texto
# with open("integrador.txt", "r") as file:
#     # Inicializar el diccionario para almacenar los registros
#     registros = []

#     # Leer cada línea del archivo
#     for line in file:
#         registro = {}
#         line = line.strip()  # Eliminar los caracteres de nueva línea y espacios en blanco al inicio y final

#         # Buscar el hash en Git
#         match_commit = commit_pattern.search(line)
#         if match_commit:
#             registro["hash"] = match_commit.group()

#         # Buscar la dirección IP
#         match_ip = ip_pattern.search(line)
#         if match_ip:
#             registro["ip"] = match_ip.group()

#         # Buscar el correo electrónico
#         match_email = email_pattern.search(line)
#         if match_email:
#             registro["email"] = match_email.group()

#         # Buscar el nombre de archivo
#         match_file = file_pattern.search(line)
#         if match_file:
#             registro["archivo"] = match_file.group()

#         # Buscar la URL
#         match_url = url_pattern.search(line)
#         if match_url:
#             registro["url"] = match_url.group()

#         # Buscar el número de versión
#         match_version = version_pattern.search(line)
#         if match_version:
#             registro["version"] = match_version.group()

#         # Buscar el nombre de host
#         match_hostname = hostname_pattern.search(line)
#         if match_hostname:
#             registro["hostname"] = match_hostname.group()

#         # Buscar el registro de log
#         match_log = log_pattern.search(line)
#         if match_log:
#             registro["fecha"] = match_log.group(1)
#             registro["etiqueta"] = match_log.group(2)
#             registro["mensaje"] =  match_log.group(3)

#         # Agregar el registro al diccionario de registros
#         registros.append(registro)

# # Imprimir los registros
# for i, registro in enumerate(registros):
#     print(f"Registro {i+1}:")
#     for key, value in registro.items():
#         print(f"{key}: {value}")
    
#     print("-----------")