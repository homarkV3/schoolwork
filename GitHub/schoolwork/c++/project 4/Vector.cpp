#include "Vector.h"
#include <stdexcept>
#include <string>
using namespace std;

Vector::Vector()
{
    capacity = CHUNK;
    n_elems = 0;
    data_ptr = new int[capacity];
}

Vector::Vector(const Vector &v)
{
    capacity = v.size();
    n_elems = v.size();
    data_ptr = new int[capacity];
    for (int i = 0; i < v.size(); i++){
       data_ptr[i]= v.at(i);
    }
}

Vector& Vector::operator=(const Vector& v)
{
    if (this != &v) {                // Avoid self-assignment
        capacity = v.size();
        n_elems = v.size();
        data_ptr = new int[capacity];
        for (int i = 0; i < this->size(); i++){
            data_ptr[i]= v.at(i);
        }
    }
    return *this; 
}

Vector::~Vector()
{ 
    delete [] data_ptr;
}

void Vector::grow()
{   
    if (capacity <= n_elems) {
        int *temp = new int[int(capacity*1.6)];
        for (int i = 0; i < n_elems; i++){
            temp[i] = data_ptr[i];
        }
        delete [] data_ptr;
        data_ptr = temp;
    }
}

int Vector::front() const
{
    return at(0);
} // Return the int in position 0, if any

int Vector::back() const
{
    return at(n_elems-1);
} // Return last element (position n_elems-1)

int Vector::at(size_t pos) const
{   
    if (pos <= n_elems && n_elems != 0){
        return data_ptr[pos];
    }
    throw range_error("OUT OF RANGE");
} // Return element in position "pos" (0-based)

size_t Vector::size() const
{
    return n_elems;
} // Return n_elems

bool Vector::empty() const
{
    return n_elems == 0;
} // Return n_elems == 0

// Mutators
int &Vector::operator[](size_t pos)
{    
    return data_ptr[pos];
} // Same as at but no bounds checking
void Vector::push_back(int item)
{
    n_elems++;
    grow();
    data_ptr[n_elems-1] = item;
} // Append a new element at the end of the array
void Vector::pop_back()
{
    at(n_elems);
    --n_elems;
} // --n_elems (nothing else to do; returns nothing)
void Vector::erase(size_t pos)
{
    at(pos);
    --n_elems;
    for (int i = pos;n_elems > i; i++){
        data_ptr[i] = data_ptr[i+1];
    }
} // Remove item in position pos and shuffles following items left
void Vector::insert(size_t pos, int item)
{
    ++n_elems;
    grow();
    for (int i = pos;n_elems > i; i++){
        data_ptr[i+1] = data_ptr[i];
    }
    data_ptr[pos] = item;
} // Shuffle items right to make room for a new element
void Vector::clear()
{
    n_elems = 0;
} // n_elems = 0 (nothing else to do; keep the current capacity)

// Iterators
int *Vector::begin()
{
    if (n_elems == 0){
        return nullptr;
    }
    return &data_ptr[0];
} // Return a pointer to 1st element, or nullptr if n_elems == 0
int *Vector::end()
{
    if (n_elems == 0){
        return nullptr;
    }
    return &data_ptr[n_elems];
} // Return a pointer to 1 past last element, or nullptr if n_elems == 0

// Comparators
bool Vector::operator==(const Vector &v) const
{
    for (int i = 0; v.n_elems <= i; i++){
        if (at(i) != v.at(i) || n_elems != v.n_elems){
            return false;
        } 
    }
    return true;
}
bool Vector::operator!=(const Vector &v) const
{
    return (*this == v);
}