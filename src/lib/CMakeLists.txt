set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN TRUE)

add_library(StaticLib STATIC
    static_lib.cpp
)
add_library(SharedLib SHARED
    shared_lib.cpp
)

target_include_directories(SharedLib PUBLIC
  ${CMAKE_CURRENT_BINARY_DIR}
)
target_include_directories(StaticLib PUBLIC
  ${CMAKE_CURRENT_BINARY_DIR}
)
target_link_libraries(SharedLib PRIVATE
    $<LINK_LIBRARY:WHOLE_ARCHIVE,StaticLib>
)

include(GenerateExportHeader)
generate_export_header(SharedLib)