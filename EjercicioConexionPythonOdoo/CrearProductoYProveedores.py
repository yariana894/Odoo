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
    models.execute_kw(BD, uid, PASSWORD, 'product.template', 'check_access_rights', ['read'],
                      {'raise_exception': False})
except xmlrpclib.Fault as ex:
    print('No tienes para leer datos', ex)
    exit(1)

    # listar etiquetas
    # LA IMAGEN NO SE INSERTA==================
    # productos = models.execute_kw(BD, uid, PASSWORD, 'product.template', 'create', [
    #     {
    #         'name': "DJI Phantom 4 PRO Plus",
    #         'sale_ok': 'true',
    #         'purchase_ok': 'true',
    #         'detailed_type': 'product',
    #         'list_price': 2.34,
    #         'standard_price': 1000,
    #         'image_1920': 'https://ih1.redbubble.net/image.565650625.0721/flat,750x,075,f-pad,750x1000,f8f8f8.u6.jpg',
    #     }
    # ])

# imprime las etiquetas de contactos
partner = models.execute_kw(BD, uid, PASSWORD, 'res.partner.category', 'search', [[]])

leer = models.execute_kw(BD, uid, PASSWORD, 'res.partner.category', 'read', [partner], {'fields': ['name']})
print(leer, "\t")

# Crear un proveedor
# models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'create', [
#     {
#         'company_type': 'company',
#         'name': 'PullAndBear',
#         'phone': '+34 900 814 900',
#         'email': 'compras@zara.es',
#         'street': 'Avenida Deputacion Arteixo. 15142. A Coruña',
#         'website': 'https://zara.es/',
#     }
# ])

# sacar el nombre del contacto con el id introducido entre []
nombre = models.execute_kw(BD, uid, PASSWORD, 'res.partner', 'name_get', [[7]])
print(nombre)

# PARA EJECUTAR UNA LISTA de los proveedores que sean proveedores
proveedores = models.execute_kw(BD, uid, PASSWORD,
                                'res.partner',
                                'search_read',
                                [[['is_company', '=', True], ['category_id', '=', [5]]]],
                                {'fields': ['name', 'phone', 'email',
                                            'website', 'category_id', 'child_ids'], })

print('Encontrados ', len(proveedores), 'proveedores')

for proveedor in proveedores:
    print('Proveedor')
    print('\tNombre: ', proveedor.get('name'))
    print('\tTelefono: ', proveedor.get('phone'))
    print('\tEmail: ', proveedor.get('email'))
    print('\tSitio web: ', proveedor.get('website'))
    print('\tcategoria: ', proveedor.get('category_id'))
    print('\tChilds: ', proveedor.get('child_ids'))
