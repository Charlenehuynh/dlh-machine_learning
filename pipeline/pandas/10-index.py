#!/usr/bin/env python3
"""Set index"""


def index(df):
    """Set index"""
    df = df.set_index("Timestamp")
    return df
