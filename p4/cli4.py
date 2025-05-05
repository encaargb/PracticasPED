#!/usr/bin/env python3
import socket
import os
import setproctitle

setproctitle.setproctitle("cli4")

SOCKET_PATH = os.environ.get("SOCKET_PATH", "/tmp/socket_grupo12")

ruta = input("Introduce la ruta del fichero: ")
if not ruta:
    print("[cli4] Ruta vacía, no se envía nada al servidor.")
    exit()

cliente = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

try:
    cliente.connect(SOCKET_PATH)
    cliente.sendall(ruta.encode())

    respuesta = cliente.recv(4096).decode()
    print("Respuesta del servidor:\n", respuesta)

except Exception as e:
    print(f"[cli4] ERROR al conectarse: {e}")

finally:
    cliente.close()
