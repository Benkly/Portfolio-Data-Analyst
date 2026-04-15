import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def cramers_v(feature1: pd.Series, feature2: pd.Series, df: pd.DataFrame, verbose: bool = False, v_only: bool = False):
  
  """A function which performs a chi-square test of independence and calculates Cramér's V for two categorical features.
  
  The function takes in two pandas Series representing the categorical features and the DataFrame they belong to. It returns a string containing the chi-square statistic, p-value, degrees of freedom, observed/expected frequencies and Cramér's V."""
  
  contingency_table = pd.crosstab(feature1, feature2)
  contingency_array = contingency_table.to_numpy()
  chisq_stat, pval, dof, expected = chi2_contingency(contingency_table)
  V = np.sqrt(chisq_stat / (df.shape[0] * (min(contingency_table.shape) - 1)))
  
  if v_only:
    return V
  
  if verbose:
    return f"""{feature1.name} vs {feature2.name}
  
    Chi-square statistic: {chisq_stat}
    p-value: {pval}
    Degrees of freedom: {dof}

    =======================================

    Observed frequencies:

    {contingency_array}

    =======================================

    Expected frequencies:
 
    {expected}

    =======================================

    Cramér's V: {V:.4f}"""
    
  else:
    return f"""{feature1.name} vs {feature2.name}
  
    Chi-square statistic: {chisq_stat}
    p-value: {pval}
    Degrees of freedom: {dof}
    Cramér's V: {V:.4f}
    """