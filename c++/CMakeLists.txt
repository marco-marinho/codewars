cmake_minimum_required(VERSION 3.28)
project(code_wars)

set(CMAKE_CXX_STANDARD 17)

add_library(codewars
        moving_zeroes_to_the_end.cpp
        human_readable_time.cpp
        rgb_to_hex_conversion.cpp
        direction_reduction.cpp)
