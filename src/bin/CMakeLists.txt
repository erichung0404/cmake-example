add_executable(Exe1
    exe1.cpp
)
target_link_libraries(Exe1 PRIVATE
    Middle
    SeamImpl
)