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
//
// by S. Efthymiou, October 2018

#ifndef NETKET_MPS_PERIODIC_HPP
#define NETKET_MPS_PERIODIC_HPP

#include <map>

#include "Machine/abstract_machine.hpp"

namespace netket {

class MPSPeriodic : public AbstractMachine {
  // Number of sites
  int N_;
  // Physical dimension
  int d_;
  // Bond dimension
  int D_;
  // Second matrix dimension (D for normal MPS, 1 for diagonal)
  int Dsec_;
  // D squared
  int Dsq_;
  // Number of variational parameters
  int npar_;
  // Period of translational symmetry (has to be a divisor of N)
  int symperiod_;

  bool is_diag_;  ///< Whether the MPS is diagonal

  // Used for tree look up
  int Nleaves_;
  // Map from site that changes to the corresponding "leaves"
  // Shape (N_, nr of leaves for the corresponding site)
  std::vector<std::vector<int>> leaves_of_site_;
  // Contractions needed to produce each leaf
  // Shape (total leaves, 2)
  std::vector<std::vector<int>> leaf_contractions_;

  // MPS Matrices (stored as [symperiod, d, D, D] or [symperiod, d, D, 1])
  std::vector<std::vector<MatrixType>> W_;

  // Map from Hilbert states to MPS indices
  std::map<double, int> confindex_;
  // Identity Matrix
  MatrixType identity_mat_;

  using LookupType = std::vector<MatrixType>;

 public:
  MPSPeriodic(std::shared_ptr<const AbstractHilbert> hilbert, int bond_dim,
              bool diag, int symperiod = -1);

  int Npar() const override;
  int Nvisible() const override;

  VectorType GetParameters() override;
  void SetParameters(VectorConstRefType pars) override;
  any InitLookup(VisibleConstType v) override;
  void UpdateLookup(VisibleConstType v, const std::vector<int> &tochange,
                    const std::vector<double> &newconf, any &lt) override;

  Complex LogValSingle(VisibleConstType v, const any &lt) override;
  void LogValDiff(VisibleConstType v,
                  const std::vector<std::vector<int>> &tochange,
                  const std::vector<std::vector<double>> &newconf,
                  Eigen::Ref<Eigen::VectorXcd>) override;

  VectorType DerLogSingle(VisibleConstType v, const any &lt) override;

  void Save(const std::string &filename) const override;
  void Load(const std::string &filename) override;

  bool IsHolomorphic() const noexcept override;

 private:
  inline MatrixType prod(const MatrixType &m1, const MatrixType &m2) const;
  inline Complex trace(const MatrixType &m) const;
  inline void setparamsident(MatrixType &m, VectorConstRefType pars) const;
  inline void Init();
  inline void InitTree();
  // Auxiliary function used for setting initial random parameters and adding
  // identities in every matrix
  inline void SetParametersIdentity(VectorConstRefType pars);
  // Auxiliary function
  inline void _InitLookup_check(LookupType &lt, Index i);
  // Auxiliary function for sorting indeces
  // (copied from stackexchange - original answer by Lukasz Wiklendt)
  inline std::vector<std::size_t> sort_indeces(const std::vector<int> &v);
  // Auxiliary function that calculates contractions from site1 to site2
  inline MatrixType mps_contraction(VisibleConstType v, const int &site1,
                                    const int &site2);
};

}  // namespace netket

#endif
