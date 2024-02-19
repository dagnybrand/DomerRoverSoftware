#include <string.h>

const int RightPar = 2;
const int RightAna = 3;

const int LeftPar = 4;
const int LeftAna = 5;

const int MiddleLeft = 13;
const int MiddleRightA = 11;

const int MiddleRight = 12;
const int MiddleLeftA = 10;

int speed = 0;
char motion;
char prev;


void stopAll() {
    analogWrite(RightAna, 0);
    analogWrite(LeftAna, 0);

    analogWrite(MiddleRightA, 0);
    analogWrite(MiddleLeftA, 0);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(RightPar, OUTPUT);
  pinMode (RightAna, OUTPUT);
  analogWrite(RightAna, 0);

  pinMode (LeftPar, OUTPUT);
  pinMode (LeftAna, OUTPUT);
  analogWrite(LeftAna, 0);

  pinMode(MiddleLeft, OUTPUT);
  pinMode (MiddleLeftA, OUTPUT);
  analogWrite(MiddleLeftA, 0);

  pinMode (MiddleRightA, OUTPUT);
  pinMode (MiddleRight, OUTPUT);
  analogWrite(MiddleRightA, 0);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    int inputDis = Serial.read() - '0';
    speed = 40;
    switch(inputDis){
      case 1:
        digitalWrite(RightPar, LOW);
        digitalWrite(LeftPar, LOW);
        analogWrite(RightAna, speed);
        analogWrite(LeftAna, speed);

        digitalWrite(MiddleRight, LOW);
        digitalWrite(MiddleLeft, LOW);
        analogWrite(MiddleRightA, speed);
        analogWrite(MiddleLeftA, speed);
        break;
      case 2:
        digitalWrite(RightPar, HIGH);
        digitalWrite(LeftPar, HIGH);
        analogWrite(RightAna, speed);
        analogWrite(LeftAna, speed);

        digitalWrite(MiddleRight, HIGH);
        digitalWrite(MiddleLeft, HIGH);
        analogWrite(MiddleRightA, speed);
        analogWrite(MiddleLeftA, speed);
        break;
      case 3:
        digitalWrite(MiddleRight, HIGH);
        digitalWrite(MiddleLeft, LOW);
        analogWrite(MiddleRightA, speed);
        analogWrite(MiddleLeftA, speed);
        break;
      case 4:
        digitalWrite(MiddleRight, LOW);
        digitalWrite(MiddleLeft, HIGH);
        analogWrite(MiddleRightA, speed);
        analogWrite(MiddleLeftA, speed);
        break;
      default:
       stopAll();
       break;
       }
    
    }
    delay(10);
  stopAll();
}