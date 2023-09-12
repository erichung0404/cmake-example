add_executable(TestExe1
    test_exe1.cpp
)
target_link_libraries(TestExe1 PRIVATE
    MiddleStub
    SeamStub
)