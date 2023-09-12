add_library(SeamImpl OBJECT
    seam_impl.cpp
)
add_library(SeamIface INTERFACE)

target_include_directories(SeamIface INTERFACE
    ${PROJECT_SOURCE_DIR}/include
)

target_link_libraries(SeamImpl PRIVATE
    SeamIface
)