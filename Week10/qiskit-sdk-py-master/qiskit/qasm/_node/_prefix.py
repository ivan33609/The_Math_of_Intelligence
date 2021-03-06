# -*- coding: utf-8 -*-

# Copyright 2017 IBM RESEARCH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

"""
Node for an OPENQASM prefix expression.
"""
from ._node import Node
from ._nodeexception import NodeException


class Prefix(Node):
    """Node for an OPENQASM prefix expression.

    children[0] is a prefix string such as '-'.
    children[1] is an expression node.
    """

    def __init__(self, children):
        """Create the prefix node."""
        Node.__init__(self, 'prefix', children, None)

    def qasm(self, prec=15):
        """Return the corresponding OPENQASM string."""
        return self.children[0] + "(" + self.children[1].qasm(prec) + ")"

    def latex(self, prec=15, nested_scope=None):
        """Return the corresponding math mode latex string."""
        return self.children[0] + "(" + \
            self.children[1].latex(prec, nested_scope) + ")"

    def real(self, nested_scope=None):
        """Return the correspond floating point number."""
        operation = self.children[0]
        expr = self.children[1].real(nested_scope)
        if operation == '+':
            return expr
        elif operation == '-':
            return -expr
        else:
            raise NodeException("internal error: undefined prefix")
