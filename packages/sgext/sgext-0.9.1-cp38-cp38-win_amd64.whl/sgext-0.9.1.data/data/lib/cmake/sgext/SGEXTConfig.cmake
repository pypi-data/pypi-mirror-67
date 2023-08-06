
####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was SGEXTConfig.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

####################################################################################

include(CMakeFindDependencyMacro)

#### Required dependencies  ####
find_dependency(Boost REQUIRED COMPONENTS program_options filesystem graph)
find_dependency(DGtal REQUIRED 1.0)

#### Optional dependencies based on SGEXT options ####
if(TRUE) #if(${SG_REQUIRES_ITK})
  find_dependency(ITK REQUIRED COMPONENTS
    ITKCommon;ITKIOImageBase;ITKImageGrid;ITKImageIntensity;ITKImageStatistics;ITKVtkGlue;ITKImageIO
    CONFIG)
endif()
if(OFF) #if (${SG_MODULE_VISUALIZE_WITH_QT})
  find_dependency(Qt5 REQUIRED
    Widgets
    Xml
    OpenGL)
endif()
if(TRUE) # if(${SG_REQUIRES_VTK})
  find_dependency(VTK COMPONENTS
    vtkChartsCore;vtkCommonCore;vtkCommonDataModel;vtkViewsInfovis;vtkRenderingCore;vtkRenderingOpenGL2
    CONFIG
    REQUIRED
    )
endif()

get_filename_component(SGEXT_CMAKE_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)
if(NOT TARGET SGCore)
  include ("${SGEXT_CMAKE_DIR}/SGEXTTargets.cmake")
endif()
