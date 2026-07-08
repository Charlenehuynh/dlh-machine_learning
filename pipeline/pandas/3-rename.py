#!/usr/bin/env python3
"""Manipulate table using pandas"""

import pandas as pd


def rename(df):
    """Manipulate table using pandas"""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    df = df[["Datetime", "Close"]]
    return df
