
from dataclasses import dataclass as _dataclass
from typing import List as _List

from ._network import Network

__all__ = ["Workspace"]


@_dataclass
class Workspace:
    """This class provides a workspace for the running calculation.
       This pre-allocates all of the memory into arrays, which
       can then be used via cython memory views
    """
    #: Number of disease classes (stages)
    n_inf_classes: int = 0

    #: Number of wards (nodes)
    nnodes: int = 0

    #: Size of population in each disease stage for work infections
    inf_tot: _List[int] = None
    #: Size of population in each disease stage for play infections
    pinf_tot: _List[int] = None
    #: Number of wards with at least one individual in this disease stage
    n_inf_wards: _List[int] = None

    #: Total number of infections in each ward over the last day
    #: This is also equal to the prevalence
    total_inf_ward: _List[int] = None

    #: Number of new infections in each ward over the last day
    total_new_inf_ward: _List[int] = None

    #: The incidence of the infection (sum of infections up to
    #: disease_class == 2)
    incidence: _List[int] = None

    @staticmethod
    def build(network: Network):
        """Create the workspace needed to run the model for the
           passed network
        """
        params = network.params

        workspace = Workspace()

        n_inf_classes = params.disease_params.N_INF_CLASSES()

        workspace.n_inf_classes = params.disease_params.N_INF_CLASSES()
        workspace.nnodes = network.nnodes

        size = workspace.nnodes + 1  # 1-indexed

        from .utils._array import create_int_array

        workspace.inf_tot = create_int_array(n_inf_classes, 0)
        workspace.pinf_tot = create_int_array(n_inf_classes, 0)
        workspace.n_inf_wards = create_int_array(n_inf_classes, 0)

        workspace.total_inf_ward = create_int_array(size, 0)
        workspace.total_new_inf_ward = create_int_array(size, 0)
        workspace.incidence = create_int_array(size, 0)

        return workspace

    def zero_all(self):
        """Reset the values of all of the arrays to zero"""
        for i in range(0, self.n_inf_classes):
            self.inf_tot[i] = 0
            self.pinf_tot[i] = 0
            self.n_inf_wards[i] = 0

        for i in range(0, self.nnodes+1):
            self.total_inf_ward[i] = 0
            self.total_new_inf_ward[i] = 0
            self.incidence[i] = 0
