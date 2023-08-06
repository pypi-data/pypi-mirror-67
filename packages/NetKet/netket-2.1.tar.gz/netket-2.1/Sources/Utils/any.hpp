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

#ifndef SOURCES_UTILS_ANY_HPP
#define SOURCES_UTILS_ANY_HPP

#include <any.hpp>
#include <iostream>

namespace netket {

using linb::any;
using linb::any_cast;
using linb::bad_any_cast;

template <class T>
T& any_cast_ref(any& x) {
  T* p = any_cast<T>(&x);
  if (p == nullptr) throw bad_any_cast{};
  return *p;
}

template <class T>
const T& any_cast_ref(any const& x) {
  const T* p = any_cast<T>(&x);
  if (p == nullptr) throw bad_any_cast{};
  return *p;
}

}  // namespace netket

#endif  // SOURCES_UTILS_ANY_HPP
