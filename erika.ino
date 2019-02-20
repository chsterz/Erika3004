
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
int inPin = 3;


void setup() {
  // Open serial communications and wait for port to open:
  pinMode(inPin, INPUT);
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }


  Serial.println("Goodnight moon!");

  // set the data rate for the SoftwareSerial port
  mySerial.begin(1200);
}
bool wait = false;
void loop() { // run over and over
   int val = digitalRead(inPin);
   Serial.println(val);
    if(val == LOW && wait == false)
     {
          if (Serial.available()) {
            mySerial.write(Serial.read());
  }
        wait = true;
     }
     else {
        wait = false;
     }

}

//char ddr2ascii(char val)
//{
//  switch(val)
//  {
//    case "a":
//     return "";
//    case "b":
//    return "";
//  }
//}
//
//char ascii2ddr(char val)
//{
//}
//}
