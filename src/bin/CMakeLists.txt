find_program(CCACHE_EXECUTABLE ccache)
if(CCACHE_EXECUTABLE)
  set(CMAKE_CXX_COMPILER_LAUNCHER ${CCACHE_EXECUTABLE})
endif()

file(
  GLOB _sources ${CMAKE_SOURCE_DIR}/src/lib/*.cpp
)
file(
  GLOB _headers ${CMAKE_SOURCE_DIR}/src/include/*.h
)
file(
  GLOB _executables ${CMAKE_SOURCE_DIR}/src/bin/main_*.cpp
)
add_executable(Main main.cpp ${_sources})
target_include_directories(Main PRIVATE ${CMAKE_SOURCE_DIR}/src/include)
target_precompile_headers(Main PRIVATE ${_headers})
foreach(_executable ${_executables})
  get_filename_component(_target ${_executable} NAME_WE)
  add_executable(${_target} ${_executable} ${_sources})
  target_include_directories(${_target} PRIVATE ${CMAKE_SOURCE_DIR}/src/include)
  target_precompile_headers(${_target} REUSE_FROM Main)
endforeach()

