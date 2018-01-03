S.O: Win 7
Python version: 3.6.4
MongoDB version: 3.6.1
Author: Andrés Ruda
Title: Techo Test

Prerrequisitos:
- Tener instalados Python y MongoDB en la máquina

Manual de uso
1. Para tener integridad en las librerías correr el Script init.bat de a carpeta set. Éste Script instalará las librerías necesarias e iniciará una instancia de MongoDB
2. Iniciar el servicio de consulta de campamentos ejecutando el script sert.bat de la carpeta set

Para el uso del servicio tomar como base la siguiente URL:
http://127.0.0.1:9000/?latitud=-33.45505&longitud=-70.62600&radio=0.06

Los campos de la URL se describen a continación:
latitud: 	Latitud base para la búsqueda
longitud: 	Longitud base para la búsqueda
radio:		Radio de búsqueda

El servicio ejecutado en el browser arrojará los resultados de la búsqueda en formato JSON

3. Abrir el archivo index.html en el browser (¡Qué no sea Internet Explorer por favor!) 
4. En el Sitio encontrará na caja de texto donde podrá ingresar el radio de búsqueda.
