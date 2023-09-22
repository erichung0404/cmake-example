cmake_minimum_required(VERSION 3.25)
project(Day21Sample CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(GNUInstallDirs)

add_subdirectory(src)

if(PROJECT_IS_TOP_LEVEL)
    add_subdirectory(packaging)
endif()