# Copyright (C) 2015-2017 by the RBniCS authors
#
# This file is part of RBniCS.
#
# RBniCS is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RBniCS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with RBniCS. If not, see <http://www.gnu.org/licenses/>.
#

from rbnics.utils.decorators import Extends, override, ReducedProblemDecoratorFor
from shape_parametrization.problems.pygem_decorated_problem import PyGeM

@ReducedProblemDecoratorFor(PyGeM)
def PyGeMDecoratedReducedProblem(ParametrizedReducedDifferentialProblem_DerivedClass):
    @Extends(ParametrizedReducedDifferentialProblem_DerivedClass, preserve_class_name=True)
    class PyGeMDecoratedReducedProblem_Class(ParametrizedReducedDifferentialProblem_DerivedClass):
    
        @override
        def __init__(self, truth_problem, **kwargs):
            # Call the standard initialization
            ParametrizedReducedDifferentialProblem_DerivedClass.__init__(self, truth_problem, **kwargs)
            
    # return value (a class) for the decorator
    return PyGeMDecoratedReducedProblem_Class
    