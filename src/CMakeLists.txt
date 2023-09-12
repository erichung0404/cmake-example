cmake_minimum_required(VERSION 3.26)
project(ItHome2023
    LANGUAGES C CXX
    VERSION 0.1.0
)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_subdirectory(bin)
add_subdirectory(lib)
add_subdirectory(mock)
add_subdirectory(test)