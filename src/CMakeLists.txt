add_executable(Main
    main.cpp
)
add_library(Message STATIC
    message.cpp
)
target_link_libraries(Main PRIVATE
    Message
)