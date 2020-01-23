from scipy.stats import ttest_ind
import numpy as np 

# calculate the significance
value, pvalue = ttest_ind(teamA_score, teamB_score, equal_var=False)
print(value, pvalue)
if pvalue > 0.05:
	print('Samples are likely drawn from the same distributions (fail to reject H0)')
else:
	print('Samples are likely drawn from different distributions (reject H0)')



