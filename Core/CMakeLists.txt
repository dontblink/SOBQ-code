#setup configuration variables for stm32-cmake
set(STM32_CHIP STM32F401RE)
set(STM32_CUBE_F4_PATH "/usr/lib/STM32CUBEF4")
set(STM32_TOOLCHAIN_PATH "/home/dev/gcc-arm-none-eabi")
set(CMAKE_MODULE_PATH "/usr/lib/stm32-cmake/cmake")
set(CMAKE_TOOLCHAIN_FILE "/usr/lib/stm32-cmake/cmake/stm32_gcc.cmake")
set(UNITY_DIR "/usr/lib/unity")

cmake_minimum_required(VERSION 3.16)
project(lolkillme LANGUAGES C )

#set(CMAKE_CXX_COMPILER $(TOOLCHAIN_PREFIX))
#set(STM32_LINKER_SCRIPT ${CMSIS_LINKER_SCRIPT})
#set(PROJECT_SOURCE_DIR "./Core")

FIND_PACKAGE(CMSIS COMPONENTS STM32F4 REQUIRED)
#FIND_PACKAGE(HAL COMPONENTS gpio tim usart dma rcc REQUIRED)
FIND_PACKAGE(HAL COMPONENTS STM32F4 REQUIRED)
set(CMAKE_INCLUDE_CURRENT_DIR TRUE)
#FIND_PACKAGE(STM32LL COMPONENTS utils exti usb REQUIRED)
INCLUDE_DIRECTORIES (
                    #${CMAKE_CURRENT_SOURCE_DIR}
                    "${PROJECT_SOURCE_DIR}/Inc"
                    #${CMSIS_INCLUDE_DIRS}
                    #${STM32HAL_INCLUDE_DIR}
                    #${STM32LL_INCLUDE_DIR}
					)

file(GLOB PROJECT_SOURCES
    "Src/*.c"
    )

ADD_EXECUTABLE( ${CMAKE_PROJECT_NAME}
                ${PROJECT_SOURCES} 
               # ${CMSIS_SOURCES} 
                #${STM32HAL_SOURCES} 
                #${STM32LL_SOURCES}
                )
TARGET_LINK_LIBRARIES(${CMAKE_PROJECT_NAME} 
                      CMSIS::STM32::F401RE
                      HAL::STM32::F4::RCC
                      HAL::STM32::F4::CORTEX
                      HAL::STM32::F4::GPIO
                      HAL::STM32::F4::TIM
                      HAL::STM32::F4::USART
                      HAL::STM32::F4::DMA
                      HAL::STM32::F4::LL_UTILS
                      HAL::STM32::F4::LL_EXTI
                      HAL::STM32::F4::LL_USB
                      STM32::Nano::FloatPrint

                      )

#STM32_SET_TARGET_PROPERTIES(${CMAKE_PROJECT_NAME})
#STM32_ADD_HEX_BIN_TARGETS(${CMAKE_PROJECT_NAME})

#cmake -DCMAKE_BUILD_TYPE=<DEBUG or RELEASE> .. && make
