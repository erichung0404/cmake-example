cmake_minimum_required(VERSION 3.25)

list(APPEND CMAKE_MESSAGE_CONTEXT ItHome2023)
project(ItHome2023)

message("Start")

add_subdirectory(foo)
add_subdirectory(bar)

message("End")
