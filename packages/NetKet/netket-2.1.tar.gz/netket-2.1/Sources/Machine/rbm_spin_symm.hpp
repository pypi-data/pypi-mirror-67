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

#ifndef NETKET_RBM_SPIN_SYMM_HPP
#define NETKET_RBM_SPIN_SYMM_HPP

#include "Machine/abstract_machine.hpp"

namespace netket {

// Rbm with permutation symmetries
class RbmSpinSymm : public AbstractMachine {
  const AbstractGraph &graph_;

  // number of visible units
  int nv_;

  // ratio of hidden/visible
  int alpha_;

  // number of hidden units
  int nh_;

  // number of parameters
  int npar_;

  // number of parameters without symmetries
  int nbarepar_;

  std::vector<std::vector<int>> permtable_;
  int permsize_;

  // weights
  MatrixType W_;

  // weights with symmetries
  MatrixType Wsymm_;

  // visible units bias
  VectorType a_;

  Complex asymm_;

  // hidden units bias
  VectorType b_;

  VectorType bsymm_;

  VectorType thetas_;
  VectorType thetasnew_;

  Eigen::MatrixXd DerMatSymm_;

  bool usea_;
  bool useb_;

 public:
  RbmSpinSymm(std::shared_ptr<const AbstractHilbert> hilbert, int alpha = 0,
              bool usea = true, bool useb = true);

  int Npar() const override;
  int Nvisible() const override;
  int Nhidden() const { return nh_; }

  VectorType DerLogSingle(VisibleConstType v, const any &lt) override;

  VectorType GetParameters() override;
  void SetParameters(VectorConstRefType pars) override;

  Complex LogValSingle(VisibleConstType v, const any &lt) override;

  void LogVal(Eigen::Ref<const RowMatrix<double>> x,
              Eigen::Ref<Eigen::VectorXcd> out, const any &) override;

  void Save(const std::string &filename) const override;
  void Load(const std::string &filename) override;

  bool IsHolomorphic() const noexcept override;

 private:
  inline void Init(const AbstractGraph &graph);

  VectorType BareDerLog(VisibleConstType v);
  void SetBareParameters();
};

}  // namespace netket

#endif
