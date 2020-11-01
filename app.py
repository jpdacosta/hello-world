class App:
    default_colour = "red"
    #Constructor---------
    def __init__(self,x,y):
        #these are instance variables. Class variables apply changes to all instances of that class
        self.x = x
        self.y = y

    def show_results(self):
        print(f"X Value: {self.x} YValue {self.y}")

    @classmethod
    def zero(cls):
        return cls(0,0)
        

    def fizz_buzz(self,number):
        if (number % 3) == 0 and (number % 5)==0:
            return "Fizz Buzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        return number
#-----Class ends here------------------------------------

#-----test code fore the class-----------------------------
app = App(1,2)
app.show_results()
app.fizz_buzz(5)
app.default_colour = "yellow"
print(app.default_colour)
# calling a class variable like this defaults all the instances to reflect this - this is a class variable
App.default_colour = "yellow"

app2 = App(3,4)
app2.show_results()
app2.fizz_buzz(5)
print(app2.default_colour)

# calling a class method is the same as calling a static method in java
app3 = App.zero()
app3.show_results()
app2.show_results()
app.show_results()