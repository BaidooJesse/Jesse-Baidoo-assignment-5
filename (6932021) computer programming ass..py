#Define a dictionary of available cars and their prices 
cars = {"Benz c300" : 400000,"Escalade":500000,"Toyota Camry":50000,"Tesla model x":400000,"BMW M5":600000,"Lexus rx":20000,"vw":20000,"Buick":300000,"Audi Q7":300000,"kia rio":33000,"Hyundai Elantra":80000,"Porsche":45000,"Ford Ranger":60000,"Honda Crv":45000,"Subaru":33000,"Mini Cooper":11000,"Aston Martin":300000,"Chevrolet impala":80000,"Nissan March":11000,"Jeep":34000,"Dodge":35000,"volvo":11000,"land Rover":5000000,"Range Rover":3000000,"G.Wagon":300000000,"Ibiza":5000,"Accent":3000,"Avantedor":4000000,"Chiron":4000000,"Veyron":20000,"Mazda":20000}
# Ask the user for their car brand preference
car_brand = input("Enter the car brand you are looking for:")
# Check if the car is available in the dealership
if car_brand in cars:
    print("Yes, the car is available.")
    print("The sales price of the car is :",cars[car_brand])
else:
    print("Sorry the car is not available at the moment.")

