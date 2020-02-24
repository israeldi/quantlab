import random
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 100
rho = .8
num_sims = 10000
beta = rho**0.5
alpha = (1 -rho)**0.5
prob_default = 0.1
tranche_cutoffs = [0, 0.2, 1]
# tranche_cutoffs = [0, 0.03, 0.07, 0.1, 0.15, 0.30, 1 ]
tranche_to_watch = 2 #(1 to num tranches)

# run simulation
z_default = norm.ppf(prob_default) # quantile function
max_defaults_protection = n * tranche_cutoffs[tranche_to_watch - 1]
wiped_out = n * tranche_cutoffs[tranche_to_watch ]
print (max_defaults_protection, wiped_out)

# histogram = [0] * (n+1)
trial_results = []
tranche_values = []
for _ in range(num_sims):
    M = random.gauss(0, 1)
    K = 0 # number of variables that are > 0
    for _ in range(n):
        R_i = beta * M + alpha * random.gauss(0, 1)
        if R_i < z_default:
            K += 1
    # histogram[K] += 1
    trial_results.append(K)
    tranch_value = wiped_out - min(wiped_out, max(0, K - max_defaults_protection))
    tranche_values.append(tranch_value)

# print(histogram)
print('Mean tranche value = ' + str(sum(tranche_values)/ num_sims))
plt.hist(tranche_values, bins=n+1, normed=0, align='mid')
plt.title('Distribution of Tranche Value in ' + str(num_sims) + ' trials')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()