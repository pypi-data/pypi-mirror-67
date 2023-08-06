#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SGEXT::SGCore" for configuration "Release"
set_property(TARGET SGEXT::SGCore APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SGEXT::SGCore PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libSGCore.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SGEXT::SGCore )
list(APPEND _IMPORT_CHECK_FILES_FOR_SGEXT::SGCore "${_IMPORT_PREFIX}/lib64/libSGCore.a" )

# Import target "SGEXT::SGExtract" for configuration "Release"
set_property(TARGET SGEXT::SGExtract APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SGEXT::SGExtract PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libSGExtract.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SGEXT::SGExtract )
list(APPEND _IMPORT_CHECK_FILES_FOR_SGEXT::SGExtract "${_IMPORT_PREFIX}/lib64/libSGExtract.a" )

# Import target "SGEXT::SGAnalyze" for configuration "Release"
set_property(TARGET SGEXT::SGAnalyze APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SGEXT::SGAnalyze PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libSGAnalyze.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SGEXT::SGAnalyze )
list(APPEND _IMPORT_CHECK_FILES_FOR_SGEXT::SGAnalyze "${_IMPORT_PREFIX}/lib64/libSGAnalyze.a" )

# Import target "SGEXT::SGLocate" for configuration "Release"
set_property(TARGET SGEXT::SGLocate APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SGEXT::SGLocate PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libSGLocate.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SGEXT::SGLocate )
list(APPEND _IMPORT_CHECK_FILES_FOR_SGEXT::SGLocate "${_IMPORT_PREFIX}/lib64/libSGLocate.a" )

# Import target "SGEXT::SGCompare" for configuration "Release"
set_property(TARGET SGEXT::SGCompare APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SGEXT::SGCompare PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libSGCompare.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SGEXT::SGCompare )
list(APPEND _IMPORT_CHECK_FILES_FOR_SGEXT::SGCompare "${_IMPORT_PREFIX}/lib64/libSGCompare.a" )

# Import target "SGEXT::SGGenerate" for configuration "Release"
set_property(TARGET SGEXT::SGGenerate APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SGEXT::SGGenerate PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libSGGenerate.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SGEXT::SGGenerate )
list(APPEND _IMPORT_CHECK_FILES_FOR_SGEXT::SGGenerate "${_IMPORT_PREFIX}/lib64/libSGGenerate.a" )

# Import target "SGEXT::SGDynamics" for configuration "Release"
set_property(TARGET SGEXT::SGDynamics APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SGEXT::SGDynamics PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libSGDynamics.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SGEXT::SGDynamics )
list(APPEND _IMPORT_CHECK_FILES_FOR_SGEXT::SGDynamics "${_IMPORT_PREFIX}/lib64/libSGDynamics.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
