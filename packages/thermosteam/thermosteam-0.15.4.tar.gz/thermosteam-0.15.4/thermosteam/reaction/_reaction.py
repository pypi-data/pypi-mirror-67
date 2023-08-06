# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:23:52 2019

@author: yoelr
"""
from . import _parse as prs
from ..utils import chemicals_user
from .._phase import NoPhase
from ..indexer import ChemicalIndexer
import numpy as np

__all__ = ('Reaction', 'ParallelReaction', 'SeriesReaction')

@chemicals_user
class Reaction:
    """Create a Reaction object which defines a stoichiometric reaction and conversion. When called, it returns the change in material due to the reaction.
    
    Parameters
    ----------
    reaction : dict or str
               A dictionary of stoichiometric coefficients or a stoichiometric equation written as:
               i1 R1 + ... + in Rn -> j1 P1 + ... + jm Pm
    reactant : str
               ID of reactant compound.
    X : float
        Reactant conversion (fraction).
    chemicals=None : Chemicals, defaults to settings.chemicals.
        Chemicals corresponing to each entry in the stoichiometry array.
    
    Examples
    --------
    >>> import thermosteam as tmo
    >>> import thermosteam.reaction as rxn
    >>> chemicals = tmo.Chemicals(['H2O', 'H2', 'O2'])
    >>> tmo.settings.set_thermo(chemicals)
    >>> srn = rxn.Reaction('2H2O -> 2H2 + O2', reactant='H2O', X=0.7)
    >>> srn.show()
    Reaction:
     stoichiometry       reactant    X[%]
     H2O -> H2 + 0.5 O2  H2O        70.00
    >>> feed = tmo.Stream('feed', H2O=200)
    >>> srn(feed.mol) # Call to run reaction on molar flow
    >>> feed.show() # Notice how 70% of water was converted to product
    Stream: feed
     phase: 'l', T: 298.15 K, P: 101325 Pa
     flow (kmol/hr): H2O  60
                     H2   140
                     O2   70
    
    """
    __slots__ = ('_chemicals', '_X_index', '_stoichiometry', '_X')
    def __init__(self, reaction, reactant, X, chemicals=None):
        chemicals = self._load_chemicals(chemicals)
        if reaction:            
            self._stoichiometry = prs.get_stoichiometric_array(reaction, chemicals)
            self._X_index = self._chemicals.index(reactant)
            self._stoichiometry *= 1/-(self._stoichiometry[self._X_index])
            self._X = X #: [float] Reactant conversion
        else:
            self._stoichiometry = np.zeros(chemicals.size)
            self._X_index = self._chemicals.index(reactant)
        self._X = X #: [float] Reactant conversion
    
    def copy(self):
        """Return copy of Reaction object."""
        copy = self.__new__(type(self))
        copy._stoichiometry = self._stoichiometry
        copy._X_index = self._X_index
        copy._chemicals = self._chemicals
        copy._X = self._X
        return copy
    
    def __add__(self, rxn):
        assert self._chemicals is rxn._chemicals, 'working chemicals must be the same to add reactions'
        assert self.reactant is rxn.reactant, 'reactants must be the same to add reactions'
        new = self.copy()
        stoichiometry = self._stoichiometry*self.X + rxn._stoichiometry*rxn.X
        new._stoichiometry = stoichiometry/-(stoichiometry[new._X_index])
        new.X = self.X + rxn.X
        return new
    
    def __iadd__(self, rxn):
        assert self._chemicals is rxn._chemicals, 'working chemicals must be the same to add reactions'
        assert self.reactant is rxn.reactant, 'reactants must be the same to add reactions'
        stoichiometry = self._stoichiometry*self.X + rxn._stoichiometry*rxn.X
        self._stoichiometry = stoichiometry/-(stoichiometry[self._X_index])
        self.X = self.X + rxn.X
        return self
    
    def __mul__(self, num):
        new = self.copy()
        new.X *= float(num)
        return new
    
    def __rmul__(self, num):
        return self.__mul__(num)
    
    def __imul__(self, num):
        self.X *= num
        return self
    
    def __div__(self, num):
        self.__mul__(self, 1/num)
    
    def __rdiv__(self, num):
        self.__mul__(self, 1/num)    
    
    def __idiv__(self, num):
        return self.__imul__(self, 1/num) 
    
    def __neg__(self):
        new = self.copy()
        new.X *= -1.
        return new
    
    def __sub__(self, rxn):
        assert self._chemicals is rxn._chemicals, 'working chemicals must be the same to add reactions'
        assert self.reactant is rxn.reactant, 'reactants must be the same to add reactions'
        new = self.copy()
        stoichiometry = self._stoichiometry*self.X - rxn._stoichiometry*rxn.X
        new._stoichiometry = stoichiometry/-(stoichiometry[new._X_index])
        new.X = self.X - rxn.X
        return new
    
    def __isub__(self, rxn):
        assert self._chemicals is rxn._chemicals, 'working chemicals must be the same to add reactions'
        assert self.reactant is rxn.reactant, 'reactants must be the same to add reactions'
        stoichiometry = self._stoichiometry*self.X + rxn._stoichiometry*rxn.X
        self._stoichiometry = stoichiometry/-(stoichiometry[self._X_index])
        self.X = self.X - rxn.X
        return 
    
    def __call__(self, material):
        material += material[self._X_index]*self.X*self._stoichiometry
    
    @property
    def X(self):
        """[float] Reaction converion as a fraction."""
        return self._X
    @X.setter
    def X(self, X):
        self._X = X
    
    @property
    def stoichiometry(self):
        """[array] Stoichiometry coefficients."""
        return self._stoichiometry
    @property
    def reactant(self):
        """[str] Reactant associated to conversion."""
        return self._chemicals.IDs[self._X_index]
    
    def __repr__(self):
        stoichiometry = prs.get_stoichiometric_string(self._stoichiometry, self._chemicals)
        return f"{type(self).__name__}('{stoichiometry}', reactant='{self.reactant}', X={self.X:.3g})"
    
    def show(self):
        outs = f"{type(self).__name__}:"
        rxn = prs.get_stoichiometric_string(self._stoichiometry, self._chemicals)
        cmp = self.reactant
        lrxn = len(rxn)
        lcmp = len(cmp)
        maxrxnlen = max([13, lrxn]) + 2
        maxcmplen = max([8, lcmp]) + 2
        X = self.X
        outs += "\n stoichiometry" + " "*(maxrxnlen - 13) + "reactant" + " "*(maxcmplen - 8) + '  X[%]'
        rxn_spaces = " "*(maxrxnlen - lrxn)
        cmp_spaces = " "*(maxcmplen - lcmp)
        outs += f"\n {rxn}{rxn_spaces}{cmp}{cmp_spaces}{X*100: >6.2f}"
        print(outs)
    _ipython_display_ = show


class ReactionItem(Reaction):
    """Create a ReactionItem object from the a ReactionSet and reaction index.
    
    Parameters
    ----------
    rxnset : ReactionSet
    index : int
        Index of reaction.
        
    """
    __slots__ = ('_index')
    def __init__(self, rxnset, index):
        self._stoichiometry = rxnset._stoichiometry[index]
        self._X = rxnset._X
        self._chemicals = rxnset._chemicals
        self._X_index = rxnset._X_index[index]
        self._index = index
    
    def copy(self):
        """Return copy of Reaction object."""
        new = super().copy()
        new._index = self._index
        return new
    
    @property
    def X(self):
        """[float] Reaction converion as a fraction."""
        return self._X[self._index]
    @X.setter
    def X(self, X):
        self._X[self._index] = X
        

class ReactionSet:
    """Create a ReactionSet that contains all reactions and conversions as an array.
    
    Parameters
    ----------
    reactions : Iterable[Reaction]
    
    """
    __slots__ = ('_stoichiometry', '_X', '_X_index', '_chemicals')
    def __init__(self, reactions):
        assert len({i.chemicals for i in reactions})==1, 'all reactions must have the same chemicals'
        self._stoichiometry = np.array([i._stoichiometry for i in reactions])
        self._X = np.array([i.X for i in reactions])
        self._X_index = np.array([i._X_index for i in reactions])
        self._chemicals = reactions[0].chemicals
    
    def __getitem__(self, index):
        stoichiometry = self._stoichiometry[index]
        if len(stoichiometry.shape) == 1:
            return ReactionItem(self, index)
        else:
            rxnset = self.__new__(type(self))
            rxnset._stoichiometry = stoichiometry
            rxnset._X = self._X[index]
            rxnset._X_index = self._X_index[index]
            rxnset._chemicals = self._chemicals
            return rxnset
    
    @property
    def X(self):
        """[1d array] Reaction converions."""
        return self._X
    
    @property
    def chemicals(self):
        """[Chemicals] Chemicals corresponing to each entry in the stoichiometry array."""
        return self._chemicals
    @property
    def stoichiometry(self):
        """[2d array] Stoichiometry coefficients."""
        return self._stoichiometry
    
    @property
    def reactants(self):
        """tuple[str] Reactants associated to conversion."""
        IDs = self._chemicals.IDs
        return tuple([IDs[i] for i in self._X_index])
    
    def __repr__(self):
        return f"<{type(self).__name__}: {', '.join(set(self.reactants))}>"
    
    def show(self):
        outs = f"{type(self).__name__}:"
        chemicals = self._chemicals
        rxns = [prs.get_stoichiometric_string(i, chemicals) for i in self._stoichiometry]
        maxrxnlen = max([13, *[len(i) for i in rxns]]) + 2
        cmps = self.reactants
        maxcmplen = max([8, *[len(i) for i in cmps]]) + 2
        Xs = self.X
        N = len(Xs)
        maxnumspace = max(len(str(N)) + 1, 5)
        outs += f"\nindex" + " "*(max(2, maxnumspace-3)) + "stoichiometry" + " "*(maxrxnlen - 13) + "reactant" + " "*(maxcmplen - 8) + '  X[%]'
        for N, rxn, cmp, X in zip(range(N), rxns, cmps, Xs):
            rxn_spaces = " "*(maxrxnlen - len(rxn))
            cmp_spaces = " "*(maxcmplen - len(cmp))
            num = str(N)
            numspace = (maxnumspace - len(num)) * " "
            outs += f"\n[{N}]{numspace}{rxn}{rxn_spaces}{cmp}{cmp_spaces}{X*100: >6.2f}"
        print(outs)
    _ipython_display_ = show
        
class ParallelReaction(ReactionSet):
    """
    Create a ParallelReaction object from Reaction objects. When called, 
    it returns the change in material due to all parallel reactions.
    
    Parameters
    ----------
    reactions : Iterable[Reaction]
    
    
    """
    __slots__ = ()
    
    def __call__(self, material):
        material += material[self._X_index]*self.X @ self._stoichiometry

    @property
    def X_net(self):
        """[ChemicalIndexer] Net reaction conversion of reactants."""
        X_net = {}
        for i, j in zip(self.reactants, self.X):
            if i in X_net:
                X_net[i] += j
            else:
                X_net[i] = j
        chemicals = self.chemicals
        data = chemicals.kwarray(X_net)
        return ChemicalIndexer.from_data(data, NoPhase, chemicals, False)

class SeriesReaction(ReactionSet):
    """Create a ParallelReaction object from Reaction objects. When called, it returns the change in material due to all reactions in series.
    
    Parameters
    ----------
    reactions : Iterable[Reaction]
    
    
    """
    __slots__ = ()
    
    def __call__(self, material):
        for i, j, k in zip(self._X_index, self.X, self._stoichiometry):
            material += material[i]*j*k

    @property
    def X_net(self):
        """[ChemicalIndexer] Net reaction conversion of reactants."""
        X_net = {}
        for i, j in zip(self.reactants, self.X):
            if i in X_net:
                X_net[i] += (1 - X_net[i]) * j
            else:
                X_net[i] = j
        chemicals = self.chemicals
        data = chemicals.kwarray(X_net)
        return ChemicalIndexer.from_data(data, NoPhase, chemicals, False)

# Short-hand conventions
# Rxn = Reaction
# RxnI = ReactionItem
# RxnS = ReactionSet
# PRxn = ParallelReaction
# SRxn = SeriesReaction

