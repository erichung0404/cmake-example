add_library(MiddleStub STATIC
    middle_stub.cpp
)
target_link_libraries(MiddleStub PRIVATE
    SeamIface
)
set_target_properties(MiddleStub PROPERTIES
    INTERFACE_LINK_LIBRARIES_DIRECT SeamStub
)