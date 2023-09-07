cmake_minimum_required(VERSION 3.25)
project(ItHome2023)

function(foo1)
  list(APPEND CMAKE_MESSAGE_INDENT " ")
  message("${CMAKE_CURRENT_FUNCTION}")
endfunction()

function(foo2)
  list(APPEND CMAKE_MESSAGE_INDENT " ")
  message("${CMAKE_CURRENT_FUNCTION}")
  foo1()
endfunction()

function(foo3)
  list(APPEND CMAKE_MESSAGE_INDENT " ")
  message("${CMAKE_CURRENT_FUNCTION}")
  foo2()
endfunction()

message("Top")
foo1()
foo2()
foo3()
