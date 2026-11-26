#include "interface.hpp"

#include <pybind11/embed.h>
#include <exception>
#include <iostream>

namespace py = pybind11;

double Interface::python_getCurrentPrice(std::string stock) {
    py::scoped_interpreter python{};

    try {
        py::module_ interface = py::module_::import("interface");
        py::object py_price = interface.attr("get_current_price")(stock);

        double price = py_price.cast<double>();
        return price;
    } catch (const std::exception& e) {
        std::cerr << "Exception in python_getCurrentPrice:\n" << e.what() << std::endl;
        return EXIT_FAILURE;
    }

}

