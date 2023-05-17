# Proyecto-final-telematica
Diseño de un servicio telemático a nivel de producción que resuelva la visualización de los sensores de nivel de agua de la plataforma SIATA 


=======
# Pasos para realizar la instalacion de la aplicacion
El primer paso a realizar es la clonacion del repositorio

HTTPS
clon de git 
cd PythonApplication/https://github.com/Joaqui0845/Proyecto-final-telematica.git

SSH
clon de git https://github.com/Joaqui0845/Proyecto-final-telematica.git

# Cambio importante a realizar

 La ejecucion de esta aplicación es dentro de un entorno de nube,por lo que se modificara el archivo web.py y se debe cambiar la dirección localhost a su dirección IP pública.
 
 ![image](https://github.com/Joaqui0845/Proyecto-final-telematica/assets/116990982/756df952-b7f8-4b96-84d8-a00731cad125)

 Si por ejemplo se encuentra en la  nube, se debe habilitar el puerto 80 y el puerto 5600 en los grupos de seguridad
 ![image](https://github.com/Joaqui0845/Proyecto-final-telematica/assets/116990982/1ba126a1-baff-402b-8534-09ab38bea22d)

# Ejecucion de la aplicacion

Ejecutar inicio.sh
Este archivo actualizará el repositorio de paquetes e instalará docker compose junto con dos imágenes, mysql y ubuntu, finalmente, ejecutará el archivo docker-compose.yml, que creará tres contenedores.

 sudo sh ./inicio.sh
Otro sistema operativo**
> SI se tiene otro sistema operativo, debes descargar docker
> compose, y las imágenes manualmente (mysql, ubuntu), y finalmente ejecutar el archivo
> docker-compose.yml
# Finalmente
debemos esperar un poco, hasta que los tres contenedores este corriendo de forma correcta
> ingrese su host local o IP pública a través del puerto 80

> SI es primera vez que se ingresa tienes que realizar el registro

