cmake_minimum_required(VERSION 3.25)
project(ItHome2023)

function(checkSomething resultVar)
  set(${resultVar})
endfunction()

message(CHECK_START "Checking something")
list(APPEND CMAKE_MESSAGE_INDENT " ")

message(CHECK_START "Checking...")
checkSomething(success)
if(success)
  message(CHECK_PASS "supported")
else()
  message(CHECK_FAIL "not supported")
endif()

list(POP_BACK CMAKE_MESSAGE_INDENT)
if(success)
  message(CHECK_PASS "ok")
else()
  message(CHECK_FAIL "failed")
endif()
