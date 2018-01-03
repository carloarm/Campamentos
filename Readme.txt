S.O: Win 7
Python version: 3.6.4
MongoDB version: 3.6.1
Author: Andr�s Ruda
Title: Techo Test

Prerrequisitos:
- Tener instalados Python y MongoDB en la m�quina

Manual de uso
1. Para tener integridad en las librer�as correr el Script init.bat de a carpeta set. �ste Script instalar� las librer�as necesarias e iniciar� una instancia de MongoDB
2. Iniciar el servicio de consulta de campamentos ejecutando el script sert.bat de la carpeta set

Para el uso del servicio tomar como base la siguiente URL:
http://127.0.0.1:9000/?latitud=-33.45505&longitud=-70.62600&radio=0.06

Los campos de la URL se describen a continaci�n:
latitud: 	Latitud base para la b�squeda
longitud: 	Longitud base para la b�squeda
radio:		Radio de b�squeda

El servicio ejecutado en el browser arrojar� los resultados de la b�squeda en formato JSON

3. Abrir el archivo index.html en el browser (�Qu� no sea Internet Explorer por favor!) 
4. En el Sitio encontrar� na caja de texto donde podr� ingresar el radio de b�squeda.
