#include <message.h>

std::string GetMessage() {
#ifdef IS_TEST
    return "Test Hello World";
#else
    return "Hello World";
#endif
}