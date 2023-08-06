#
# Copyright (C). 2015 Satoru SATOH <ssato at redhat.com>
# License: MIT
#
# pylint: disable=missing-docstring, protected-access
from __future__ import absolute_import

import unittest

import anytemplate.engine as TT
import anytemplate.engines.strtemplate as strtemplate


class Test(unittest.TestCase):

    def test_10_find_by_filename(self):
        strtemplate.Engine._file_extensions.append("t")
        clss = TT.find_by_filename("foo.t")
        self.assertTrue(strtemplate.Engine in clss)
        strtemplate.Engine._file_extensions.remove("t")

    def test_20_find_by_name__found(self):
        self.assertEqual(TT.find_by_name("string.Template"),
                         strtemplate.Engine)

    def test_20_find_by_name__not_found(self):
        self.assertTrue(TT.find_by_name("not_existing_engine") is None)

# vim:sw=4:ts=4:et:
