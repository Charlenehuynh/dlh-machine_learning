#!/usr/bin/env python3

"""Modify a table"""


def array(df):
    """Modify a table"""
    arr = df[["High", "Close"]].tail(10).values
    return arr
