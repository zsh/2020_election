
def get_nb(votes):
    votes_1d_counts = {str(k): 0 for k in range(1,10)}
    votes_2d_counts = {str(k): 0 for k in range(0,10)}
    votes_3d_counts = {str(k): 0 for k in range(0,10)}
    for v in votes:
        if (v != '0'):
            if (len(v)==1):
                votes_1d_counts[v[0]] += 1
            elif (len(v)==2):
                votes_1d_counts[v[0]] += 1
                votes_2d_counts[v[1]] += 1
            elif (len(v)>=3):
                votes_1d_counts[v[0]] += 1
                votes_2d_counts[v[1]] += 1
                votes_3d_counts[v[2]] += 1

    total_1d = sum(votes_1d_counts.values())
    total_2d = sum(votes_2d_counts.values())
    total_3d = sum(votes_3d_counts.values())

    votes_1d_normalized = {}
    votes_2d_normalized = {}
    votes_3d_normalized = {}
    if (total_1d != 0):
        votes_1d_normalized = {k: v / total_1d for k, v in votes_1d_counts.items()}
    if (total_2d != 0):
        votes_2d_normalized = {k: v / total_2d for k, v in votes_2d_counts.items()}
    if (total_3d != 0):
        votes_3d_normalized = {k: v / total_3d for k, v in votes_3d_counts.items()}

    return votes_1d_normalized, votes_2d_normalized, votes_3d_normalized, total_1d, total_2d, total_3d
