add_executable(TestMain
  test_main.cpp
)
target_link_libraries(TestMain PRIVATE
  GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(TestMain)
