// mylib.cpp

#include <iostream>

int myadd(int a, int b) {
    return a + b;
}

class Point {
public:
    Point(int x, int y) : x_(x), y_(y) {}
    void print() const {
        std::cout << "(" << x_ << ", " << y_ << ")" << std::endl;
    }
private:
    int x_, y_;
};
