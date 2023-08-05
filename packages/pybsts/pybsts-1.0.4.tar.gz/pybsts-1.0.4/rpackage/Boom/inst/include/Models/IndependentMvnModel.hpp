// Copyright 2018 Google LLC. All Rights Reserved.
/*
  Copyright (C) 2012 Steven L. Scott

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
*/

#ifndef BOOM_INDEPENDENT_MVN_MODEL_HPP
#define BOOM_INDEPENDENT_MVN_MODEL_HPP

#include "Models/EmMixtureComponent.hpp"
#include "Models/GaussianModelBase.hpp"
#include "Models/MvnBase.hpp"
#include "Models/Policies/ParamPolicy_2.hpp"
#include "Models/Policies/PriorPolicy.hpp"
#include "Models/Policies/SufstatDataPolicy.hpp"
#include "LinAlg/DiagonalMatrix.hpp"

namespace BOOM {
  class IndependentMvnSuf : public SufstatDetails<VectorData> {
   public:
    explicit IndependentMvnSuf(int dim);
    IndependentMvnSuf *clone() const override;

    void clear() override;
    void resize(int dim);
    void Update(const VectorData &) override;
    void update_raw(const Vector &y);
    void update_single_dimension(double y, int position);
    void add_mixture_data(const Vector &v, double prob);

    // Increment the sample size, sum, and sum_of_squares by specified amounts.
    void update_expected_value(double sample_size, const Vector &expected_sum,
                               const Vector &expected_sum_of_squares);

    // The sum of observations for the variable in position i.
    double sum(int i) const;

    // The sum of squares of observations for the variable in position i.
    double sumsq(int i) const;  // uncentered sum of squares

    // The centered sum of squared observations for the variable in position i.
    double centered_sumsq(int i, double mu) const;

    // The number of observations in position i.
    double n(int i = 0) const;

    // The sample mean of variable in position i.
    double ybar(int i) const;

    // The sample variance of the variable in position i.
    double sample_var(int i) const;

    IndependentMvnSuf *abstract_combine(Sufstat *s) override;
    void combine(const Ptr<IndependentMvnSuf> &);
    void combine(const IndependentMvnSuf &);
    Vector vectorize(bool minimal = true) const override;
    Vector::const_iterator unvectorize(Vector::const_iterator &v,
                                       bool minimal = true) override;
    Vector::const_iterator unvectorize(const Vector &v,
                                       bool minimal = true) override;
    ostream &print(ostream &out) const override;

   private:
    std::vector<GaussianSuf> suf_;
  };

  class IndependentMvnModel
      : public MvnBase,
        public ParamPolicy_2<VectorParams, VectorParams>,
        public SufstatDataPolicy<VectorData, IndependentMvnSuf>,
        public PriorPolicy,
        virtual public EmMixtureComponent {
   public:
    explicit IndependentMvnModel(int dim);
    IndependentMvnModel(const Vector &mean, const Vector &variance);
    IndependentMvnModel(const IndependentMvnModel &rhs);
    IndependentMvnModel *clone() const override;

    void add_mixture_data(const Ptr<Data> &dp, double weight) override;
    void mle() override;
    
    // Several virtual functions from MvnBase are re-implemented here
    // for efficiency.
    double Logp(const Vector &x, Vector &g, Matrix &h,
                uint nderivs) const override;
    const Vector &mu() const override;
    const SpdMatrix &Sigma() const override;
    const SpdMatrix &siginv() const override;
    DiagonalMatrix diagonal_variance() const;
    double ldsi() const override;
    Vector sim(RNG &rng = GlobalRng::rng) const override;

    Ptr<VectorParams> Mu_prm();
    const Ptr<VectorParams> Mu_prm() const;
    const VectorParams &Mu_ref() const;

    Ptr<VectorParams> Sigsq_prm();
    const Ptr<VectorParams> Sigsq_prm() const;
    const VectorParams &Sigsq_ref() const;

    const Vector &sigsq() const;
    double mu(int i) const;
    double sigsq(int i) const;
    double sigma(int i) const;

    void set_mu(const Vector &mu);
    void set_mu_element(double value, int position);
    void set_sigsq(const Vector &sigsq);
    void set_sigsq_element(double sigsq, int position);

    double pdf(const Data *dp, bool logscale) const override;
    int number_of_observations() const override { return dat().size(); }

   private:
    mutable SpdMatrix sigma_scratch_;
    mutable Vector g_;
    mutable Matrix h_;
  };

}  // namespace BOOM
#endif  //  BOOM_INDEPENDENT_MVN_MODEL_HPP
