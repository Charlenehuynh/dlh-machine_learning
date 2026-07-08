#!/usr/bin/env python3
"""slicing table"""


def slice(df):
    """slicing table"""
    arr = df[["High", "Low", "Close", "Volume_(BTC)"]][::60]
    return arr
