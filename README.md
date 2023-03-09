# Topicos Especiales de Telematica - Reto Practico 1

## Información de la asignatura

Desplegar tres microservicios en dos lenguajes de programación distintos, una ApiGW y asegurar que se comuniquen entre ellos.

## Titulo del Proyecto

Reto Telematica 1

## Datos del Estudiante

Nombre:
Jose Manuel Fonseca Palacio

## Descripción y alcance del proyecto

El proyecto consiste en el despliegue de tres microservicios en lenguajes de programación distintos, una ApiGW. Se diseño una aplicación web de ventas en linea. Para los microservicios se utilizo python en cuanto a un Catalogo y un carro, y go para el servicio de pago.
## Estructura del proyecto


El proyecto contiene 5 carpetas.

La primera que es API, contiene el servidor desde donde se pueden hacer las llamadas a los otros microservicios

La segunda que es Cart, la cual contiene cuatro carpetas más, una llamada python que contiene el micro-servicio Cart, include y tools que contiene algunas librerias necesarias y protos que incluye los .proto necesarios para el funcionamiento de cart.

La tercera es Catalog, la cual contiene cuatro carpetas más, una llamada python que contiene el micro-servicio Catalog, include y tools que contiene algunas librerias necesarias y protos que incluye los .proto necesarios para el funcionamiento de catalog.

La cuarta es Paymentp, la cual tiene un archivo llamado grpc-go, dentro de la cual hay multiples carpetas para el funcionamiento de go, dentro de code, habran dos carpetas, una llamada PaymentWork y data, dentro PaymentWork habran dos carpetas más, una llamada protos, que son los .proto necesarion para el funcionamiento de payment, y una llamada Payment que es donde se encuentra el micro-servicio de payment.

La quinta es imgenes contiene imagenes para la documentación.

## Arquitectura de la solución planteada.

![alt text](https://github.com/jmfonsecap/TelematicaReto1/blob/main/image.jpg?raw=true)

## Resultados Logrados

- Se logro implementar los tres microservicios e intercomunicarlos entre ellos por medio de un RPC a pesar de que estos estuvieran en lenguajes de programación distintos.
- Se logro implementar un ApiGW que se comunique con los tres microservicios y se pueda comunicar con esta a traves de postman. 
- Se logro desplegar la aplicación en AWS en 4 maquinas distintas.

## Descripción tecnica de la solución implementada

La aplicación consta de tres microservicios y un ApiGW, los microservicios Catalog, Cart y APIGW estan implementados en el lenguaje Python, usando el framework Bottle para el APIGW, por su lado el microservicio Payment esta implementado en Go.


### Cart microservice

Requisitos:

- python v3.11.2^
- git v2.39^

Proceso de instalación y despliegue:

Primero se actualiza
```sh
 $ sudo apt-get update
 $ sudo apt-get upgrade
```
Luego proceda a instalar python3 así como actualizad pip:

```sh
 $ sudo apt-get install python3
 $ sudo apt-get install python3-pip
```
Instale las librerias requeridas para gRPC:
```sh
$ sudo python3 -m pip install grpcio
$ sudo python3 -m pip install grpcio-tools
```
Ahora, se clona el repositorio donde está el código:

```sh
$ sudo git clone https://github.com/jmfonsecap/TelematicaReto1
```

Se mueve a la carpeta del microservicio Cart


```sh
$ cd TelematicaReto1/Back/Cart
```

Se edita el archivo cambiando la variable en grpc.insecure_channel('18.204.5.43:8080') por la ip en donde se despliega el catalogo.

```sh
$ sudo nano cart.py
```

- Se despliega el servicio 

```sh
$ sudo python3 cart.py
```

### Catalog microservice

Requisitos:

- python v3.11.2^
- git v2.39^

Proceso de instalación y despliegue:

Primero se actualiza
```sh
 $ sudo apt-get update
 $ sudo apt-get upgrade
```
Luego proceda a instalar python3 así como actualizad pip:

```sh
 $ sudo apt-get install python3
 $ sudo apt-get install python3-pip
```
Instale las librerias requeridas para gRPC:
```sh
$ sudo python3 -m pip install grpcio
$ sudo python3 -m pip install grpcio-tools
```
Ahora, se clona el repositorio donde está el código:

```sh
$ sudo git clone https://github.com/jmfonsecap/TelematicaReto1
```

Se mueve a la carpeta del microservicio Catalog


```sh
$ cd TelematicaReto1/Back/Catalog
```

- Se despliega el servicio 

```sh
$ sudo python3 cart.py
```

### Payment microservice

Requisitos:

- go v1.17.5^
- git v2.39^

Proceso de instalación y despliegue:

Primero se actualiza
```sh
 $ sudo apt-get update
 $ sudo apt-get upgrade
```
Se pasa a la carpeta /temp para asi instalar go

```sh
$ cd /tmp
$ wget https://go.dev/dl/go1.17.5.linux-amd64.tar.gz
$ tar -C /usr/local -xzf go1.17.5.linux-amd64.tar.gz
$ export GOPATH=$HOME/go
$export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
$ exec $SHELL
```

Vuelva a la carpeta principal
```sh
 $ cd ../home/ubuntu
```
Instale las librerias requeridas para protocol compiler plugins
```sh
$ go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.28
$ go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2
$ export PATH="$PATH:$(go env GOPATH)/bin"
```
Ahora, se clona el repositorio donde está el código:

```sh
$ sudo git clone https://github.com/jmfonsecap/TelematicaReto1
```

Se mueve a la carpeta del microservicio Cart


```sh
$ cd TelematicaReto1/Back/Paymentp/code/PaymentWork/Payment
```

Se edita el archivo cambiando la variable addr por la ip en donde se despliega el cart.

```sh
$ sudo nano main.go
```

- Se despliega el servicio 

```sh
$ sudo go run main.go
```

### Api GateWay

Requisitos:

- python v3.11.2^
- git v2.39^

Proceso de instalación y despliegue:

Primero se actualiza
```sh
 $ sudo apt-get update
 $ sudo apt-get upgrade
```
Luego proceda a instalar python3 así como actualizad pip:

```sh
 $ sudo apt-get install python3
 $ sudo apt-get install python3-pip
```
Instale las librerias requeridas para gRPC:
```sh
$ sudo python3 -m pip install grpcio
$ sudo python3 -m pip install grpcio-tools
```
Ahora, se clona el repositorio donde está el código:

```sh
$ sudo git clone https://github.com/jmfonsecap/TelematicaReto1
```

Se mueve a la carpeta del APIGw


```sh
$ cd TelematicaReto1/Back/API
```
Se instala bottle

```sh
$ pip install bottle
```
- Se despliega el servicio 

```sh
$ sudo python3 service.py
```
## Guía de uso


