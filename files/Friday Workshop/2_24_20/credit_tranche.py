import random
from scipy.stats import norm
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import matplotlib.pyplot as plt

# Constants
EQUITY_INDEX_CUTOFFS = [0, 0.03, 0.07, 0.1, 0.15, 0.3, 1 ]
# Parameters
n = 1000 #names in credit index
rho = 0.1
num_sims = 1000
prob_default = 0.25
# For equity tranche 0-20%, mezzanine 20%-80%:
# tranche_cutoffs = [0, 0.2, 1 ]
tranche_cutoffs = EQUITY_INDEX_CUTOFFS
tranche_to_watch = 4 #1 is equity, 2 mezz, etc

# derived parameters
z_score_of_default = norm.ppf(prob_default)
beta = rho**0.5
alpha = (1 -rho)**0.5
max_defaults_protected = int(round(n * tranche_cutoffs[tranche_to_watch-1]))
wiped_out_defaults = int(round(n * tranche_cutoffs[tranche_to_watch]))
names_in_tranche = wiped_out_defaults - max_defaults_protected

# run simulation
trial_results = []
names_remaining_in_tranche =[]
for _ in range(num_sims):
    M = random.gauss(0, 1)
    K = 0 # number of names defaulting
    for _ in range(n):
        R_i = beta * M + alpha * random.gauss(0, 1)
        if R_i < z_score_of_default:
            K += 1
    trial_results.append(K)
    remaining_in_tranche = max(0, names_in_tranche - \
                           max(0, K - max_defaults_protected))
    names_remaining_in_tranche.append(remaining_in_tranche)

fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
binz = np.arange(-0.5, names_in_tranche + 1.5)
plt.hist(names_remaining_in_tranche, bins = binz)

plt.title('Names Left in Tranche ' + str(tranche_to_watch) + ' (' +
          str(num_sims) + ' trials)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()