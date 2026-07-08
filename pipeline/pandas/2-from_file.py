#!/usr/bin/env python3
"""Wrote function loads data from a file"""

import pandas as pd


def from_file(filename, delimiter):
    """Wrote function loads data from a file"""
    return pd.read_csv(filename, sep=delimiter)
