#include <iostream>

extern int x;
void Foo();
int main() {
    Foo();
    std::cout << x << std::endl;
    return 0;
}