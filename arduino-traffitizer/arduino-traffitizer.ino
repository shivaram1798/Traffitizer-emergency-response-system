int data;
int led1=5;
int led2=16;
int led3=4;
void setup() 
{ 
  Serial.begin(9600); 
  pinMode(led1, OUTPUT); 
  pinMode(led2, OUTPUT);
  pinMode(led3,OUTPUT);
  digitalWrite (led1,LOW); //GREEN SIGNAL
  digitalWrite (led2,LOW);//RED SIGNAL
  digitalWrite (led3,LOW);//ORANGE SIGNAL
}
void loop() 
{
 while(Serial.available())
  {
    data = Serial.read();
  }
  if (data == '1')
  {
  digitalWrite (led3,HIGH);//ORANGE SIGNAL ON
  delay(100);
  digitalWrite (led3,LOW);//ORANGE SIGNAL OFF*/
  digitalWrite (led1, HIGH);// GREEN SIGNAL ON
  digitalWrite(led2,LOW);//RED SIGNAL OFF
  delay(1000);
  }
  if (data == '0')
  {
  digitalWrite (led1,LOW);//GREEN SIGNAL OFF
  digitalWrite (led2, HIGH);//RED SIGNAL ON
  delay(1000);
  }
}
