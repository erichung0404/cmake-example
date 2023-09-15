list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR}/cmake)

include(dependencies)

include_directories(${CMAKE_CURRENT_LIST_DIR}/include)

add_subdirectory(bin)
add_subdirectory(lib)
add_subdirectory(test)
