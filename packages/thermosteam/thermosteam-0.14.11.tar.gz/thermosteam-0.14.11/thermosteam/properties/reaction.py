# -*- coding: utf-8 -*-
'''
All data and methods for estimating a chemical's heat of formation.

References
----------
.. [1] Albahri, Tareq A., and Abdulla F. Aljasmi. "SGC Method for
   Predicting the Standard Enthalpy of Formation of Pure Compounds from
   Their Molecular Structures." Thermochimica Acta 568
   (September 20, 2013): 46-60. doi:10.1016/j.tca.2013.06.020.
.. [2] Ruscic, Branko, Reinhardt E. Pinzon, Gregor von Laszewski, Deepti
    Kodeboyina, Alexander Burcat, David Leahy, David Montoy, and Albert F.
    Wagner. "Active Thermochemical Tables: Thermochemistry for the 21st
    Century." Journal of Physics: Conference Series 16, no. 1
    (January 1, 2005): 561. doi:10.1088/1742-6596/16/1/078.
.. [3] Frenkelʹ, M. L, Texas Engineering Experiment Station, and
    Thermodynamics Research Center. Thermodynamics of Organic Compounds in
    the Gas State. College Station, Tex.: Thermodynamics Research Center,
    1994.   
    
'''

__all__ = ('API_TDB_data', 
           'ATcT_l', 'ATcT_g', 
           'heat_of_formation', 
           'heat_of_formation_liquid',
           'heat_of_formation_gas',
)
           
from .heat_capacity import _TRC_gas
from .utils import CASDataReader, get_from_data_sources

read = CASDataReader(__file__, "Reactions")
API_TDB_data = read('API TDB Albahri Hf.tsv')
ATcT_l = read('ATcT 1.112 (l).tsv')
ATcT_g = read('ATcT 1.112 (g).tsv')


heat_of_formation_sources = {
    'API_TDB': API_TDB_data
}
heat_of_formation_liquid_sources = {
    'ATCT_L': ATcT_l
}
heat_of_formation_gas_sources = {
    'ATCT_G': ATcT_g,
    'TRC': _TRC_gas,
}

def heat_of_formation(CASRN, method='Any'):
    r'''
    Return a chemical's standard-phase heat of formation.
    The lookup is based on CASRNs. Selects the only
    data source available ('API TDB') if the chemical is in it.
    Return None if the data is not available.

    Function has data for 571 chemicals.

    Parameters
    ----------
    CASRN : string
        CASRN [-].

    Returns
    -------
    Hf : float
        Standard-state heat of formation [J/mol].

    Other Parameters
    ----------------
    method : string, optional
        The method name to use. If method is "Any", the first available
        value from these methods will returned. If method is "All",
        a dictionary of method results will be returned.

    Notes
    -----
    Only one source of information is available to this function. it is:

        * 'API_TDB', a compilation of heats of formation of unspecified phase.
          Not the original data, but as reproduced in [1]_. Some chemicals with
          duplicated CAS numbers were removed.

    Examples
    --------
    >>> Hf(CASRN='7732-18-5')
    -241820.0

    '''
    return get_from_data_sources(heat_of_formation_sources, CASRN, 'Hf', method)

def heat_of_formation_liquid(CASRN, method='Any'):
    r'''
    Return a chemical's liquid standard phase heat of formation. 
    The lookup is based on CASRNs. Selects the only data source available,
    Active Thermochemical Tables (l), if the chemical is in it.
    Return None if the data is not available.

    Function has data for 34 chemicals.

    Parameters
    ----------
    CASRN : string
        CASRN [-]

    Returns
    -------
    Hf_l : float
        Liquid standard-state heat of formation, [J/mol]

    Other Parameters
    ----------------
    method : string, optional
        The method name to use. If method is "Any", the first available
        value from these methods will returned. If method is "All",
        a dictionary of method results will be returned.

    Notes
    -----
    Only one source of information is available to this function. It is:

        * 'ATCT_L', the Active Thermochemical Tables version 1.112. [2]_

    Examples
    --------
    >>> heat_of_formation_liquid('67-56-1')
    -238400.0

    '''
    return get_from_data_sources(heat_of_formation_liquid_sources,
                                 CASRN, 'Hf_298K', method)


def heat_of_formation_gas(CASRN, method='Any'):
    r'''
    Retrieve a chemical's gas heat of formation. Lookup is based on CASRNs. 
    Automatically select a data source to use if no Method is provided.
    Return None if the data is not available.

    Prefered sources are 'Active Thermochemical Tables (g)' for high accuracy,
    and 'TRC' for less accuracy but more chemicals.
    Function has data for approximately 2000 chemicals.

    Parameters
    ----------
    CASRN : string
        CASRN [-]

    Returns
    -------
    Hf_g : float
        Gas phase heat of formation, [J/mol]

    Other Parameters
    ----------------
    method : string, optional
        The method name to use. If method is "Any", the first available
        value from these methods will returned. If method is "All",
        a dictionary of method results will be returned.
    
    Notes
    -----
    Sources are:

        * 'ATCT_G', the Active Thermochemical Tables version 1.112. [2]_
        * 'TRC', from a 1994 compilation. [3]_

    Examples
    --------
    >>> Hf_g('67-56-1')
    -200700.0

    '''
    if method == 'All':
        Hf_g = {'ATCT_G': ATcT_g.retrieve(CASRN, 'Hf_298K'),
              'TRC': _TRC_gas.retrieve(CASRN, 'Hf'),
              }
    elif method == 'Any':
        Hf_g = ATcT_g.retrieve(CASRN, 'Hf_298K')
        if Hf_g is None:
            Hf_g = _TRC_gas.retrieve(CASRN, 'Hf')
    elif method == 'ATCT_G':
        Hf_g = ATcT_g.retrieve(CASRN, 'Hf_298K')
    elif method == 'TRC':
        Hf_g = _TRC_gas.retrieve(CASRN, 'Hf')
    else:
        raise ValueError("invalid method; method must be one of the following: "
                         "'TRC', or 'ATCT_G'.")
    return Hf_g
   