#!/usr/bin/env python3
"""read"""
import csv

with open("Popular_Baby_Names.csv") as f:
    data = csv.reader(f)
    print([row for row in data])
