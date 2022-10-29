from ejemplo.models import Familiar
import datetime

Familiar(nombre="Rossana", direccion="Rio Parana 745", numero_pasaporte=123123,fecha=datetime.date.today()).save()
Familiar(nombre="Luis", direccion="Rio Parana 745", numero_pasaporte=890890,fecha=datetime.date.today()).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345,fecha=datetime.date.today()).save()
Familiar(nombre="Carolina", direccion="Rio Parana 745", numero_pasaporte=567567,fecha=datetime.date.today()).save()

print("Se cargo con éxito los usuarios de pruebas")