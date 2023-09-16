add_library(Message SHARED
  message.cpp
)
set_target_properties(Message PROPERTIES
  VERSION 1.0.0
  SOVERSION 1
)
target_include_directories(Message PUBLIC
  ${PROJECT_SOURCE_DIR}/src/include
)
