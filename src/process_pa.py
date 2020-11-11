# note: code is for the three csv files for PA

import pandas as pd
import numpy as np
import gen_plot
import util

state="PA"
year=2020
cities = ["allegheny", "chester", "philadelphia"]
candidates = ["Biden", "Trump"]
vote_class = ["Election", "Absentee", "Total"]      # Election and Absentee not available for Philadelphia, Chester

# change values for col, city, cand, v_class
col=3           # Allegheny, Trump, col = 5: Election, 6: Absentee, 7: Total
                #            Biden, col = 2: Election, 3: Absentee, 4: Total
                # Philadelphia, Chester, Trump, col = 3: total
                #                        Biden, col = 2: total

city=2          # index cities, 0: Allegheny, 1: Chester, 2: Philadelphia
cand=1          # index candidates, 0: Biden, 1: Trump
v_class=2       # index vote_class, 0: Election, 1: Absentee, 2: Total

# comment/un-comment the following
#dir_data = '../data/pa/pa_allegheny_2020_11_09_01_28_PM.csv'
dir_data = '../data/pa/pa_philadelphia_2020_11_10_04_04_PM.csv'
#dir_data = '../data/pa/pa_chester_2020_11_06_08_19_PM.csv'


# no need to change the remaining
if (city==0):
    rows_to_skip=[0,1,2]
else:
    rows_to_skip=[0,1,2,3,4,5,6]
csv_data = pd.read_csv(dir_data, skiprows=rows_to_skip, header=None)
csv_data.drop(csv_data.tail(1).index, inplace=True)     # drop total line in sheet

votes = csv_data.iloc[:, col].to_numpy().astype(int)
# the remaining code can be adapted to plot other state's data by simply providing the array of votes

votes_str = list(map(str, votes))
votes_mean = round(np.mean(votes),2)
votes_stdev = round(np.std(votes),2)
votes_med = np.median(votes).astype(int)
votes_max = max(votes)
votes_min = min(votes)

title = candidates[cand] + " (" + str(year) + ") "+state+", " + cities[city].capitalize() + " - [" + vote_class[v_class] + "], vote counts: mean=" + str(votes_mean) + " stdev=" + str(votes_stdev) + " med=" + str(votes_med) + " max=" + str(votes_max) + " min=" + str(votes_min)
filename = candidates[cand] + "_" + state + "_" + cities[city].capitalize() + "_" + str(year) + "_" + vote_class[v_class] + "_NB.png"

v_1d, v_2d, v_3d, n1, n2, n3 = util.get_nb(votes_str)
gen_plot.gen_nb_plot(v_1d, v_2d, v_3d, n1, n2, n3, title, filename)
