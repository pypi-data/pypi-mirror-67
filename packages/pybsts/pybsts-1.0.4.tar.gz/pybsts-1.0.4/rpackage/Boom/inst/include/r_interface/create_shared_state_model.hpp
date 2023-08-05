#ifndef BOOM_R_INTERFACE_CREATE_SHARED_STATE_MODEL_HPP_
#define BOOM_R_INTERFACE_CREATE_SHARED_STATE_MODEL_HPP_
/*
  Copyright (C) 2005-2019 Steven L. Scott

  This library is free software; you can redistribute it and/or modify it under
  the terms of the GNU Lesser General Public License as published by the Free
  Software Foundation; either version 2.1 of the License, or (at your option)
  any later version.

  This library is distributed in the hope that it will be useful, but WITHOUT
  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
  FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
  details.

  You should have received a copy of the GNU Lesser General Public License along
  with this library; if not, write to the Free Software Foundation, Inc., 51
  Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
*/

#include "r_interface/list_io.hpp"
#include "r_interface/create_state_model.hpp"
#include <Models/StateSpace/StateSpaceModelBase.hpp>
#include <functional>
#include <list>

//==============================================================================
// The functions listed here throw exceptions.  Code that uses them should be
// wrapped in a try-block where the catch statement catches the exception and
// calls Rf_error() with an appropriate error message.  The functions
// handle_exception(), and handle_unknown_exception (in handle_exception.hpp),
// are suitable defaults.  These try-blocks should be present in any code called
// directly from R by .Call.
// ==============================================================================

namespace BOOM {

  // Forward declarations.  

  // Host model.
  class MultivariateStateSpaceModelBase;
  
  // Trend models.  This list will grow over time as more models are added.
  class SharedLocalLevelStateModel;

  namespace RInterface {

    // A factory for creating state components that are shared across multiple
    // time series.
    class SharedStateModelFactory : public StateModelFactoryBase {
     public:

      // Args:
      //   io_manager: A pointer to the object manaaging the R list that will
      //     record (or has already recorded) the MCMC output.  If a nullptr is
      //     passed then states will be created without IoManager support.
      explicit SharedStateModelFactory(RListIoManager *io_manager)
          : StateModelFactoryBase(io_manager) {}

      // Adds all the state components listed in
      // r_state_specification_list to the model.
      // Args:
      //   model: The model to which the state will be added.  
      //   r_state_specification_list: An R list of state components to be added
      //     to the model.  This function intended to handle the state
      //     specification argument in bsts.
      //   prefix: An optional prefix added to the name of each state component.
      void AddState(MultivariateStateSpaceModelBase *model,
                    SEXP r_shared_state_specification,
                    const std::string &prefix = "");

     private:
      // A factory function that unpacks information from an R object created by
      // AddXXX (where XXX is the name of a type of state model), and use it to
      // build the appropriate BOOM StateModel.  The specific R function
      // associated with each method is noted in the comments to the worker
      // functions that implement each specific type.
      //
      // Args:
      //   r_state_component:  The R object created by AddXXX.
      //   prefix: An optional prefix to be prepended to the name of the state
      //     component in the io_manager.
      //
      // Returns:
      //   A BOOM smart pointer to the appropriately typed MultivariateStateModel.
      Ptr<MultivariateStateModel> CreateSharedStateModel(
          MultivariateStateSpaceModelBase *model,
          SEXP r_state_component,
          const std::string &prefix);


      // Specific functions to create specific state models.
      Ptr<MultivariateStateModel> CreateSharedLocalLevel(
          SEXP r_state_component,
          MultivariateStateSpaceModelBase *model, 
          const std::string &prefix);
    };
    
  }  // namespace RInterface
  
}  // namespace BOOM

#endif  // BOOM_R_INTERFACE_CREATE_SHARED_STATE_MODEL_HPP_

