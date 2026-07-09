#!/usr/bin/env python3
"""Computes descriptive statistics for all columns"""


def analyze(df):
    """Drop and display statistic"""
    df = df.drop(columns=["Timestamp"])
    stats = df.describe()
    return stats
