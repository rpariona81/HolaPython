import math
import mariadb
import sys

# for x in range(0, 6):
#     print(str(math.pow(2,x)) + " Hola a todos desde mi chromebook!")

# Instantiate Connection
try:
   conn = mariadb.connect(
      user="ronaldpa_123",
      password="joaquin",
      host="151.106.100.76",
      port=3306)
except mariadb.Error as e:
   print(f"Error connecting to MariaDB Platform: {e}")
   sys.exit(1)

# Instantiate Cursor
cur = conn.cursor()

# Adds contact
def add_usuario(cur, nombres, apellidos, cargo, usuario):
   """Adds the given usuario to the contacts table"""

   cur.execute("INSERT INTO ronaldpa_123.t_usuario(nombres, apellidos, cargo, usuario) VALUES (?, ?, ?, ?)",
      (nombres, apellidos, cargo, usuario))

new_contact_nombres = "Jhon"
new_contact_apellidos = "O'connor"
new_contact_cargo = 2
new_contact_usuario = "joconnor"

add_usuario(cur,
   new_contact_nombres,
   new_contact_apellidos,
   new_contact_cargo,
   new_contact_usuario)

# Close Connection
conn.close()
