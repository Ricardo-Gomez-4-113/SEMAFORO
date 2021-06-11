import time
calle = input("¿Para que calle estara hecho el semaforo 1.-Baja 2.-Media 3.-Alta?\n")
hora = input("¿En que hora se estara utilizando el semaforo el semaforo 1.-Baja 2.-Media 3.-Alta?\n")
if (calle == '1' and hora == '1'):
	print("El semaforo se confuguro para una calle baja en una hora baja")
	while True:
		print("Verde")
		time.sleep(35)
		print("Rojo")
		time.sleep(15)
		print("Amarillo")
		time.sleep(15)
if (calle == '2' and hora == '2'):
	print("El semaforo se confuguro para una calle media en una hora media")
	while True:
		print("Verde")
		time.sleep(60)
		print("Rojo")
		time.sleep(15)
		print("Amarillo")
		time.sleep(15)
if (calle == '3' and hora == '3'):
	print("El semaforo se confuguro para una calle alta en una hora alta")
	while True:
		print("Verde")
		time.sleep(150)
		print("Rojo")
		time.sleep(15)
		print("Amarillo")
		time.sleep(15)
	
if (calle == '1' and hora == '2'):
	print("El semaforo se confuguro para una calle baja en una hora media")
	while True:
		print("Verde")
		time.sleep(45)
		print("Rojo")
		time.sleep(15)
		print("Amarillo")
		time.sleep(15)
if (calle == '1' and hora == '3'):
	print("El semaforo se confuguro para una calle baja en una hora alta")
	while True:
		print("Verde")
		time.sleep(50)
		print("Rojo")
		time.sleep(15)
		print("Amarillo")
		time.sleep(15)
if (calle == '2' and hora == '1'):
	print("El semaforo se confuguro para una calle media en una hora baja")
	while True:
		print("Verde")
		time.sleep(45)
		print("Rojo")
		time.sleep(15)
		print("Amarillo")
		time.sleep(15)
if (calle == '2' and hora == '3'):
	print("El semaforo se confuguro para una calle media en una hora alta")
	while True:
		print("Verde")
		time.sleep(45)
		print("Rojo")
		time.sleep(15)
		print("Amarillo")
		time.sleep(15)
if (calle == '3' and hora == '1'):
	print("El semaforo se confuguro para una calle alta en una hora baja")
	while True:
		print("Verde")
		time.sleep(50)
		print("Rojo")
		time.sleep(15)
		print("Amarillo")
		time.sleep(15)
if (calle == '3' and hora == '2'):
	print("El semaforo se confuguro para una calle alta en una hora media")
	while True:
		print("Verde")
		time.sleep(45)
		print("Rojo")
		time.sleep(15)
		print("Amarillo")
		time.sleep(15)