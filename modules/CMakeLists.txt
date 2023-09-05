cmake_minimum_required(VERSION 3.27)
project(VariableScope)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

include(Func)
func(
  KEYWORD_ONE_VALUE keyword_one_value
  KEYWORD_MULTI_VALUE keyword multi value
  OPTION2
  rest arg1 arg2
)