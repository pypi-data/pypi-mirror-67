#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Shapelets.io
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


########################################################################################################################
# IMPORT
########################################################################################################################
import unittest
from khiva.linalg import *
from khiva.array import *
from khiva.library import set_backend, KHIVABackend


########################################################################################################################

class LinalgTest(unittest.TestCase):
    DELTA = 1e-6

    def setUp(self):
        set_backend(KHIVABackend.KHIVA_BACKEND_CPU)

    def test_lls(self):
        lls_result = lls(Array.from_numpy(np.array([[4, 3], [-1, -2]]), dtype.f32), Array.from_list([3, 1], dtype.f32))
        a = lls_result.to_numpy()
        self.assertAlmostEqual(a[0], 1, delta=self.DELTA)
        self.assertAlmostEqual(a[1], 1, delta=self.DELTA)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LinalgTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
