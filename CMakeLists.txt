cmake_minimum_required(VERSION 3.16)
#setup configuration variables for stm32-cmake
#set(STM32_CHIP STM32F401RE)
#set(STM32_CUBE_F4_PATH "/usr/lib/STM32CUBEF4")
# set(STM32_TOOLCHAIN_PATH "/home/dev/gcc-arm-none-eabi")
#set(CMAKE_MODULE_PATH "/usr/lib/stm32-cmake/cmake")

#set(CMAKE_TOOLCHAIN_FILE "/usr/lib/stm32-cmake/cmake/stm32_gcc.cmake")
set(UNITY_DIR "/usr/lib/unity/src")

project(lolkillme LANGUAGES C ASM)

set(TARGET_GROUP production CACHE STRING "What Should I Build?")


if(TARGET_GROUP STREQUAL Test)
else()
    set(CMAKE_BUILD_TYPE TARGET_GROUP)
endif()

set(CMAKE_INCLUDE_CURRENT_DIR TRUE)

if(TARGET_GROUP STREQUAL Test)
        include(CTest)
        add_library(unity STATIC ${UNITY_DIR}/unity.c)
        target_include_directories(unity PUBLIC ${UNITY_DIR})

        add_subdirectory(Core/TestSrc)


else()
    FIND_PACKAGE(CMSIS COMPONENTS STM32F4 REQUIRED)
    FIND_PACKAGE(HAL COMPONENTS STM32F4 REQUIRED)

    add_subdirectory(Core)

    ADD_EXECUTABLE( ${CMAKE_PROJECT_NAME}                
                    "startup_stm32f401xe.s"    
                    "Core/Src/main.c"                  
                    )
    target_link_libraries( ${CMAKE_PROJECT_NAME}
                           project_sources
                           )

    stm32_add_linker_script(${CMAKE_PROJECT_NAME} PRIVATE STM32F401RETx_FLASH.ld)
endif()


#STM32_SET_TARGET_PROPERTIES(${CMAKE_PROJECT_NAME})
#STM32_ADD_HEX_BIN_TARGETS(${CMAKE_PROJECT_NAME})

#cmake -DCMAKE_BUILD_TYPE=<DEBUG or RELEASE> .. && make
