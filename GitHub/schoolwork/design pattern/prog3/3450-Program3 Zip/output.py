from abc import ABC, abstractmethod

class Output(ABC):
    @abstractmethod
    def write(self, o):
        pass

class StreamOutput(Output):
    @classmethod
    def create(cls, stream):
        return cls(stream)

    def __init__(self, stream):
        self.sink = stream

    def write(self, o):
        self.sink.write(str(o))

class BracketOutput(Output):
    @classmethod
    def create(cls, output):
        return cls(output)

    def __init__(self, output):
        self.decorated_output = output

    def write(self, o):
        self.decorated_output.write(f'[{o}]\n')

class NumberedOutput(Output):
    @classmethod
    def create(cls, output):
        return cls(output)

    def __init__(self, output):
        self.decorated_output = output
        self.line_number = 0

    def write(self, o):
        self.line_number += 1
        self.decorated_output.write(f'{self.line_number:5}: {o}')

class TeeOutput(Output):
    @classmethod
    def create(cls, output, second_stream):
        return cls(output, second_stream)

    def __init__(self, output, second_stream):
        self.decorated_output = output
        self.second_sink = second_stream

    def write(self, o):
        self.decorated_output.write(o)
        self.second_sink.write(str(o))

class Predicate(ABC):
    @abstractmethod
    def execute(self, o):
        pass

class FilterOutput(Output):
    @classmethod
    def create(cls, output, predicate):
        return cls(output, predicate)

    def __init__(self, output, predicate):
        self.decorated_output = output
        self.predicate = predicate

    def write(self, o):
        if self.predicate.execute(o):
            self.decorated_output.write(o)

class ContainsDigit(Predicate):
    @classmethod
    def create(cls):
        return cls()

    def execute(self, o):
        return any(char.isdigit() for char in str(o))

class ContainsLetter(Predicate):
    @classmethod
    def create(cls):
        return cls()

    def execute(self, o):
        return any(char.isalpha() for char in str(o))

def main():
    file_to_read = input('Enter the name of the file to read: ')
    with open(file_to_read, 'r') as f:
        lines = f.readlines()

    output = StreamOutput.create(open('out.txt', 'w'))

    while True:
        print('Select a decorator:')
        print('1. BracketOutput')
        print('2. NumberedOutput')
        print('3. TeeOutput')
        print('4. FilterOutput')
        print('5. Done')

        selection = int(input())

        if selection == 1:
            output = BracketOutput.create(output)
        elif selection == 2:
            output = NumberedOutput.create(output)
        elif selection == 3:
            tee_file = input('Enter the name of the file for the TeeOutput: ')
            output = TeeOutput.create(output, open(tee_file, 'w'))
        elif selection == 4:
            print('Select a predicate:')
            print('1. ContainsDigit')
            print('2. ContainsLetter')

            predicate_selection = int(input())
            predicate = ContainsDigit.create() if predicate_selection == 1 else ContainsLetter.create()

            output = FilterOutput.create(output, predicate)
        elif selection == 5:
            break

    for line in lines:
        output.write(line)

if __name__ == '__main__':
    main()
