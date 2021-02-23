import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import ttest_ind
from statsmodels.stats.power import tt_ind_solve_power
import numpy as np


col = plt.rcParams['axes.prop_cycle'].by_key()['color']

mu1 = 0
mu2 = 0.5
sigma = 1
fig = plt.figure(figsize=[4, 4])
ax = fig.add_subplot(111)
x = np.linspace(mu1 - 3*sigma, mu1 + 3*sigma, 100)
plt.plot(x, mlab.normpdf(x, mu1, sigma))
x = np.linspace(mu2 - 3*sigma, mu2 + 3*sigma, 100)
plt.plot(x, mlab.normpdf(x, mu2, sigma))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', which='both', left='off',
                   right='off', labelleft='off')
plt.savefig('two_normal_distributions.png', format='png', dpi=300)

fig = plt.figure(figsize=[10, 10])
iterations = 10000
n = [5, 10, 25, 50, 100, 1000]
offset =[50, 100, 300, 500, 700, 800]
scale =[3, 3, 2.5, 2.5, 2.3, 2.2]
powers = []
for i, sample_size in enumerate(n):
    p_values = []
    sig_p_values = []
    effect_sizes = []
    for cur_iter in range(iterations):
        s1 = np.random.normal(mu1, sigma, sample_size)
        s2 = np.random.normal(mu2, sigma, sample_size)
        t_test = ttest_ind(s1, s2)
        p_values.append(t_test.pvalue)
        if t_test.pvalue <= 0.05:
            effect_sizes.append(s2.mean() - s1.mean())
            sig_p_values.append(t_test.pvalue)
    ax = fig.add_subplot(3,2,i+1)
    if sample_size == 1000:
        plt.bar(0, 10000, 0.1, alpha=0.5, color=col[2], edgecolor='black', linewidth=1.2)
    else:
        plt.hist(p_values, 20, normed=False, alpha=0.5, color=col[2], edgecolor='black', linewidth=1.2)
    plt.xlim([0, 1])
    p_values = np.array(p_values)
    sig = sum(p_values <= 0.05)
    plt.text(0.8, sig - offset[i], 'n = ' + str(sample_size))
    power = tt_ind_solve_power(effect_size=(mu1 - mu2) / sigma, nobs1=sample_size, alpha=0.05)
    powers.append(power)
    plt.text(0.71, sig - scale[i]*offset[i], 'power = ' + '{:2.0f}%'.format(power*100))
    if i in [4, 5]:
        plt.xlabel('p-values')
    if i in [0, 2, 4]:
        plt.ylabel('count (n)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
plt.savefig('t_tests.png', format='png', dpi=300)

fig = plt.figure(figsize=[8, 10])
iterations = 10000
n = [5, 10, 25, 50, 100, 1000]
for i, sample_size in enumerate(n):
    p_values = []
    sig_p_values = []
    effect_sizes = []
    for cur_iter in range(iterations):
        s1 = np.random.normal(mu1, sigma, sample_size)
        s2 = np.random.normal(mu2, sigma, sample_size)
        t_test = ttest_ind(s1, s2)
        p_values.append(t_test.pvalue)
        if t_test.pvalue <= 0.05:
            effect_sizes.append(s2.mean() - s1.mean())
            sig_p_values.append(t_test.pvalue)
    ax = fig.add_subplot(3,2,i+1)
    plt.plot(sig_p_values, effect_sizes, 'o', color='black', alpha=0.4)
    plt.plot([0, 0.05],[0.5, 0.5], '--', color='red')
#    if i in [0, 1]:
#        plt.plot([0, 0.05],[-0.5, -0.5], '--', color='red')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    effect_sizes = np.array(effect_sizes)
    above_effect = 100 * ((sum(effect_sizes >= (mu2 - mu1)) + sum(effect_sizes <= (mu1 - mu2)))
                          / len(effect_sizes))
    x = '{:2.1f}'.format(above_effect)
    p = '{:2.0f}%'.format(powers[i] * 100)
    plt.title('n = ' + str(sample_size) + ' ' + 'power = '
              + p + '  ' + x + '% with greater abs effect sizes',
              fontsize=8)
    if i in [4, 5]:
        plt.xlabel('p-values')
    if i in [0, 2, 4]:
        plt.ylabel('effect size')
plt.tight_layout(pad=2, h_pad=4)
plt.savefig('n' + str(sample_size) + '_sig_p_values.png', format='png', dpi=300)
