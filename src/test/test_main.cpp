#include <gtest/gtest.h>

namespace {
TEST(UsageTest, CanUseGoogleTest) {
  SUCCEED();
}
}  // anonymous namespace

int main(int argc, char** argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
