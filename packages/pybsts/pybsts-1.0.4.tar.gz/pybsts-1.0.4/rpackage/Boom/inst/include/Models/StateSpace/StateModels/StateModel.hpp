// Copyright 2018 Google LLC. All Rights Reserved.
#ifndef BOOM_STATE_SPACE_STATE_MODEL_HPP
#define BOOM_STATE_SPACE_STATE_MODEL_HPP
/*
  Copyright (C) 2008-2016 Steven L. Scott

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

#include "LinAlg/VectorView.hpp"
#include "Models/ModelTypes.hpp"
#include "Models/StateSpace/Filters/SparseMatrix.hpp"
#include "Models/StateSpace/Filters/SparseVector.hpp"
#include "uint.hpp"

namespace BOOM {

  class ScalarStateSpaceModelBase;
  class DynamicInterceptRegressionModel;

  namespace StateSpace {
    class TimeSeriesRegressionData;
  }  // StateSpace
  
  // A StateModel describes the propogation rules for one component of state in
  // a StateSpaceModel.  A StateModel has a transition matrix T, which can be
  // time dependent, an error variance Q, which may be of smaller dimension than
  // T, and a matrix R that can multiply draws from N(0, Q) so that the
  // dimension of RQR^T matches the state dimension.
  class StateModel : virtual public PosteriorModeModel {
   public:
    // Traditional state models are Gaussian, but Bayesian modeling lets you
    // work with conditionally Gaussian models just as easily.  For
    // conditionally Gaussian state models this enum can be used as an argument
    // to determine whether they should be viewed as normal mixtures, or as
    // plain old non-normal marginal models.
    enum Behavior {
      MARGINAL,  // e.g. treat the t-distribution like the t-distribution.
      MIXTURE    // e.g. treat the t-distribution like a normal mixture.
    };

    StateModel();
    ~StateModel() override {}
    StateModel *clone() const override = 0;

    // Some state models need to know the maximum value of t so they can set up
    // space for latent variables, etc.  Many state models do not need this
    // capability, so the default implementation is a no-op.
    virtual void observe_time_dimension(int max_time) {}

    // Add the relevant information from the state vector to the complete data
    // sufficient statistics for this model.  This is often a difference between
    // the current and previous state vectors.
    //
    // Args:
    //   then:  The state for this component at time_now - 1.
    //   now: The state for this component at time time_now.
    //   time_now:  The current time index.
    virtual void observe_state(const ConstVectorView &then,
                               const ConstVectorView &now,
                               int time_now) = 0;

    // Many models won't be able to do anything with an initial state, so the
    // default implementation is a no-op.
    virtual void observe_initial_state(const ConstVectorView &state);

    // The dimension of the state vector.
    virtual uint state_dimension() const = 0;

    // The dimension of the full-rank state error term.  This might be smaller
    // than state_dimension if the transition equation contains a deterministic
    // component.  For example, the seasonal model has state_dimension =
    // number_of_seasons - 1, but state_error_dimension = 1.
    virtual uint state_error_dimension() const = 0;

    // Add the observed error mean and variance to the complete data sufficient
    // statistics.  Child classes can choose to implement this method by
    // throwing an exception.
    virtual void update_complete_data_sufficient_statistics(
        int t, const ConstVectorView &state_error_mean,
        const ConstSubMatrix &state_error_variance) = 0;

    // Add the expected value of the derivative of log likelihood to the
    // gradient.  Child classes can choose to implement this method by throwing
    // an exception.
    //
    // Args:
    //   gradient: Subset of the gradient vector corresponding to this state
    //     model.
    //   t: The time index of the state innovation, which is for the
    //     t -> t+1 transition.
    //   state_error_mean: Subset of the state error mean for time t
    //     corresponding to this state model.
    //   state_error_variance: Subset of the state error variance for time t
    //     corresponding to this state model.
    virtual void increment_expected_gradient(
        VectorView gradient, int t, const ConstVectorView &state_error_mean,
        const ConstSubMatrix &state_error_variance);

    // Simulates the state eror at time t, for moving to time t+1.
    // Args:
    //   rng:  The random number generator to use for the simulation.
    //   eta: A view into the error term to be simulated.  ***NOTE*** eta.size()
    //     matches state_dimension(), not state_error_dimension().  If the error
    //     distribution is not full rank then some components of eta will be
    //     deterministic functions of others (most likely just zero).
    //   t: The time index of the error.  The convention is that state[t+1] =
    //     T[t] * state[t] + error[t], so errors at time t are part of the state
    //     at time t+1.
    virtual void simulate_state_error(RNG &rng, VectorView eta,
                                      int t) const = 0;
    virtual void simulate_initial_state(RNG &rng, VectorView eta) const;

    virtual Ptr<SparseMatrixBlock> state_transition_matrix(int t) const = 0;

    // The state_variance_matrix has state_dimension rows and columns.
    // This is Durbin and Koopman's R_t Q_t R_t^T
    virtual Ptr<SparseMatrixBlock> state_variance_matrix(int t) const = 0;

    // The state_expander_matrix has state_dimension rows and
    // state_error_dimension columns.  This is Durbin and Koopman's
    // R_t matrix.
    virtual Ptr<SparseMatrixBlock> state_error_expander(int t) const = 0;

    // The state_error_variance matrix has state_error_dimension rows
    // and columns.  This is Durbin and Koopman's Q_t matrix.
    virtual Ptr<SparseMatrixBlock> state_error_variance(int t) const = 0;

    // State models can have different notions of observation coefficients
    // depending on the type of model that owns them.  Each state space model
    // must know which function to call to get the right observation matrix,
    // observation coefficients, etc.

    // Observation coefficients for a ScalarStateModel(Base).
    virtual SparseVector observation_matrix(int t) const = 0;

    virtual Vector initial_state_mean() const = 0;
    virtual SpdMatrix initial_state_variance() const = 0;

    // Some state models can behave differently in different contexts.
    // E.g. they can be viewed as conditionally normal when fitting,
    // but as T or normal mixtures when forecasting.  These virtual
    // functions control how the state models swtich between roles.
    // The default behavior at construction should be
    // 'set_conditional_behavior', where a state model will behave as
    // conditionally Gaussian given an appropriate set of latent
    // variables.
    //
    // Because the traditional state models are actually Gaussian
    // (instead of simply conditionally Gaussian), the default
    // behavior for these member functions is a no-op.
    virtual void set_behavior(Behavior) {}

    // The index of a state model is its position in the vector of state models
    // maintained by the host model which owns the StateModel (e.g. a
    // StateSpaceModel.
    int index() const {return index_;}
    void set_index(int i) { index_ = i; }

    // Some models require constraints on the relationship between the state and
    // the model parameters in order to maintain identifiability.  Not all do,
    // so the default implementation of this function is a no-op.
    //
    // Effects:
    //   Modify the parameters so that they satisfy whatever identifiability
    //   constraints are assumed by the model.  Corresponding changes will be
    //   made to the state.  The resulting model will be equivalent to before
    //   this call, but for the constraints being satisfied.
    virtual void impose_identifiability_constraint() {}
    
   private:
    int index_;
  };

  //
  class StateModelAdapter : virtual public StateModel {
   public:
    StateModelAdapter(const Ptr<StateModel> &base) : base_(base) {}
    StateModelAdapter(const StateModelAdapter &rhs)
        : StateModel(rhs), base_(rhs.clone()) {}
    StateModelAdapter *clone() const override {return new StateModelAdapter(*this);}
    StateModelAdapter &operator=(const StateModelAdapter &rhs) {
      if (&rhs != this) {
        StateModel::operator=(rhs);
        base_.reset(rhs.base_->clone());
      }
      return *this;
    }

    //---------------------------------------------------------------------------
    // Overrides required by Model.
    ParamVector parameter_vector() override {
      return base_->parameter_vector();
    }

    const ParamVector parameter_vector() const override {
      return base_->parameter_vector();
    }

    void add_data(const Ptr<Data> &dp) override {
      base_->add_data(dp);
    }

    void clear_data() override { base_-> clear_data();}

    void combine_data(const Model &other_model, bool just_suf = true) override {
      base_->combine_data(other_model, just_suf);
    }

    void sample_posterior() override {base_->sample_posterior();}
    double logpri() const override {return base_->logpri();}
    void set_method(const Ptr<PosteriorSampler> &sampler) override {
      base_->set_method(sampler);
    }
    int number_of_sampling_methods() const override {
      return base_->number_of_sampling_methods();
    }
    
    //---------------------------------------------------------------------------
    // Overrides required by StateModel.
    void observe_time_dimension(int max_time) override {
      base_->observe_time_dimension(max_time);
    }

    void observe_state(const ConstVectorView &then, const ConstVectorView &now,
                       int time_now) override {
      base_->observe_state(then, now, time_now);
    }

    void observe_initial_state(const ConstVectorView &state) override {
      base_->observe_initial_state(state);
    }

    uint state_dimension() const override { return base_->state_dimension(); }

    uint state_error_dimension() const override {
      return base_->state_error_dimension();
    }

    void update_complete_data_sufficient_statistics(
        int t, const ConstVectorView &state_error_mean,
        const ConstSubMatrix &state_error_variance) override {
      base_->update_complete_data_sufficient_statistics(
          t, state_error_mean, state_error_variance);
    }

    void increment_expected_gradient(
        VectorView gradient, int t, const ConstVectorView &state_error_mean,
        const ConstSubMatrix &state_error_variance) override {
      base_->increment_expected_gradient(
          gradient, t, state_error_mean, state_error_variance);
    }

    void simulate_state_error(RNG &rng, VectorView eta, int t) const override {
      base_->simulate_state_error(rng, eta, t);
    }

    void simulate_initial_state(RNG &rng, VectorView eta) const override {
      base_->simulate_initial_state(rng, eta);
    }

    Ptr<SparseMatrixBlock> state_transition_matrix(int t) const override {
      return base_->state_transition_matrix(t);
    }

    Ptr<SparseMatrixBlock> state_variance_matrix(int t) const override {
      return base_->state_variance_matrix(t);
    }

    Ptr<SparseMatrixBlock> state_error_expander(int t) const override {
      return base_->state_error_expander(t);
    }

    Ptr<SparseMatrixBlock> state_error_variance(int t) const override {
      return base_->state_error_variance(t);
    }
    
    SparseVector observation_matrix(int t) const override {
      return base_->observation_matrix(t);
    }
    
    Vector initial_state_mean() const override {
      return base_->initial_state_mean();
    }

    SpdMatrix initial_state_variance() const override {
      return base_->initial_state_variance();
    }

    void set_behavior(Behavior behavior) override {
      base_->set_behavior(behavior);
    }

   protected:
    PosteriorSampler * sampler(int i) override { return base_->sampler(i); }
    PosteriorSampler const * const sampler(int i) const override {
      return base_->sampler(i);
    }
    
   private:
    Ptr<StateModel> base_;
    
  };
  
  //===========================================================================
  // A variant of a state model for use with dynamic intercept regression
  // models.
  class DynamicInterceptStateModel
      : virtual public StateModel {
   public:
    DynamicInterceptStateModel *clone() const override = 0;

    // Observation coefficients for a dynamic intercept regression model.
    // Args:
    //   t:  The time point for which coefficients are desired.
    //   data_point:  The data point managed by the model at time t.
    // Returns:
    //   The return value is a sparse number_of_observations X state_dimension
    //   matrix.  When multiplied by the state it gives the expected value for
    //   each of the observations at time t.
    using DataType = StateSpace::TimeSeriesRegressionData;
    virtual Ptr<SparseMatrixBlock> observation_coefficients(
        int t, const DataType &data_point) const;
  };

  //===========================================================================
  // The simple way to convert a StateModel into a DynamicInterceptStateModel.
  class DynamicInterceptStateModelAdapter
      : public DynamicInterceptStateModel,
        public StateModelAdapter {
   public:
    explicit DynamicInterceptStateModelAdapter(const Ptr<StateModel> &base)
        : StateModelAdapter(base) {}
    DynamicInterceptStateModelAdapter * clone() const override {
      return new DynamicInterceptStateModelAdapter(*this);
    }
    
    //---------------------------------------------------------------------------
    // This section contains all the overrides expected from Model.
    using StateModelAdapter::parameter_vector;
    using StateModelAdapter::add_data;
    using StateModelAdapter::clear_data;
    using StateModelAdapter::combine_data;
    using StateModelAdapter::sample_posterior;
    using StateModelAdapter::logpri;
    using StateModelAdapter::set_method;
    using StateModelAdapter::number_of_sampling_methods;

    //---------------------------------------------------------------------------
    // This section contains all the overrides expected from StateModel.
    using StateModelAdapter::observe_time_dimension;
    using StateModelAdapter::observe_state;
    using StateModelAdapter::observe_initial_state;
    using StateModelAdapter::state_dimension;
    using StateModelAdapter::state_error_dimension;
    using StateModelAdapter::update_complete_data_sufficient_statistics;
    using StateModelAdapter::increment_expected_gradient;
    using StateModelAdapter::simulate_state_error;
    using StateModelAdapter::simulate_initial_state;
    using StateModelAdapter::state_transition_matrix;
    using StateModelAdapter::state_variance_matrix;
    using StateModelAdapter::state_error_expander;
    using StateModelAdapter::state_error_variance;
    using StateModelAdapter::observation_matrix;
    using StateModelAdapter::initial_state_mean;
    using StateModelAdapter::initial_state_variance;
    using StateModelAdapter::set_behavior;

   protected:
    using StateModelAdapter::sampler;
  };

  //===========================================================================
  class MultivariateStateModel : virtual public StateModel {
   public:
    MultivariateStateModel *clone() const override = 0;

    SparseVector observation_matrix(int t) const override {
      report_error("MultivariateStateModel was used where a StateModel "
                   "was expected.");
      return SparseVector(0);
    }
    
    // The coefficients (Z) in the observation equation.  The coefficients are
    // arranged so that y = Z * state + error.  Thus columns of the observation
    // coefficients Z correspond to the state dimension.
    //
    // Args:
    //   t:  The time index of the observation.
    //   observed: Indicates which elements of the outcome variable are observed
    //     at time t.  Rows of Z corresponding to unobserved variables are
    //     omitted.
    virtual Ptr<SparseMatrixBlock> observation_coefficients(
        int t, const Selector &observed) const = 0;
  };
  
}  // namespace BOOM

#endif  // BOOM_STATE_SPACE_STATE_MODEL_HPP
