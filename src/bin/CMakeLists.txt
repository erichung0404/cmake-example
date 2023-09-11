add_executable(MyApp
    intro_libs.cpp
)

target_link_libraries(MyApp PRIVATE
    MyApp_Static
    MyApp_Shared
)