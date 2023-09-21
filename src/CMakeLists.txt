include_directories(include)

add_subdirectory(lib)

add_executable(Main
    main.cpp
)
target_link_libraries(Main PRIVATE
    SharedLib
    StaticLib
)