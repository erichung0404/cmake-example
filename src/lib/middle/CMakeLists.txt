add_library(Middle STATIC
    middle.cpp
)
target_link_libraries(Middle PRIVATE
    SeamIface
)
set_target_properties(Middle PROPERTIES
    INTERFACE_LINK_LIBRARIES_DIRECT SeamImpl
)