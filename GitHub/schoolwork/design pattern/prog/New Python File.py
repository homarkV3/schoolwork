from typing import TypeVar, Generic, List, Callable

T = TypeVar('T')

class Iterator(Generic[T]):
    def first(self) -> None:
        raise NotImplementedError

    def next(self) -> None:
        raise NotImplementedError

    def isDone(self) -> bool:
        raise NotImplementedError

    def current(self) -> T:
        raise NotImplementedError

class Iterable(Generic[T]):
    def getIterator(self) -> Iterator[T]:
        raise NotImplementedError

class Sequence(Generic[T]):
    def add(self, value: T) -> None:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError

    def capacity(self) -> int:
        raise NotImplementedError

    def get(self, index: int) -> T:
        raise NotImplementedError

class IterableSequence(Sequence[T], Iterable[T]):
    pass

class MyArray(IterableSequence[T]):
    def __init__(self, size: int):
        self.array = [None] * size
        self.length = 0

    def add(self, value: T) -> None:
        if self.length < len(self.array):
            self.array[self.length] = value
            self.length += 1
        else:
            raise IndexError("Array is full")

    def size(self) -> int:
        return self.length

    def capacity(self) -> int:
        return len(self.array)

    def get(self, index: int) -> T:
        if 0 <= index < self.length:
            return self.array[index]
        else:
            raise IndexError("Index out of range")

class MyIterator(Iterator[T]):
    def __init__(self, sequence: IterableSequence[T]):
        self.sequence = sequence
        self.current_index = 0

    def first(self) -> None:
        self.current_index = 0

    def next(self) -> None:
        self.current_index += 1

    def isDone(self) -> bool:
        return self.current_index >= self.sequence.size()

    def current(self) -> T:
        return self.sequence.get(self.current_index)

class MyFilterIterator(Iterator[T]):
    def __init__(self, iterator: Iterator[T], predicate: Callable[[T], bool]):
        self.iterator = iterator
        self.predicate = predicate

    def first(self) -> None:
        self.iterator.first()
        self.advance()

    def next(self) -> None:
        self.iterator.next()
        self.advance()

    def isDone(self) -> bool:
        return self.iterator.isDone()

    def current(self) -> T:
        return self.iterator.current()

    def advance(self) -> None:
        while not self.iterator.isDone() and not self.predicate(self.iterator.current()):
            self.iterator.next()

# Example usage
def is_even(n: int) -> bool:
    return n % 2 == 0

array = MyArray(5)
array.add(1)
array.add(2)
array.add(3)
array.add(4)
array.add(5)

iterator = MyIterator(array)
filter_iterator = MyFilterIterator(iterator, is_even)

print("Original sequence:")
iterator.first()
while not iterator.isDone():
    print(iterator.current())
    iterator.next()

print("Filtered sequence (even numbers):")
filter_iterator.first()
while not filter_iterator.isDone():
    print(filter_iterator.current())
    filter_iterator.next()