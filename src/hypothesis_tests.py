from scipy.stats import ttest_ind, chi2_contingency
import pandas as pd


def t_test(group1, group2):
    stat, p_value = ttest_ind(group1, group2, nan_policy='omit')
    return p_value


def chi_square_test(table):
    chi2, p, dof, expected = chi2_contingency(table)
    return p