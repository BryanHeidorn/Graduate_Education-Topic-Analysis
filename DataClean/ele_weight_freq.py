# deal with find the weight frequency of element code in each topic
import pandas as pd
import numpy as np

# Step 1:
# read in the clean_ele.csv file
data = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/DataClean/clean_ele.csv")

# Step 2:
# # create the result df for counting frequency, which contains "topic", "ele_code", and "weight_freq"
w_freq_result = pd.DataFrame(columns=['topic', 'ele_code', 'weight_freq'])

# loop each topic
i = 1
while(i < 26):
    # initialize dictionary [key(ele_code) : value(freq)]
    dic = {}
    # loop each documents
    temp_df = data.loc[data["topic"] == i]
    for j in range(len(temp_df)):
        elecode = temp_df.values[j][4].strip()
        gamma = temp_df.values[j][2]
        if(elecode != "NAN"):
            if("," in elecode == False):
                if(dic.has_key(elecode) == False):
                    dic[elecode] = gamma
                else:
                    dic[elecode] += gamma
                    # dic[elecode] += gamma value
            else:
                lst = []
                for ele in elecode.split(','):
                    lst.append(ele.strip())
                curr_gamma = gamma/len(lst)
                for e in lst:
                    if (dic.has_key(e) == False):
                        dic[e] = curr_gamma
                    else:
                        dic[e] += curr_gamma
    # sort the dic depend on value
    dic = sorted(dic.items(), key = lambda item:item[1])

    # put temp dic to result df
    for t in dic:
        w_freq_result = w_freq_result.append({'topic':i, 'ele_code':t[0], 'weight_freq': round(t[1], 2)}, ignore_index=True)

    i += 1

w_freq_result.to_csv("ele_weight_freq.csv")


