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

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(stock-dashboard main.cpp
    src/app.cpp
    include/app.hpp)
target_link_libraries(stock-dashboard PRIVATE wx::core wx::base)

target_include_directories(stock-dashboard PRIVATE include)