#!/usr/bin/env python3

"""Drop Na"""


def prune(df):
    """Drop Na"""
    df = df.dropna(subset=["Close"])
    return df
