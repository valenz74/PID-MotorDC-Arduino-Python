float pin10=10;
float cv = 20.0;
String valor = "";
float pwm1; // Variable del PWM 1
void setup() {
  pinMode(pin10, OUTPUT);  
  Serial.begin(9600); // Inicializar la comunicación serial a 9600 baudios
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read(); // Lee un carácter desde el puerto serie
    if (receivedChar != '\n') { // Ignora el carácter de nueva línea
      valor += receivedChar; // Agrega el carácter a la cadena
    } else { // Cuando se recibe una nueva línea, se considera que se ha completado la cadena
      cv = valor.toFloat(); // Convierte la cadena a un valor flotante
      analogWrite(pin10, cv);
      Serial.println(cv); // Imprime el valor del motor
      valor = ""; // Reinicia la cadena para la próxima lectura
    }
  }

}
