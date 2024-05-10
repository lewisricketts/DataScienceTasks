flights = {
    'Paris': 80,
    'Berlin': 90,
    'Barcelona': 100,
    'Rome': 150,
    'New York': 500,
    'Cairo': 400,
    'Amsterdam': 130,
    'La Reunion': 1000
}

hotel_costs = {'Paris' : 100, 'Berlin' : 90, 'Barcelona' : 100, 'Rome' : 75, 'New York': 200, 'Cairo' : 50, 'Amsterdam': 90, 'La Reunion' : 60}
print("\n")
print("Welcome to HyperionDev Travel - please find below the potential flight destinations and prices: \n")
for destination, price in flights.items():
    print(f"Destination: {destination.title()}, Price: £{price}")
print("\n")
print("These are the hotel costs for the following destinations also: \n ")
for destination, price in hotel_costs.items():
    print(f"Hotel cost per night for {destination.title()} is £{price}")

cost_hotel = hotel_costs["price"]
plane_cost = flights["price"]

def hotel_cost(num_nights, cost_hotel):
    total_hotel = num_nights * cost_hotel
    return total_hotel #returns the total_hotel value and stores it 

# Plane_cost function uses from an if else that if it is Paris then it costs 150 and anywhere else typed = 75. It multiplies this by 2 for the return journey. Stores cost as total_plane

def plane_cost(base_cost,y=2):
    total_plane = base_cost * y
    return total_plane
    
#car_rental function mutliples rental days by a standard fee of 50 and stores this value as total_car
def car_rental(rental_days):
    total_car = rental_days * 50
    return int(total_car)

#holiday_cost function is the total of total_car plus total_plane plus total_hotel. It stores this sum in total_holiday_cost
def holiday_cost(total_hotel, total_plane, total_car):
    total_holiday_cost = total_car + total_plane + total_hotel
    return total_holiday_cost

#functions are at the top of the code as this is good practice

#asks the user for the city they're travelling to and stores as the variable city_flight

#asks the user how many nights they will be staying and casts this as an integer
#calls the total_hotel function
num_nights = int(input("How many nights will you be staying at the hotel?"))
total_hotel = int(hotel_cost(num_nights))

#asks the user how many rental days the car will be rented for 
#calls the total_car and returns the total_car value
rental_days = int(input("How many days will you be hiring a car for?"))
total_car = int(car_rental(rental_days))

total_holiday_cost = total_hotel + total_plane + total_car

# print(f"Your hotel costs are £{total_hotel}")
# print(f"Your plane cost is £") + {total_plane}""
# print(f"Your car rental come to £") + {total_car}
# print(f"Your total holiday comes to £") + {total_holiday_cost}
# print("Thanks so much for booking with HyperionDev Travel! Bon Voyage!")
#The above doesn't print correctly because the f-string {} needs to be surrounded by speech marks and bracket not using the + sign


print(f"Congratulations you have successfully booked a holiday to {city_flight}!")
print(f"You will be staying for {num_nights} nights and will have access to a car for {rental_days} days")
print(f"Your hotel costs are: £{total_hotel}")
print(f"Your plane cost is: £{total_plane}")
print(f"Your car rental comes to: £{total_car}")
print(f"Your total holiday comes to £{total_holiday_cost}")
print("Thanks so much for booking with HyperionDev Travel! Bon Voyage!")