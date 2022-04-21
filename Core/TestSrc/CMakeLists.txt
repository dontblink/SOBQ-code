add_executable(suite_1_app
              template.c)

target_link_libraries( suite_1_app
                       unity
                     )

add_test(suite_1_test suite_1_app)
