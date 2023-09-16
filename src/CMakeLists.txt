add_subdirectory(lib)

add_executable(Main
    main.cpp
)
target_link_libraries(Main PRIVATE
    Message
    Util
)
target_compile_definitions(Main PRIVATE
  $<$<BOOL:$<TARGET_PROPERTY:IS_TEST>>:IS_TEST_MAIN>
)