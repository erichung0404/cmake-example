include(FetchContent)
set(FETCHCONTENT_QUIET OFF)
FetchContent_Declare(Day21Sample
    GIT_REPOSITORY https://github.com/erichung0404/cmake-example.git
    GIT_TAG day22-packaging
    GIT_SHALLOW TRUE
)
FetchContent_MakeAvailable(Day21Sample)
