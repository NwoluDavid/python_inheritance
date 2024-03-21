"""Assignment 2 , ex 9.5""" 
################################################################################

class Restaurant:
    def __init__(self, name, cuisine_type) -> None:
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant called {self.name} offers {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open and offers {self.cuisine_type}")

    def set_number_served(self, served_customers: int):
        self.number_served = served_customers
        print(f"We have served {self.number_served} customers")

    def increment_number_served(self, new_customers: int):
        self.number_served += new_customers
        print(f"We served {new_customers} more customers today. Total: {self.number_served}")


class IceCreamStand(Restaurant):
    """Represent aspects of restaurants, specific to Ice Cream Restaurants."""

    def __init__(self, name, cuisine_type, flavors) -> None:
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f" \n We offer the following flavors:")
        for flavor in self.flavors:
            print("-", flavor)


# question 9.6
ice_cream_stand = IceCreamStand("Coldstone", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
# ice_cream_stand.describe_restaurant()
# ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavors()



           
class Users:
    
    """simulating real-life  user"""
    def __init__(self, first_name , last_name , gender , email ) -> None:
        self.first_name=first_name
        self.last_name= last_name
        self.gender= gender
        self.email=email
        self.login_attempts =0
    
    def decribe_user(self):
        user_summary={
            "firstName":self.first_name,
            "lastName": self.last_name,
            "gender":self.gender,
            "email":self.email, 
        }

        print(f"\n this is {self.first_name} {self.last_name} detials \n {user_summary}")
        
    def greet_user(self):
        print(f"\n\t Hello {self.first_name} {self.last_name}")
        
    def increament_login_attempts(self):
        self.login_attempts+=1
        print(f"\n {self.login_attempts} login attempt")
        
    def reset_login_attempts(self):
        self.login_attempts=0
        print(f" \n login attempt has been resetted to {self.login_attempts}")


class Privileges:
    """A simple attempt to model the Admin Privilages"""
    
    def __init__(self, privilages=["can add post", " can delete post", "can ban user" ]) -> None:
      """Initialize the Privileges attributes."""
      self.privileges =privilages
    
    def show_privileges (self):
        print(f" \nthe Admin has the following privileges: \n\n{self.privileges}")

class Admin(Users):
    """Represent aspects of User, specific to Admin User."""
    def __init__(self, first_name , last_name , gender , email, privileges)-> None:
        """initialing the parent class"""
        super().__init__(first_name , last_name , gender , email)
        # self.privileges=privileges  """ this line forms part of Question 9.7"""
        # the codes commented out is to allow smoot runing of 9.8
        self.privileges = Privileges()
    
    # def show_privileges (self):
    #     print(f" \nthe Admin has the following privileges: \n\n{self.privileges}")

# Question 9.7 
David= Admin("Daniel","Nwolu", "Male", "nwoludaniel.c@gmail.com",["can add post", " can delete post", "can ban user" ])
# David.show_privileges()
# and 9.8
David.privileges.show_privileges()




class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"\n\n{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self,battery_size = 75) -> None:
        self.battery_size =battery_size
 
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size=100
        print (self.battery_size)
                
    
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

# Question 9.9
my_tesla = ElectricCar('tesla', 'model S', 2019 )
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()