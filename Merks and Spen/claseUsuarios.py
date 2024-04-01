class Usuario:
    def __init__(self, id_usuario, username, password, nombre_completo, correo, id_rol, id_departamento):
        self.id_usuario = id_usuario
        self.username = username
        self.password = password
        self.nombre_completo = nombre_completo
        self.correo = correo
        self.id_rol = id_rol
        self.id_departamento = id_departamento

class Rol:
    def __init__(self, id_rol, nombre, descripcion):
        self.id_rol = id_rol
        self.nombre = nombre
        self.descripcion = descripcion

class Departamento:
    def __init__(self, id_departamento, nombre, descripcion):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.descripcion = descripcion
