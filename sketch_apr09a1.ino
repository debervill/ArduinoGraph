    // библиотека для работы с аналоговым акселерометром
     #include <TroykaAccelerometer.h>
     
    // пины подключения осей акселерометра
    #define PIN_X A1
    #define PIN_Y A2
    #define PIN_Z A0
     
    // калибровочные значения одного из акселерометров
    // для получения своих калибровочных значений воспользуйтесь скетчем «AccelerometerCalibration»
    #define MIN_X   1.172
    #define MAX_X   1.763
    #define MIN_Y   1.162
    #define MAX_Y   1.831
    #define MIN_Z   1.221
    #define MAX_Z   1.802

    
     
    // создаём объект для работы с аналоговым акселерометром
    TroykaAccelerometer accel(PIN_X, PIN_Y, PIN_Z);
     
    void setup() {
      // открываем последовательный порт
      Serial.begin(9600);
      // каждый акселерометр необходмо калибровать индивидуально
      // для получения калибровочных значений воспользуйтесь скетчем «AcelerometerCalibration»
      // калибруем акселерометр по калибровочным значениям одного из партии
      accel.calibrate(MIN_X, MAX_X, MIN_Y, MAX_Y, MIN_Z, MAX_Z);
    }
     
    void loop() {
    
      // выводим направление и величины ускорения в «м/с²»
      Serial.print(accel.readAX());
      Serial.print("\t");      
      Serial.print(accel.readAY());
      Serial.print("\t");
      Serial.println(accel.readAZ());
      Serial.print("\t");
      delay(100);
      
      
  
        }
