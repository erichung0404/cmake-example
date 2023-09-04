list(APPEND CMAKE_MESSAGE_CONTEXT "Normal Variables")

set(varName a b c) # "a;b;c"
message("a b c: ${varName}")
set(varName "a b c") # "a b c"
message("\"a b c\": ${varName}")
set(varName a b;c) # "a;b;c"
message("a b;c: ${varName}")
set(varName a "b c") # "a;b c"
message("a \"b c\": ${varName}")