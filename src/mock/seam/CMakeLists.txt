add_library(SeamStub OBJECT
    seam_stub.cpp
)
target_link_libraries(SeamStub PRIVATE
    SeamIface
)