add_executable(Main
    main.cpp
)

add_subdirectory(lib)

target_link_libraries(Main PRIVATE
    SharedLib
)