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

#ifndef NETKET_ABSTRACTLAYER_HH
#define NETKET_ABSTRACTLAYER_HH

#include <complex>
#include <fstream>
#include <random>
#include <vector>

#include <Eigen/Dense>
#include <nlohmann/json_fwd.hpp>

#include "Machine/abstract_machine.hpp"

namespace netket {
/**
  Abstract class for Neural Network layer.
*/
class AbstractLayer {
 public:
  using VectorType = AbstractMachine::VectorType;
  using MatrixType = AbstractMachine::MatrixType;
  using VectorRefType = AbstractMachine::VectorRefType;
  using VectorConstRefType = AbstractMachine::VectorConstRefType;
  using VisibleConstType = AbstractMachine::VisibleConstType;

  /**
  Member function returning the name of the layer.
  @return Name of Layer.
  */
  virtual std::string Name() const = 0;
  /**
  Member function returning the number of inputs a layer takes.
  @return Number of Inputs into the Layer.
  */
  virtual int Ninput() const = 0;

  /**
  Member function returning the number of outputs from the layer.
  @return Number of Outputs from the Layer.
  */
  virtual int Noutput() const = 0;

  /**
  Member function returning the number of variational parameters.
  @return Number of variational parameters in the Layer.
  */
  virtual int Npar() const = 0;

  /**
  Member function writing the current set of parameters in the machine.
  @param pars is where the layer parameters are written into.
  @param start_idx is the index of the vector pars to start writing from.
  */
  virtual void GetParameters(VectorRefType pars) const = 0;

  /**
  Member function setting the current set of parameters in the layer.
  @param pars is where the layer parameters are to be read from.
  @param start_idx is the index of the vector pars to start reading from.
  */
  virtual void SetParameters(VectorConstRefType pars) = 0;

  /**
  Member function providing a random initialization of the parameters.
  @param seed is the see of the random number generator.
  @param sigma is the variance of the gaussian.
  */
  virtual void InitRandomPars(int seed, double sigma) = 0;

  /**
  Member function to feedforward through the layer. Writes the output into
  output
  @param input a constant reference to the input to the layer
  @param output reference to the output vector.
  */
  virtual void Forward(const VectorType &input, VectorType &output) = 0;

  /**
  Member function to perform backpropagation to compute derivates.
  @param prev_layer_output a constant reference to the output from previous
  layer.
  @param this_layer_output a constant reference to the output from the current
  layer.
  @param next_layer_data a constant reference to the derivative dL/dA where A is
  the activations of the current layer and L is the the final output of the
  Machine: L = log(psi(v))
  @param din a constant reference to the derivative of the input from the
  current layer.
  @param der a constant reference to the derivatives wrt to the parameters in
  the machine.
  */
  virtual void Backprop(const VectorType &prev_layer_output,
                        const VectorType &this_layer_output,
                        const VectorType &dout, VectorType &din,
                        VectorRefType der) = 0;

  virtual void to_json(nlohmann::json &j) const = 0;

  virtual void from_json(const nlohmann::json &j) = 0;

  /**
  destructor
  */
  virtual ~AbstractLayer() {}
};
}  // namespace netket

#endif
