list(APPEND CMAKE_MESSAGE_CONTEXT "Predefeind Varaibles")

message("top: CMAKE_SOURCE_DIR = ${CMAKE_SOURCE_DIR}")
message("top: CMAKE_BINARY_DIR = ${CMAKE_BINARY_DIR}")
message("top: CMAKE_CURRENT_SOURCE_DIR = ${CMAKE_CURRENT_SOURCE_DIR}")
message("top: CMAKE_CURRENT_BINARY_DIR = ${CMAKE_CURRENT_BINARY_DIR}")

add_subdirectory(subdir)
