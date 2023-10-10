
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data == 'w') {
        drive_forward();
    }

    if (data == 'a') {
        turn_left();
    }

    if (data == 's') {
        drive_backward();
    }

    if (data == 'd') {
        turn_right();
    }
  }
}