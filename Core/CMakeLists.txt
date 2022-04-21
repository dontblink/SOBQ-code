add_library(project_sources STATIC
			"Src/gpio.c"
		    "Src/stm32f4xx_hal_msp.c"
		    "Src/stm32f4xx_it.c"
		    "Src/system_stm32f4xx.c"
		    "Src/usart.c"     )
target_include_directories(project_sources PUBLIC Inc)

target_link_libraries(project_sources
                		HAL::STM32::F4::CORTEX
						HAL::STM32::F4::RCC
						HAL::STM32::F4::GPIO
						HAL::STM32::F4::TIM
						HAL::STM32::F4::UART
						HAL::STM32::F4::DMA
						HAL::STM32::F4::LL_UTILS
						HAL::STM32::F4::LL_EXTI
						HAL::STM32::F4::LL_USB
						CMSIS::STM32::F4    
						STM32::NoSys
					)

target_compile_definitions(
    project_sources PUBLIC 
    USE_HAL_DRIVER=1
    STM32F401xE=1
    )
