#tasks.py
#invoke will run from any child directory and go up directories until it finds a tasks.py file
#all file paths are relative from location of script, so do not remove from top level directory
#this allows invoke to be run from any folder in the project
import shutil, os
from invoke import task, run


@task
def clean_cmake(ctx, build_type):
    """Deletes and re-creates cmake build folder"""
    if build_type.lower() == "all":
        lst = {"Debug", "Release", "Test"}
    else:
        if build_type.lower() == "debug" or \
            build_type.lower() == "release" or \
            build_type.lower() == "test":
            lst = {build_type.lower().capitalize()}
        else:
            print("Fuck")
            return

    root = os.path.dirname(os.path.abspath(__file__))
    #iterate through list and clean appropriate folder
    for item in lst:
        directory = os.path.dirname(os.path.abspath(__file__))+"\\Core\\"+item
        print(directory)

        #check to make sure directory exists, otherwise rmtree fails
        if(os.path.isdir(directory)):
            shutil.rmtree(directory)
        #os.mkdir(directory)
        command = ("docker run -w /usr/project/ --rm" \
                + " -v \"{}\":/usr/project nirve/armenv:v1".format(root) \
                + " cmake -S . -B {}/".format(item) \
                + " -DCMAKE_TOOLCHAIN_FILE=/usr/lib/stm32-cmake/cmake/stm32_gcc.cmake"
                + " -DSTM32_TOOLCHAIN_PATH=/home/dev/gcc-arm-none-eabi" \
                + " -DSTM32_TARGET_TRIPLET=arm-none-eabi" \
                + " -DSTM32_CUBE_F4_PATH=/usr/lib/STM32CUBEF4"
                + " -DTARGET_GROUP={}".format(item)
                )
        print(command)
        run(command)

        #build_cmake(ctx, build_type)

@task
def clean_test(ctx):
    root = os.path.dirname(os.path.abspath(__file__))
    directory = os.path.dirname(os.path.abspath(__file__))+"\\Core\\Test"
    print(directory)

    #check to make sure directory exists, otherwise rmtree fails
    if(os.path.isdir(directory)):
        shutil.rmtree(directory)
    #os.mkdir(directory)
    command = ("docker run -w /usr/project/ --rm" \
            + " -v \"{}\":/usr/project nirve/armenv:v1".format(root) \
            + " cmake -S . -B Test/" \
            #+ " -DCMAKE_TOOLCHAIN_FILE=/usr/lib/stm32-cmake/cmake/stm32_gcc.cmake"
            #+ " -DSTM32_TOOLCHAIN_PATH=/home/dev/gcc-arm-none-eabi" \
            #+ " -DSTM32_TARGET_TRIPLET=arm-none-eabi" \
            #+ " -DSTM32_CUBE_F4_PATH=/usr/lib/STM32CUBEF4"
            + " -DTARGET_GROUP=Test"
            )
    print(command)
    run(command)

@task(help={"build_type": "Debug, Release, or All"})
def build(ctx, build_type):
    """Builds makefile using cmake"""
    
    if build_type.lower() == "all":
        lst = {"Debug", "Release", "Test"}
    else:
        if build_type.lower() == "debug" or \
            build_type.lower() == "release" or \
            build_type.lower() == "test":
            lst = {build_type.lower().capitalize()}
        else:
            print("It's Fucked")        
            return

    for item in lst:
        print("Building Cmake as {}".format(item))
        root = os.path.dirname(os.path.abspath(__file__))
        
        # run docker file, change to build folder, remove container on exit
        # mount project in /usr/project
        # run cmake for the given build configuration
        command = ("docker run -w /usr/project/ --rm" \
                + " -v \"{}\":/usr/project nirve/armenv:v1".format(root) \
                + " cmake --build {}".format(item) \
                )        
        print(command)
        run(command)


@task
def run_interactive(ctx):
    root = os.path.dirname(os.path.abspath(__file__))
    print(root)
    command = 'docker run -it --rm -v \"{}\":/usr/project nirve/armenv:v1'.format(root)
    run(command)

# @task(help={'clean':"prints shit"})
# def build(ctx, build_type):
#     """Builds elf using make"""
    
#     if build_type.lower() == "all":
#         lst = {"Debug", "Release"}
#     else:
#         if build_type.lower() == "debug" or build_type.lower() == "release":
#             lst = {build_type.lower().capitalize()}
#         else:
#             print("It's Fucked")        
#             return

#     for item in lst:
#         print("make as {}".format(item))
#         root = os.path.dirname(os.path.abspath(__file__))
        
#         # run docker file, change to build folder, remove container on exit
#         # mount project in /usr/project
#         # run cmake for the given build configuration
#         command = ("docker run -w /usr/project/{} --rm".format(item) \
#                 + " -v \"{}\":/usr/project nirve/armenv:v1".format(root) \
#                 + " make ." )
#         print(command)
#         run(command)
