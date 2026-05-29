from scipy.stats import ttest_ind

def run_ttest(group_a, group_b):

    stat, p_value = ttest_ind(
        group_a,
        group_b,
        nan_policy='omit'
    )

    return p_value