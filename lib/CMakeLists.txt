add_library(TestLib_Greeting
  greeting.cpp
)

set_property(TARGET TestLib_Greeting PROPERTY 
  STATIC_LIBRARY_OPTIONS "--thin"
)