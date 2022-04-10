# deal with find the frequency of element code in each topic
# Author: Songyi Zheng

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Find element code and amount value for each document
# "edu_df" is original all data
edu_df = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/data/clean_edu.csv")
new_edu_df = pd.DataFrame(edu_df, columns=["AwardNumber", "AwardedAmountToDate", "ProgramElementCode(s)"])
new_edu_df.columns=["document", "amount", "ele_code"]

# "top_doc_df" is all data after classify but before filter gamma
top_doc_df = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/data/Edu/ori_top_documents.csv")

# join two dfs and find element code and amount value
data = top_doc_df.join(new_edu_df.set_index("document"), on="document")
data.groupby('topic')

# "clean_ele" is completed file contain documents and ele_code info
data["ele_code"] = data["ele_code"].astype(str)
# Clean data: Upper all character in element code
# Data Error fix: element code "054Y" and "154Y" are same, so change "054Y" to "154Y"
for i in range(0, len(data)):
    curr_ele = data.values[i][4].upper()
    if("054Y" in curr_ele):
        curr_ele = curr_ele.replace("054Y", "154Y")
    data.loc[i, "ele_code"] = curr_ele
# store data
#data.to_csv("clean_ele.csv")

# Step 2:
# create the result df for counting frequency, which contains "topic", "ele_code", and "freq"
freq_result = pd.DataFrame(columns=['topic', 'ele_code', 'freq'])

# loop each topic
i = 1
while(i < 26):
    # initialize dictionary [key(ele_code) : value(freq)]
    dic = {}
    # loop each documents
    temp_df = data.loc[data["topic"] == i]
    for j in range(len(temp_df)):
        elecode = temp_df.values[j][4].strip()
        if(elecode != "NAN"):
            if("," in elecode == False):
                if(dic.has_key(elecode) == False):
                    dic[elecode] = 1
                else:
                    dic[elecode] += 1
            else:
                lst = []
                for ele in elecode.split(','):
                    lst.append(ele.strip())
                for e in lst:
                    if (dic.has_key(e) == False):
                        dic[e] = 1
                    else:
                        dic[e] += 1
    # sort the dic depend on value
    dic = sorted(dic.items(), key = lambda item:item[1])

    # put temp dic to result df
    for t in dic:
        freq_result = freq_result.append({'topic':i, 'ele_code':t[0], 'freq':t[1]}, ignore_index=True)

    i += 1

#freq_result.to_csv("ele_freq.csv")











