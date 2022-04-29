# deal with find the funding amount of each element code in each topic
# Author: Jiahui Wang


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the "clean_ele" file and preprocesing the data
ele_df = pd.read_csv("/Users/jiahuiwang/Desktop/2022Spring/Capstone/clean_ele.csv")
ele_df["ele_code"] = ele_df["ele_code"].astype(str)

# create the result dataframe for calculate the each element code investigate amount
amount_result = pd.DataFrame(columns=['topic', 'ele_code', 'ele_amount'])

# loop each topic
i = 1
while(i < 26):
    # initialize dictionary [key(ele_code) : value(freq)]
    amount_dic = {}
    # loop each documents
    topic_df = ele_df.loc[ele_df["topic"] == i]
    for j in range(len(topic_df)):
        elecode = tpoic_df.values[j][4].strip()
        if(elecode != "NAN"):
            amount = topic_df.values[j][3]
            gamma = topic_df.values[j][2]
            if("," in elecode == False):
                if(amount_dic.has_key(elecode) == False):
                    amount_dic[elecode] = round(amount * gamma, 2)
                else:
                    amount_dic[elecode] += amount * gamma
                    amount_dic[elecode] = round(dic[elecode],2)
            else:
                ele_list = elecode.split(',')
                n = len(ele_list)
                for e in ele_lst:
                    if (dic.has_key(e) == False):
                        dic[e] = round((amount * gamma) / n, 2)
                    else:
                        dic[e] += (amount * gamma) / n
                        dic[e] = round(dic[e], 2)
                        
    # sort the amount dic
    amount_dic = sorted(amount_dic.items(), key = lambda item:item[1])

    # put temp dic to result df
    for t in amount_dic:
        amount_result = amount_result.append({'topic':i, 'ele_code':t[0], 'ele_amount':t[1]}, ignore_index=True)
        
    i += 1
    
# write the dataframe to csv file
amount_result.to_csv("ele_amount.csv")

