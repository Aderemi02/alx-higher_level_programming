#!/usr/bin/python3
"""functions that multiplies two matrices"""
import numpy as num


def lazy_matrix_mul(m_a, m_b):
    """using NumPy to multiply two matrices"""

    return (num.matmul(m_a, m_b))
