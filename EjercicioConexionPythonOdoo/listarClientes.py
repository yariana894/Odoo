import xmlrpc.client as xmlrpclib

URL = "http://localhost:8069"
USER = "yariana894@gmail.com"
PASSWORD = "Ad1234"
BD = "cebem"

# clave api
# 50add66396badcacb590254a8a32db45ab391d5e

# Conectamos con el api de odoo
odoo = xmlrpclib.ServerProxy(URL + '/xmlrpc/2/common')

try:
    version = odoo.version()
    print(version.get('server_version'))
except:
    print("No podemos conectar con Odoo")
    exit(1)

# Logueamos en el sistema
uid = odoo.authenticate(BD, USER, PASSWORD, {})
print(uid)

# obtenemos el modelo
models = xmlrpclib.ServerProxy(URL + '/xmlrpc/2/object')

try:
    models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})
except xmlrpclib.Fault as ex:
    print('No tienes para leer datos', ex)
    exit(1)

# PARA EJECUTAR UNA LISTA por compañías
clientes = models.execute_kw(BD, uid, PASSWORD,
                             'res.partner',
                             'search_read',
                             [[['is_company', "=", True]]],
                             {'fields': ['phone', 'email', 'name',
                                         'website']})  # ,'limit': 4 limit es opcional, solo por si queremos limitar la busqueda
# {'fields': ['phone', 'email', 'name', 'website'],'limit': 4})

print('Encontrado', len(clientes), 'clientes')

for cliente in clientes:
    print('Cientes')
    print('\tNombre: ', cliente.get('name'))
    print('\tTelefono: ', cliente.get('phone'))
    print('\tEmail: ', cliente.get('email'))
    print('\tSitio web: ', cliente.get('website'))

### Contar clientes
# cuentaClientes = models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'search_count', [[['is_company', '=', True]]])
# print("Encontrados: ", cuentaClientes)

### Crear un contacto
# id = models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'create', [{'name': "Hola", }])
# print(id)

### MODIFICAR el nombre del cliente
# EN EL ID SE PONE EL ID DEL CLIENTE QUE QUEREMOS MODIFICAR
# models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'write', [[id], {'name': "Hola"}])
# get record name after having changed it
# models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'name_get', [[id]])

### BUSCAR todos los ids de los contactos
partner = models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'search', [[]])
print("Partner=", partner)

### BUSCAR el id y nombre de los contactos
# EN EL ID SE PONE EL ID DEL CLIENTE QUE QUEREMOS MODIFICAR
# leer = models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'read', [partner], {'fields': ['name']})
# print(leer, "\t")

### Borrar un contacto
# EN EL ID SE PONE EL ID DEL CLIENTE QUE QUEREMOS MODIFICAR
# id = 48
# models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'unlink', [[id]])
# ver = models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'search', [[['id', '=', id]]])
# print(ver)



