#include <Keyboard.h>
#include <Cytron_SmartDriveDuo.h>

int signalParLeft = 11; 
int signalParRight = 10;
int signalMidLeft = 5;
int signalMidRight = 3;

int directionParLeft = 7;
int directionParRight = 8;
int directionMidLeft = 4;
int directionMidRight = 2;

int translated = 0;

// initial speed
int LS = 0;
int RS = 0;
int MLS = 0;
int MRS = 0;


// bind wheels parallel
Cytron_SmartDriveDuo outer(PWM_INDEPENDENT, directionParLeft, directionParRight, signalParLeft, signalParRight);
Cytron_SmartDriveDuo inner(PWM_INDEPENDENT, directionMidLeft, directionMidRight, signalMidLeft, signalMidRight);

int onCount = 255;
char readthis;
//String stringPart1, stringPart2;
void setup() {
 // pinMode(13, OUTPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  
  digitalWrite(13, HIGH);
  delay(2000); // Delay for 5 seconds.
  digitalWrite(13, LOW);
//  digitalWrite(13, HIGH);
//  delay(2000); // Delay for 5 seconds.
//  digitalWrite(13, LOW);
  
  Serial.println("Move the controller");
}

void loop() {
    // put your main code here, to run repeatedly:
    if(Serial.available()) {
      readthis = (char)Serial.read();

    // gets values from two axis from the controller. idk how they are doing that so i will do that so i'm just including this comment
    // make sure to multiple the forward axis by 0.6 and the turn axis by .3 so that it never goes above 255
    
    set motors(controllerMotorConverter(forward), controllerMotorConverter(turn));
    }
}

void controllerMotorConverter(controller){
  // pygame controllers use -1 to 1 value, and the motor recieves value from -255 to 255, so we need to convert them

  c_stabilizer = 0.5 // how much we want to slow it down

  return controller * 250 * c_stabilizer
}

void setMotors(forward, turn){
      double left = forward + turn;
      double right = forward - turn;
       
      outer.control(left, right);
      inner.control(left, right);
}
