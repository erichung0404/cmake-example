add_library(Middle STATIC
    middle.cpp
)
target_link_libraries(Middle PRIVATE
    SeamIface
)