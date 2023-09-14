#include <iostream>

#include <fmt/core.h>

int main()
{
    std::cout << fmt::format("Test fmt {}", "specifier") << std::endl;
    return 0;
}