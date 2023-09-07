cmake_minimum_required(VERSION 3.25)
project(ItHome2023)

variable_watch(name)

function(Foo name)
  message(STATUS "Hello, ${name}!")
endfunction()

set(name "Eric")

Foo(${name})


