// Copyright 2018-2019 The Simons Foundation, Inc. - All Rights Reserved.
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

#include "pauli_strings.hpp"

namespace netket {

PauliStrings::PauliStrings(const std::vector<std::string> &ops,
                           const std::vector<Complex> &opweights,
                           double cutoff = 1e-10)
    : AbstractOperator(std::make_shared<CustomHilbert>(
          GraphFromOps(ops), std::vector<double>{0., 1.})),
      nqubits_(GetHilbert().Size()),
      noperators_(ops.size()),
      I_(Complex(0, 1)),
      cutoff_(cutoff) {
  std::vector<std::vector<int>> tochange(noperators_);
  std::vector<Complex> weights = opweights;
  std::vector<std::vector<int>> zcheck(noperators_);
  int nchanges = 0;

  if (static_cast<int>(opweights.size()) != noperators_) {
    throw InvalidInputError(
        "Operator weights size is inconsistent with number of operators");
  }

  for (int i = 0; i < noperators_; i++) {
    for (int j = 0; j < nqubits_; j++) {
      if (ops[i][j] == 'X') {
        tochange[i].push_back(j);
        nchanges++;
      } else if (ops[i][j] == 'Y') {
        tochange[i].push_back(j);
        weights[i] *= I_;
        zcheck[i].push_back(j);
        nchanges++;
      } else if (ops[i][j] == 'Z') {
        zcheck[i].push_back(j);
      } else if (ops[i][j] != 'I') {
        throw InvalidInputError(
            "Operator in string is not a Pauli or Identity");
      }
    }
  }

  for (int i = 0; i < noperators_; i++) {
    auto tc = tochange[i];
    auto it = std::find(std::begin(tochange_), std::end(tochange_), tc);
    if (it != tochange_.end()) {
      int index = std::distance(tochange_.begin(), it);
      weights_[index].push_back(weights[i]);
      zcheck_[index].push_back(zcheck[i]);
    } else {
      tochange_.push_back(tc);
      weights_.push_back({weights[i]});
      zcheck_.push_back({zcheck[i]});
    }
  }

  InfoMessage() << "Pauli Operator created " << std::endl;
  InfoMessage() << "Nqubits = " << nqubits_ << std::endl;
  InfoMessage() << "Noperators = " << noperators_ << std::endl;
}

Edgeless PauliStrings::GraphFromOps(const std::vector<std::string> &ops) {
  const auto nqubits = CheckOps(ops);
  return Edgeless(nqubits);
}

Index PauliStrings::CheckOps(const std::vector<std::string> &ops) {
  if (ops.size() == 0) {
    throw InvalidInputError("No Pauli operators passed");
  }

  Index nqubits = ops[0].size();
  for (const auto op : ops) {
    if (static_cast<Index>(op.size()) != nqubits) {
      throw InvalidInputError(
          "Operator size is inconsistent with number of qubits");
    }
  }
  return nqubits;
}

void PauliStrings::FindConn(VectorConstRefType v, std::vector<Complex> &mel,
                            std::vector<std::vector<int>> &connectors,
                            std::vector<std::vector<double>> &newconfs) const {
  assert(v.size() == nqubits_);

  connectors.resize(0);
  newconfs.resize(0);
  mel.resize(0);
  for (std::size_t i = 0; i < tochange_.size(); i++) {
    Complex mel_temp = 0.0;
    for (std::size_t j = 0; j < weights_[i].size(); j++) {
      Complex m_temp = weights_[i][j];
      for (auto k : zcheck_[i][j]) {
        assert(k >= 0 && k < v.size());
        if (int(std::round(v(k))) == 1) {
          m_temp *= -1.;
        }
      }
      mel_temp += m_temp;
    }
    if (std::abs(mel_temp) > cutoff_) {
      std::vector<double> newconf_temp(tochange_[i].size());
      int jj = 0;
      for (auto sj : tochange_[i]) {
        assert(sj < v.size() && sj >= 0);
        if (int(std::round(v(sj))) == 0) {
          newconf_temp[jj] = 1;
        } else {
          newconf_temp[jj] = 0;
        }
        jj++;
      }

      newconfs.push_back(newconf_temp);
      connectors.push_back(tochange_[i]);
      mel.push_back(mel_temp);
    }
  }
}

}  // namespace netket
