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

add_library(${PROJECT_NAME}::StaticLib ALIAS StaticLib)
add_library(${PROJECT_NAME}::SharedLib ALIAS SharedLib)

include(GenerateExportHeader)
generate_export_header(SharedLib)
generate_export_header(StaticLib)

target_include_directories(StaticLib PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
)
target_include_directories(SharedLib PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
)

target_sources(StaticLib PUBLIC
  FILE_SET HEADERS
  FILES
    ${PROJECT_SOURCE_DIR}/src/include/static_lib.h
  BASE_DIRS ${PROJECT_SOURCE_DIR}/src/include
)
target_sources(SharedLib PUBLIC
  FILE_SET HEADERS
  FILES
    ${PROJECT_SOURCE_DIR}/src/include/shared_lib.h
  BASE_DIRS ${PROJECT_SOURCE_DIR}/src/include
)

install(
  FILES
    ${CMAKE_CURRENT_BINARY_DIR}/sharedlib_export.h
    ${CMAKE_CURRENT_BINARY_DIR}/staticlib_export.h
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(TARGETS StaticLib SharedLib
  EXPORT MyLibs
  FILE_SET HEADERS
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
install(EXPORT MyLibs
  FILE ${PROJECT_NAME}Targets.cmake
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
  NAMESPACE ${PROJECT_NAME}::
)
export(EXPORT MyLibs
  NAMESPACE ${PROJECT_NAME}::
  FILE ${PROJECT_NAME}Targets.cmake
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
    ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}
)
install(DIRECTORY ${PROJECT_SOURCE_DIR}/src/include/
  DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)