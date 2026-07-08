#!/usr/bin/env python3
"""sort values"""


def high(df):
    """sort values"""
    df = df.sort_values(by="High", ascending=False)
    return df
