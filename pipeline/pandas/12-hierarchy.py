#!/usr/bin/env python3
"""Hierachy 12"""

import pandas as pd

index = __import__("10-index").index


def hierarchy(df1, df2):
    """Hierarchy 12"""
    df1 = index(df1)
    df2 = index(df2)
    df1 = df1[(df1.index >= 1417411980) & (df1.index <= 1417417980)]
    df2 = df2[(df2.index >= 1417411980) & (df2.index <= 1417417980)]
    new = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    new = new.swaplevel(0, 1)
    new = new.sort_index()
    return new
