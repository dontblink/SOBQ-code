#setup configuration variables for stm32-cmake
set(STM32_CHIP STM32F401RE)
set(STM32Cube_DIR "/usr/lib/STM32CUBEF4")
set(TOOLCHAIN_PREFIX "/home/dev/gcc-arm-none-eabi-9-2020-q2-update")
set(CMAKE_MODULE_PATH "/usr/lib/stm32-cmake/cmake")
set(CMAKE_TOOLCHAIN_FILE "/usr/lib/stm32-cmake/cmake/gcc_stm32.cmake")

cmake_minimum_required(VERSION 3.13.0)
project(lolkillme LANGUAGES C )

#set(CMAKE_CXX_COMPILER $(TOOLCHAIN_PREFIX))
#set(STM32_LINKER_SCRIPT ${CMSIS_LINKER_SCRIPT})
#set(PROJECT_SOURCE_DIR "./Core")

FIND_PACKAGE(CMSIS REQUIRED)
FIND_PACKAGE(STM32HAL COMPONENTS gpio tim usart dma rcc REQUIRED)
FIND_PACKAGE(STM32LL COMPONENTS utils exti usb REQUIRED)
INCLUDE_DIRECTORIES (
                    ${CMAKE_CURRENT_SOURCE_DIR}
                    "${PROJECT_SOURCE_DIR}/Inc"
                    ${CMSIS_INCLUDE_DIRS}
                    ${STM32HAL_INCLUDE_DIR}
                    ${STM32LL_INCLUDE_DIR}
					)

file(GLOB PROJECT_SOURCES
    "Src/*.c"
    )

ADD_EXECUTABLE( ${CMAKE_PROJECT_NAME}
                ${PROJECT_SOURCES} 
                ${CMSIS_SOURCES} 
                ${STM32HAL_SOURCES} 
                ${STM32LL_SOURCES}
                )

STM32_SET_TARGET_PROPERTIES(${CMAKE_PROJECT_NAME})
STM32_ADD_HEX_BIN_TARGETS(${CMAKE_PROJECT_NAME})

#cmake -DCMAKE_BUILD_TYPE=<DEBUG or RELEASE> .. && make