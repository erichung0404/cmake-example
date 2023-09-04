list(APPEND CMAKE_MESSAGE_CONTEXT "Cache Variables")

set(varName "first init" CACHE STRING "")
message("cache variable: $CACHE{varName}") # first init
set(varName "update without FORCE" CACHE STRING "")
message("cache variable: $CACHE{varName}") # first init
set(varName "update with FORCE" CACHE STRING "" FORCE)
message("cache variable: $CACHE{varName}") # update with FORCE
set(varName "override with normal variable")
message("cache variable: ${varName}") # update with FORCE
set(varName "override with normal variable")
message("cache variable: ${varName}") # override with normal variable
