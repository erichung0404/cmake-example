cmake_minimum_required(VERSION 3.27)
project(VariableScope)

function(func)
  set(prefix FOO)
  set(options OPTION1 OPTION2)
  set(keywordOneValue KEYWORD_ONE_VALUE)
  set(keywordMultiValue KEYWORD_MULTI_VALUE)
  include(CMakeParseArguments)
  cmake_parse_arguments(
    ${prefix}
    "${options}"
    "${keywordOneValue}"
    "${keywordMultiValue}"
    ${ARGN} # args...
  )
  message("prefix: ${prefix}")
  message("Options: ")
  foreach(arg IN LISTS options)
    if(${prefix}_${arg})
      message(" ${arg} enabled")
    else()
      message(" ${arg} disabled")
    endif()
  endforeach()

  message("Keywords: ")
  foreach(arg IN LISTS keywordOneValue keywordMultiValue)
    message(" ${arg} = ${prefix}_${arg} = ${${prefix}_${arg}}")
  endforeach()

  message("args: ${ARGN}")
endfunction()

func(
  KEYWORD_ONE_VALUE keyword_one_value
  KEYWORD_MULTI_VALUE keyword multi value
  OPTION2
  rest arg1 arg2
)