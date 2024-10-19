class Ferrari:
  def car_model(self):
    print("La Ferrari")
    
  def fuel_type(self):
    print("Fuel type is Petrol")
    
  def max_speed(self):
    print("Max speed is 350 km/h")
    
    
class BMW:
  def car_model(self):
    print("BMW m1")
    
  def fuel_type(self):
    print("Fuel type is Gasoline")
    
  def max_speed(self):
    print("Max speed is 265 km/h")
    
    
class MercedesBenz:
  def car_model(self):
    print("Mercedes T80")
    
  def fuel_type(self):
    print("Fuel type is Petrol")
    
  def max_speed(self):
    print("Max speed is 750 km/h")
    
    
class TATA:
  def car_model(self):
    print("Altroz Racer")
    
  def fuel_type(self):
    print("Fuel type is Petrol")
    
  def max_speed(self):
    print("Max speed is 170 km/h")
    
    
class McLaren:
  def car_model(self):
    print("McLaren P1 GTR")
    
  def fuel_type(self):
    print("Fuel type is Petrol")
    
  def max_speed(self):
    print("Max speed is 349 km/h")
    
  
class RollsRoyce:
  def car_model(self):
    print("Rolls-Royce Ghost")  
    
  def fuel_type(self):
    print("Fuel type is Petrol")
    
  def max_speed(self):
    print("Max speed is 250 km/h")
    
ferrari = Ferrari()
bmw = BMW()
mercedesbenz = MercedesBenz()
tata = TATA()
mclaren = McLaren()
rollsroyce = RollsRoyce()
    
for car in (ferrari, bmw, mercedesbenz, tata, mclaren, rollsroyce):

    car.car_model()
    car.max_speed()
    car.fuel_type()