#!/usr/bin/env python3
"""Sort values"""


def flip_switch(df):
    """Sort values"""
    df = df.sort_values(by="Timestamp", ascending=False)
    df = df.T
    return df
