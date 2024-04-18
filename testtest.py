import xmlrpc.client

url =  'https://ferromaya1.odoo.com'
db = 'ferromaya1'
username = 'api_odoo_test1@copantesa.com'
password = '8822063d73155aeac883ae109c996b0d8706c174'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())


uid = common.authenticate(db, username, password, {})
print (uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

result_facturas = models.execute_kw(db, uid, password, 'account.move', 'search_read',[[['id', '>',0 ]]],  {'fields': ['amount_total_signed', 'invoice_date', 'company_id' , 'state']})

print (result_facturas)
