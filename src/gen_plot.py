import matplotlib.pyplot as plt
import numpy as np

def gen_nb_plot(votes_1d_normalized, votes_2d_normalized, votes_3d_normalized, n1, n2, n3, title, filename):

    y_lim_max_1d = .35
    y_lim_max_2d = .35
    y_lim_max_3d = .35

    x1 = np.arange(1,10)
    x23 = np.arange(0,10)

    NB_probs1 = np.zeros(9)
    for i, d in enumerate(range(1,10)):
        NB_probs1[i] = np.log10((d+1)/d)

    def calc_nb(N):
        probs = np.zeros(10)
        for d in range(0,10):
            for k in range(10**(N-2), 10**(N-1)-1):
                probs[d] += np.log10(1 + (1/(10*k + d)))
        return probs

    NB_probs2 = calc_nb(2)
    NB_probs3 = calc_nb(3)

    plt.rcParams["font.family"] = "Helvetica"

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10,5))
    fig.suptitle(title, fontname="Arial", fontsize=12, fontweight='bold')

    for i in range(3):
        ax[i].set_xlabel('$d$')
        ax[i].set_ylabel('$P(d)$')

    if (n1 != 0):
        ax[0].set_title("1D, $n$="+str(n1), fontsize=11)
        ax[0].set_xticks(x1)
        ax[0].bar(x1, list(votes_1d_normalized.values()), align='center', color='orange', width=0.5)
        ax[0].plot(x1, NB_probs1, color='blue', marker='o')
        ax[0].set_ylim(0, y_lim_max_1d)

    if (n2 != 0):
        ax[1].set_title("2D, $n$="+str(n2), fontsize=11)
        ax[1].set_xticks(x23)
        ax[1].bar(x23, list(votes_2d_normalized.values()), align='center', color='orange', width=0.5, label='NB (empirical)')
        ax[1].plot(x23, NB_probs2, color='blue', marker='o', label='NB (theory)')
        ax[1].set_ylim(0, y_lim_max_2d)

    if (n3 != 0):
        ax[2].set_title("3D, $n$="+str(n3), fontsize=11)
        ax[2].set_xticks(x23)
        ax[2].bar(x23, list(votes_3d_normalized.values()), align='center', color='orange', width=0.5)
        ax[2].plot(x23, NB_probs3, color='blue', marker='o')
        ax[2].set_ylim(0, y_lim_max_3d)

    fig.subplots_adjust(bottom=0.2, wspace=0.33)
    ax[1].legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), fancybox=False, shadow=False, ncol=3)

    plt.savefig(filename, dpi=300)
