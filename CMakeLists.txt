cmake_minimum_required(VERSION 3.27)
project(TestLib)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(Main
  main.cpp
)

include_directories(${PROJECT_SOURCE_DIR}/include)
add_subdirectory(lib)

target_link_libraries(Main PRIVATE
  TestLib_Greeting
)

target_compile_options(Main PRIVATE
  "SHELL:-Xassembler --keep-locals"
  "SHELL:-Xassembler --warn"
)

target_link_options(Main PRIVATE
  "LINKER:SHELL:-stats"
  "LINKER:SHELL:-z,defs"
)