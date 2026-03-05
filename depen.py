class V8Engine:
    def start(self):
        return "VROOM VROOM!"


class ElectricEngine:
    def start(self):
        return "whirrrrrr..."


class Car:
    # GOOD: The car asks for an engine to be injected!
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        print(self.engine.start())


# --- THE INJECTION ---
# We (the outside boss) build the engine first...
my_electric_motor = V8Engine()

# ...and we INJECT it into the car!
my_new_car = Car(engine=my_electric_motor)

my_new_car.drive()  # Output: whirrrrrr...
