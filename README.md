# Resuelve
##Esta es un examen para candidatos en Resuelve :)

Lo primero que haremos es instalar el gestor de dependencias de python que es pip.
Tanto en Windows y macOS, ademas de la mayoria de las distribuciones de Linux pip ya viene instalado.
Lo podemos comprobar con el comando 
```
pip --version
```
Luego instalamos el entorno virtualque nos va a permitir instalar dependencias y que no entren en conflicto con otras ya existentes en el sistema

Utilizamos el comando 
```
pip install virtualenv     
```
Luego creamos el entorno virtual 
```
virtualenv env
```
Luego se activa

macOS y Linux 
```
source env/bin/activate
```
Windows 
```
.\env\Scripts\activate
```
 A prtir de aqui instalamos nuestras dependencias 
```
pip install -r requirements.txt
```

Y listo podemos correr nuestra aplicacion
Se corre con el siguiente comando 
python test_resuelve.py

Las pruebas de corren de esta forma
python _testr_resuelve.py ResuelveTests.test_get_medium_date

Hasta luego !:)
                 
