include(FetchContent)
set(FETCHCONTENT_QUIET OFF)
FetchContent_Declare(fmt
  GIT_REPOSITORY  https://github.com/fmtlib/fmt.git
  GIT_REMOTE_NAME origin
  GIT_TAG         10.1.1
  GIT_SHALLOW     TRUE
)
FetchContent_Declare(googletest
  GIT_REPOSITORY  https://github.com/google/googletest.git
  GIT_REMOTE_NAME origin
  GIT_TAG         v1.14.0
  GIT_SHALLOW     TRUE
)
FetchContent_MakeAvailable(fmt googletest)
