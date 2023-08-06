

if(TIMEMORY_BUILD_AVAIL)
    add_executable(timemory-avail
        ${CMAKE_CURRENT_LIST_DIR}/timemory-avail.cpp
        ${CMAKE_CURRENT_LIST_DIR}/timemory-avail.hpp)
    target_include_directories(timemory-avail PRIVATE ${CMAKE_CURRENT_LIST_DIR})
    target_link_libraries(timemory-avail PRIVATE timemory-extensions timemory-headers)
    set_target_properties(timemory-avail PROPERTIES INSTALL_RPATH_USE_LINK_PATH ON)
    install(TARGETS timemory-avail DESTINATION bin)

    add_executable(timemory-yaml
        ${CMAKE_CURRENT_LIST_DIR}/timemory-yaml.cpp)
    target_include_directories(timemory-yaml PRIVATE ${CMAKE_CURRENT_LIST_DIR})
    target_compile_options(timemory-yaml PRIVATE "-O0" "-g")
    target_link_libraries(timemory-yaml PRIVATE timemory-extensions timemory-headers)
    set_target_properties(timemory-yaml PROPERTIES INSTALL_RPATH_USE_LINK_PATH ON)
    install(TARGETS timemory-yaml DESTINATION bin)
endif()
