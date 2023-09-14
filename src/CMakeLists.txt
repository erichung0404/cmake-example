list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR}/cmake)

include(dependencies)

add_executable(MyApp
  main.cpp
)
target_link_libraries(MyApp PRIVATE
  fmt::fmt-header-only
)