// Copyright 2018 The Simons Foundation, Inc. - All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "py_utils.hpp"

#include <pybind11/eigen.h>
#include "Utils/all_utils.hpp"

namespace py = pybind11;

namespace netket {

void AddUtilsModule(py::module m) {
  auto subm = m.def_submodule("utils");

  py::class_<netket::default_random_engine>(subm, "RandomEngine")
      .def(py::init<netket::default_random_engine::result_type>(),
           py::arg("seed") = netket::default_random_engine::default_seed)
      .def("seed", static_cast<void (netket::default_random_engine::*)(
                       netket::default_random_engine::result_type)>(
                       &netket::default_random_engine::seed));
  subm.def(
      "seed",
      [](const DistributedRandomEngine::ResultType &seed) {
        GetDistributedRandomEngine().Seed(seed);
      },
      py::arg("seed") = netket::default_random_engine::default_seed,
      R"EOF(seed: The chosen seed for the distributed random number generator.  )EOF");

  subm.def(
      "random_engine", []() { return; },
      R"EOF(seed: The random engine for the distributed random number generator.  )EOF");

  subm.def("rand_uniform_real",
           [](Eigen::Ref<Eigen::VectorXd> samples) {
             auto gen = GetDistributedRandomEngine().Get();
             std::uniform_real_distribution<> dis;

             for (Index i = 0; i < samples.size(); i++) {
               samples(i) = (dis(gen));
             }
           },
           py::arg("samples"));

  subm.def("rand_uniform_real",
           [](Eigen::Ref<Eigen::MatrixXd> samples) {
             auto gen = GetDistributedRandomEngine().Get();
             std::uniform_real_distribution<> dis;

             for (Index i = 0; i < samples.rows(); i++) {
               for (Index j = 0; j < samples.cols(); j++) {
                 samples(i, j) = (dis(gen));
               }
             }
           },
           py::arg("samples"));

  subm.def("rand_uniform_int",
           [](Index low, Index high, Eigen::Ref<Eigen::VectorXi> samples) {
             auto gen = GetDistributedRandomEngine().Get();
             std::uniform_int_distribution<> dis(low, high);

             for (Index i = 0; i < samples.size(); i++) {
               samples(i) = dis(gen);
             }
           },
           py::arg("low"), py::arg("high"), py::arg("samples"));

  subm.def("sum_log_cosh_complex",
           [](Eigen::Ref<const MatrixXcd> input, Eigen::Ref<VectorXcd> output) {
             SumLogCosh(input, output);
           },
           py::arg("input"), py::arg("output"));

  py::class_<MPIHelpers>(m, "MPI")
      .def_static("rank", &MPIHelpers::MPIRank,
                  R"EOF(int: The MPI rank for the current process.  )EOF")
      .def_static(
          "size", &MPIHelpers::MPISize,
          R"EOF(int: The total number of MPI ranks currently active.  )EOF");
}  // namespace netket

}  // namespace netket
