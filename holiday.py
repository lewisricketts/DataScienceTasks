# Define flights and hotel costs dictionaries
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

hotel_costs = {
    'Paris': 100,
    'Berlin': 90,
    'Barcelona': 100,
    'Rome': 75,
    'New York': 200,
    'Cairo': 50,
    'Amsterdam': 90,
    'La Reunion': 60
}

# Display flight destinations and prices
print("\nWelcome to HyperionDev Travel - please find below the potential flight destinations and prices: \n")
for destination, price in flights.items():
    print(f"Destination: {destination}, Price: £{price}")

# Display hotel costs for each destination
print("\nThese are the hotel costs for the following destinations also: \n")
for destination, price in hotel_costs.items():
    print(f"Hotel cost per night for {destination}: £{price}")

# Creaated user defined functions to calculate hotel cost, flight costs and rental car costs.
def hotel_cost(num_nights, destination):
    if destination in hotel_costs:
        return num_nights * hotel_costs[destination]
    else:
        print("Error detected. Please try again")

def plane_cost(destination):
    if destination in flights: # Loops the destination in the flights dictionary
        return flights[destination] * 2  # Plane cost based on flight price for return journey - returns the cost of the destination and multiplies by 2 for return journey
    else:
        print("Error detected. Please try again")

def car_rental(rental_days):
    return rental_days * 50  # Fixed rental fee per day (could have made this into a dictionary)

def holiday_cost(total_hotel, total_plane, total_car):
    return total_hotel + total_plane + total_car

# Prompt user for destination and number of nights
city_flight = input("Enter the destination you are traveling to: ").strip() #removes any whitespace to prevent errors occuring
num_nights = int(input("How many nights will you be staying at the hotel? "))

# Calculate hotel cost
total_hotel = hotel_cost(num_nights, city_flight)

# Calculate plane cost
total_plane = plane_cost(city_flight)

# Prompt user for rental days and calculate car rental cost
rental_days = int(input("How many days will you be hiring a car for? "))
total_car = car_rental(rental_days)

# Calculate total holiday cost
total_holiday_cost = holiday_cost(total_hotel, total_plane, total_car)

# Output booking details and total costs
print("\nCongratulations! You have successfully booked a holiday with HyperionDev Travel!")
print(f"You will be staying in {city_flight} for {num_nights} nights.")
print(f"Hotel cost: £{total_hotel}")
print(f"Plane cost: £{total_plane}")
print(f"Car rental cost: £{total_car}")
print(f"Total holiday cost: £{total_holiday_cost}")
print("Thank you for booking with HyperionDev Travel! Bon Voyage!")
