#include <iostream>

#include <message.h>

int main() {
#ifndef IS_TEST_MAIN
    std::cout << "Is Test" << std::endl;
#else
    std::cout << GetMessage() << std::endl;
#endif
return 0;
}