cmake_minimum_required(VERSION 3.27)
project(VariableScope)

set(x 1)
block()
  set(x 2)
  set(y 3)
  message("inner x: ${x}")
  message("inner y: ${y}")
endblock()

message("outer x: ${x}")
message("outer y: ${y}")