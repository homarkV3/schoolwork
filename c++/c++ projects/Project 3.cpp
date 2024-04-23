#include <bitset>
#include <cassert>
#include <iostream>

using namespace std;

class Bits {
    using IType = unsigned long long;
    enum { NBITS = sizeof(IType) * 8 };
    IType bits = 0;

public:
    Bits() = default;
    Bits(IType n) {
        bits = n;
    }
    static int size() {
        return NBITS;
    }

    bool at(int pos) const {
        assert(0 <= pos && pos < NBITS);
        return bits & (IType(1) << pos);
    }

    void reset() {
        bits = 0;
    }

    void assign(int pos, bool val) {
        if (at(pos)) {
            toggle(pos);
        }
        if (val) {
            bits |= (IType(1) << pos);
        }
    }

    void assign(IType n) {
        bits = n;
    }

    void toggle(int pos) {
        (bits ^= 1ULL << pos);
    }

    void toggle() {
        bits = ~bits;
    }

    void shift(int n) {
        if (n > 0) {
            bits = bits >> n;
        }
        else if (n < 0) {
            bits = bits << -n;
        }
    }

    void rotate(int n) {

        // save sign
        int sign = 1;

        if (n < 0) {
            sign = -1;
            n = -n;
        }

        // remove complete rotates
        n %= NBITS;

        // rotate rigth
        if (sign == 1) {
            bits = (bits >> n) | (bits << (NBITS - n));
        }

        // rotate left
        else {
            bits = (bits << n) | (bits >> (NBITS - n));
        }
    }

    int ones(unsigned int ones) const {
        int count = 0;
        while (ones) {
            count += ones & bits;
            ones >>= 1;
        }

        return count;
    }
};