# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Magdalena Zarowiecki"
__copyright__ = "Copyright 2023, Magdalena Zarowiecki"
__email__ = "magdalena.z@scilifelab.uu.se"
__license__ = "GPL-3"


def test_dummy():
    from dummy import dummy
    assert dummy() == 1
