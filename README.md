# SOBQ-code

CMake file meant to be run in this docker:
https://github.com/dontblink/Docker-armenv
Docker contains arm toolchain, STM32F4 HAL, and stm32-cmake.

mount folder and run docker:
docker run -it --rm -v $(pwd):/usr/project nirve/armenv:v1
to run in interactive mode. 

If you use vscode, there's a workspace file that maps the project file, stm32f4 hal/ll libraries, and the stm32-cmake library
use remote-containers extension, attach to the above running docker file, and vscode should find the workspace file on reboot.

build by going to /usr/project/core/build 
run cmake -DCMAKE_BUILD_TYPE=DEBUG .. && make
