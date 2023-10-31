# [ ... previous code ... ]
# Abstract Factory
class AbstractDriverFactory:
    def create_display_driver(self):
        pass

    def create_print_driver(self):
        pass

# Concrete Factories
class LowResDriverFactory(AbstractDriverFactory):
    def create_display_driver(self):
        return LowResDisplayDriver()

    def create_print_driver(self):
        return LowResPrintDriver()

class HighResDriverFactory(AbstractDriverFactory):
    def create_display_driver(self):
        return HighResDisplayDriver()

    def create_print_driver(self):
        return HighResPrintDriver()

# Abstract Product classes
class DisplayDriver:
    def draw(self):
        pass

class PrintDriver:
    def print(self):
        pass

# Concrete Product classes
class LowResDisplayDriver(DisplayDriver):
    def draw(self):
        print("Drawing a Widget using a LowResDisplayDriver")

class HighResDisplayDriver(DisplayDriver):
    def draw(self):
        print("Drawing a Widget using a HighResDisplayDriver")

class LowResPrintDriver(PrintDriver):
    def print(self):
        print("Printing a Document using a LowResPrintDriver")

class HighResPrintDriver(PrintDriver):
    def print(self):
        print("Printing a Document using a HighResPrintDriver")

class Widget:
    def __init__(self, display_driver):
        self.display_driver = display_driver

    def draw(self):
        self.display_driver.draw()

class Document:
    def __init__(self, print_driver):
        self.print_driver = print_driver

    def print(self):
        self.print_driver.print()

def get_factory_from_user_input():
    print("Choose resolution (1. Low, 2. High): ")
    choice = int(input())
    
    if choice == 1:
        return LowResDriverFactory()
    elif choice == 2:
        return HighResDriverFactory()
    else:
        print("Invalid choice. Defaulting to Low Resolution.")
        return LowResDriverFactory()

# Main driver
def main():
    factory = get_factory_from_user_input()

    widget = Widget(factory.create_display_driver())
    widget.draw()

    document = Document(factory.create_print_driver())
    document.print()

main()
