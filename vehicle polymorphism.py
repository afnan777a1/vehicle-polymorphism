class Ferrari:
  def car_model(self):
    print("La Ferrari")
    
  def car_price(self):
    print("This car cost over 1 Million")

  def car_mileage(self):
    print("Mileage is 16 kmpl")

  def fuel_type(self):
    print("Fuel type is Petrol")
    
  def max_speed(self):
    print("Max speed is 350 km/h")
    
    
class BMW:
  def car_model(self):
    print("BMW m1")
    
  def car_price(self):
    print("This car cost over $556,333 Dollars")

  def car_mileage(self):
    print("Mileage is 16.29 kmpl")

  def fuel_type(self):
    print("Fuel type is Gasoline")
    
  def max_speed(self):
    print("Max speed is 265 km/h")
    
    
class MercedesBenz:
  def car_model(self):
    print("Mercedes T80")
    
  def car_price(self):
    print("This car cost over $4 Million")

  def car_mileage(self):
    print("Mileage is 2 kmpl")

  def fuel_type(self):
    print("Fuel type is Petrol")
    
  def max_speed(self):
    print("Max speed is 750 km/h")
    
    
class TATA:
  def car_model(self):
    print("Altroz Racer")
    
  def car_price(self):
    print("This car cost over 10 lakh")

  def car_mileage(self):
    print("Mileage is 19.33 kmpl")

  def fuel_type(self):
    print("Fuel type is Petrol")
    
  def max_speed(self):
    print("Max speed is 170 km/h")
    
    
class McLaren:
  def car_model(self):
    print("McLaren P1 GTR")
    
  def car_price(self):
    print("This car cost over $5 Million")

  def car_mileage(self):
    print("Mileage is 7 kmpl")

  def fuel_type(self):
    print("Fuel type is Petrol")
    
  def max_speed(self):
    print("Max speed is 349 km/h")
    
  
class RollsRoyce:
  def car_model(self):
    print("Rolls-Royce La Rose Noire Droptail")  

  def car_price(self):
    print("This car cost over $30 millionss")

  def car_mileage(self):
    print("Mileage is 16 kmpl")

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
    car.car_price()
    car.car_mileage()
    car.max_speed()
    car.fuel_type()
