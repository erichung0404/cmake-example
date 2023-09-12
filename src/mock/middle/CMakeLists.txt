add_library(MiddleStub STATIC
    middle_stub.cpp
)
target_link_libraries(MiddleStub PRIVATE
    SeamIface
)