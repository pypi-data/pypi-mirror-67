// Copyright 2018 The Simons Foundation, Inc. - All
// Rights Reserved.
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
//
// by G. Mazzola, May-Aug 2018

#ifndef NETKET_JAS_SYMM_HPP
#define NETKET_JAS_SYMM_HPP

#include "Machine/abstract_machine.hpp"

namespace netket {

// Jastrow with permutation symmetries
class JastrowSymm : public AbstractMachine {
  const AbstractGraph &graph_;

  std::vector<std::vector<int>> permtable_;
  int permsize_;

  // number of visible units
  int nv_;

  // number of parameters
  int npar_;

  // number of parameters without symmetries
  int nbarepar_;

  // weights
  MatrixType W_;

  // weights with symmetries
  MatrixType Wsymm_;

  VectorType thetas_;
  VectorType thetasnew_;

  Eigen::MatrixXd DerMatSymm_;
  Eigen::MatrixXi Wtemp_;

 public:
  explicit JastrowSymm(std::shared_ptr<const AbstractHilbert> hilbert);

  int Nvisible() const override;
  int Npar() const override;

  VectorType DerLogSingle(VisibleConstType v, const any &cache) override;

  VectorType GetParameters() override;
  void SetParameters(VectorConstRefType pars) override;

  Complex LogValSingle(VisibleConstType v, const any &) override;

  void LogVal(Eigen::Ref<const RowMatrix<double>> x,
              Eigen::Ref<Eigen::VectorXcd> out, const any &) override;

  void LogValDiff(VisibleConstType v,
                  const std::vector<std::vector<int>> &tochange,
                  const std::vector<std::vector<double>> &newconf,
                  Eigen::Ref<Eigen::VectorXcd>) override;

  void Save(const std::string &filename) const override;
  void Load(const std::string &filename) override;

  bool IsHolomorphic() const noexcept override;

 private:
  inline void Init(const AbstractGraph &graph);

  VectorType BareDerLog(VisibleConstType v);
  void SetBareParameters();
};

}  // namespace netket

#endif  // NETKET_JAS_SYMM_HPP
