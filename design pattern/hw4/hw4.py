class DisplayDriver:
    def draw(self):
        raise NotImplementedError("Draw method not implemented.")

class HighResDisplay(DisplayDriver):
    def draw(self):
        print("Drawing a Widget using a HighResDisplayDriver")

class LowResDisplay(DisplayDriver):
    def draw(self):
        print("Drawing a Widget using a LowResDisplayDriver")

class PrintDriver:
    def print(self):
        raise NotImplementedError("Print method not implemented.")

class HighResPrint(PrintDriver):
    def print(self):
        print("Printing a Document using a HighResPrintDriver")

class LowResPrint(PrintDriver):
    def print(self):
        print("Printing a Document using a LowResPrintDriver")

class DriverFactory:
    def get_display_driver(self):
        raise NotImplementedError

    def get_print_driver(self):
        raise NotImplementedError

class HighResDriverFactory(DriverFactory):
    def get_display_driver(self):
        return HighResDisplay()

    def get_print_driver(self):
        return HighResPrint()

class LowResDriverFactory(DriverFactory):
    def get_display_driver(self):
        return LowResDisplay()

    def get_print_driver(self):
        return LowResPrint()

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

def main():
    resolution_setting = "high"  
    if resolution_setting == "high":
        factory = HighResDriverFactory()
    else:
        factory = LowResDriverFactory()

    widget = Widget(factory.get_display_driver())
    document = Document(factory.get_print_driver())

    widget.draw()
    document.print()

if __name__ == "__main__":
    main()