cmake_minimum_required(VERSION 3.24)
project(stock-dashboard VERSION 0.1.0 LANGUAGES C CXX)

include(FetchContent)

FetchContent_Declare(
    wxwidgets
    URL https://github.com/wxWidgets/wxWidgets/releases/download/v3.2.11/wxWidgets-3.2.11.tar.bz2
    URL_HASH SHA1=760d57d2eb6591869dd096222f7b9e5c77736f9f
    SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/external/wxwidgets"
    DOWNLOAD_EXTRACT_TIMESTAMP FALSE
)
FetchContent_MakeAvailable(wxwidgets)

FetchContent_Declare(
    wxmathplot
    URL https://github.com/GitHubLionel/wxMathPlot/archive/2a392efbe9c77ef7d8e387dc406c262b15df4ff9.tar.gz
    DOWNLOAD_EXTRACT_TIMESTAMP FALSE
    # Fetch the sources without running wxMathPlot's standalone build.
    SOURCE_SUBDIR unused-cmake-directory
)
FetchContent_MakeAvailable(wxmathplot)

find_package(Python 3.8 REQUIRED COMPONENTS Interpreter Development.Embed)
FetchContent_Declare(
    pybind11
    URL https://github.com/pybind/pybind11/archive/refs/tags/v3.0.2.tar.gz
    URL_HASH SHA256=2f20a0af0b921815e0e169ea7fec63909869323581b89d7de1553468553f6a2d
    DOWNLOAD_EXTRACT_TIMESTAMP FALSE
)
FetchContent_MakeAvailable(pybind11)

add_library(wxmathplot STATIC
    "${wxmathplot_SOURCE_DIR}/mathplot/mathplot.cpp"
    "${wxmathplot_SOURCE_DIR}/MathPlotConfig/MathPlotConfig.cpp"
)
target_compile_features(wxmathplot PUBLIC cxx_std_17)
target_include_directories(wxmathplot
    PUBLIC "${wxmathplot_SOURCE_DIR}/mathplot"
    PRIVATE "${wxmathplot_SOURCE_DIR}/MathPlotConfig"
)
target_link_libraries(wxmathplot
    PUBLIC wx::core wx::base
    PRIVATE wx::adv wx::aui
)
if(APPLE)
    # wxMathPlot assumes GNU-compatible compilers provide sincos.
    target_compile_definitions(wxmathplot PRIVATE sincos=__sincos)
endif()

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(stock-dashboard
    main.cpp
    src/app.cpp
    include/app.hpp
    src/interface.cpp
    include/interface.hpp
)
target_link_libraries(stock-dashboard PRIVATE wxmathplot pybind11::embed)
target_include_directories(stock-dashboard PRIVATE include)