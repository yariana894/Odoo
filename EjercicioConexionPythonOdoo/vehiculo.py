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
    models.execute_kw(BD, uid, PASSWORD, 'fleet.vehicle', 'check_access_rights', ['read'], {'raise_exception': False})
except xmlrpclib.Fault as ex:
    print('No tienes para leer datos', ex)
    exit(1)

# TODOS LOS VEHICULOS
vehiculos = models.execute_kw(BD, uid, PASSWORD, 'fleet.vehicle', 'search', [[]])
print("Vehiculos=", vehiculos)

# VEHICULOS CON ID
leer = models.execute_kw(BD, uid, PASSWORD, 'fleet.vehicle', 'read', [vehiculos], {'fields': ['model_id']})
print(leer, "\t")

# VEHICULOS CON MATRICULA
license_plate = input("Introduce la matrícula que quiera: ")
ids = models.execute_kw(BD, uid, PASSWORD, 'fleet.vehicle', 'search', [[['license_plate', '=', license_plate]]])
print(ids)

# APARTADO 3 FUNCIONA
vehiculos = models.execute_kw(BD, uid, PASSWORD,
                              'fleet.vehicle',
                              'search_read',
                              [[['license_plate', '=', license_plate]]],
                              {'fields': ['id', 'license_plate', 'odometer'], })

print('Encontrados ', len(vehiculos), 'vehiculos')

for vehiculo in vehiculos:
    print('Proveedor')
    vehid = vehiculo.get('id')
    vehmatr = vehiculo.get('license_plate')
    vehodo = vehiculo.get('odometer')
    models.execute_kw(BD, uid, PASSWORD, 'fleet.vehicle', 'write', [[vehid], {'odometer': vehodo + 10}])
    print('\tId: ', vehid)
    print('\tMatrícula: ', vehmatr)
    print('\tOdometer: ', vehodo)
