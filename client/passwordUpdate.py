import subprocess

def update_password(username, new_password):
  """Actualiza la clave de un usuario en Windows Server.

  Args:
    username: El nombre de usuario del usuario a actualizar.
    new_password: La nueva contraseña del usuario.
  """

  # Configuramos el comando para actualizar la clave.
  command = [
      "net",
      "user",
      username,
      "new",
      "password",
      new_password,
  ]

  # Ejecutamos el comando.
  output = subprocess.run(command, capture_output=True)

  # Verificamos el resultado del comando.
  if output.returncode != 0:
    raise Exception(output.stderr)


if __name__ == "__main__":
  # Solicitamos al usuario el nombre de usuario y la nueva contraseña.
  username = input("Ingrese el nombre de usuario: ")
  new_password = input("Ingrese la nueva contraseña: ")

  # Actualizamos la clave del usuario.
  update_password(username, new_password)

  # Imprimimos un mensaje de éxito.
  print("La clave del usuario ha sido actualizada correctamente.")
