set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN TRUE)

add_library(StaticLib STATIC
    static_lib.cpp
)
add_library(SharedLib SHARED
    shared_lib.cpp
)
set_target_properties(SharedLib PROPERTIES
  VERSION 1.0.0
  SOVERSION 1
)
target_sources(StaticLib PRIVATE
  FILE_SET HEADERS
  FILES ${PROJECT_SOURCE_DIR}/src/include/static_lib.h
  BASE_DIRS ${PROJECT_SOURCE_DIR}/src/include
)
target_sources(SharedLib PRIVATE
  FILE_SET HEADERS
  FILES ${PROJECT_SOURCE_DIR}/src/include/shared_lib.h
  BASE_DIRS ${PROJECT_SOURCE_DIR}/src/include
)

include(GNUInstallDirs)
install(TARGETS StaticLib SharedLib
  EXPORT MyLibs
  FILE_SET HEADERS
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
install(EXPORT MyLibs
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
  NAMESPACE Day21Sample::
)

include(CMakePackageConfigHelpers)
write_basic_package_version_file(${PROJECT_NAME}ConfigVersion.cmake
  VERSION 1.0.0
  COMPATIBILITY AnyNewerVersion
)
configure_package_config_file(
  ${PROJECT_NAME}Config.cmake.in
  ${PROJECT_NAME}Config.cmake
  INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
)
install(
  FILES
    ${PROJECT_BINARY_DIR}/src/lib/${PROJECT_NAME}ConfigVersion.cmake
    ${PROJECT_BINARY_DIR}/src/lib/${PROJECT_NAME}Config.cmake
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
)