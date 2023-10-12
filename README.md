<center><h1>Control PID MOTORDC CON ARDUINO Y PYTHON</h1></center> 

Este proyecto muestra cómo controlar la velocidad de un motor DC utilizando un Arduino y Python. El control se implementa utilizando un controlador PID.


<h2>Hardware necesario</h2>

* Un Arduino.
* Un motor DC.
* Un cable USB para conectar el Arduino a la computadora.
* Puente H L298N.
* Bateria 9V o fuente externa.

![img](https://github.com/MSL01/PID-MotorDC-Arduino-Python/assets/100708772/6be15cfb-de6a-48f7-b416-0e5a3d0306e9)



<h2>Librerías utilizadas.</h2>

El proyecto utiliza las siguientes librerías:

* ```tkinter:``` Para crear la interfaz gráfica de usuario.
* ```control:``` Para implementar el controlador PID.
* ```numpy:``` Para realizar cálculos matemáticos.
* ```matplotlib:``` Para crear gráficos.
* ```serial:``` Para comunicarse con el Arduino.
* ```time:``` Para controlar el tiempo.
* ```simple_pid:``` Para implementar un controlador PID simple.


<h2>Cómo funciona el proyecto</h2>
El proyecto funciona de la siguiente manera:

* El Arduino lee la velocidad actual del motor DC utilizando el encoder.
* La velocidad actual del motor DC se envía a la computadora a través de la comunicación serial.
* El programa de Python calcula el error entre la velocidad actual y la velocidad deseada.
* El controlador PID calcula la acción de control necesaria para reducir el error.
* La acción de control se envía al Arduino a través de la comunicación serial.
* El Arduino ajusta la velocidad del motor DC en función de la acción de control.
  

<h2>Gráficos</h2>

El proyecto también incluye una función para crear gráficos de la velocidad actual y la velocidad deseada del motor DC. Para crear el gráfico, simplemente haga clic en el botón "Conectar" en la interfaz gráfica de usuario.

![Captura2](https://github.com/MSL01/PID-MotorDC-Arduino-Python/assets/100708772/5863a705-a6a5-400e-a0f1-40e2daf59306)

![Captura](https://github.com/MSL01/PID-MotorDC-Arduino-Python/assets/100708772/bb2f0364-a5df-4a6f-9491-c450d23ba37b)


<h2>Sintonización del controlador PID</h2>

Los parámetros del controlador PID (Kp, Ki y Kd) se pueden ajustar para optimizar el rendimiento del sistema. Para sintonizar el controlador PID, siga los siguientes pasos:

* Aumente la ganancia proporcional (Kp) hasta que el sistema comience a oscilar.
* Reduzca la ganancia proporcional (Kp) hasta que el sistema deje de oscilar.
* Aumente la ganancia integral (Ki) hasta que el error estacionario se reduzca a un valor aceptable.
* Aumente la ganancia derivativa (Kd) para mejorar la respuesta del sistema a los cambios repentinos en la velocidad deseada.
