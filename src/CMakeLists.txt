add_executable(Day23Sample_Main main.cpp)
target_link_libraries(Day23Sample_Main PRIVATE
    Day21Sample::SharedLib
    Day21Sample::StaticLib
)