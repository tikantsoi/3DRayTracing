#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:16:02 2020

@author: tikantsoi

Provide utility functions
"""

import numpy as np

def vec(vec):
    """
    Create a vector
    """
    return np.array(vec, dtype=float)

def norm(vec):
    """
    Normalisation
    """
    return np.linalg.norm(vec)

def hat(vec):
    """
    Return a unit vector in the direction
    """
    return vec / norm(vec)

