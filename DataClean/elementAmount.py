# deal with find the funding amount of each element code in each topic
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read in the "clean_ele" file
ele_df = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/DataClean/clean_ele.csv")
ele_df["ele_code"] = ele_df["ele_code"].astype(str)

# create the result df for counting frequency, which contains "topic", "ele_code", and "ele_amount"
amount_result = pd.DataFrame(columns=['topic', 'ele_code', 'ele_amount'])

# loop each topic
i = 1
while(i < 26):
    # initialize dictionary [key(ele_code) : value(freq)]
    dic = {}
    # loop each documents
    temp_df = ele_df.loc[ele_df["topic"] == i]
    for j in range(len(temp_df)):
        elecode = temp_df.values[j][4].strip()
        if(elecode != "NAN"):
            amount = temp_df.values[j][3]
            gamma = temp_df.values[j][2]
            if("," in elecode == False):
                if(dic.has_key(elecode) == False):
                    dic[elecode] = round(amount * gamma, 2)
                else:
                    dic[elecode] += amount * gamma
                    dic[elecode] = round(dic[elecode],2)
            else:
                lst = []
                for ele in elecode.split(','):
                    lst.append(ele.strip())
                for e in lst:
                    if (dic.has_key(e) == False):
                        dic[e] = round((amount * gamma) / len(lst), 2)
                    else:
                        dic[e] += (amount * gamma) / len(lst)
                        dic[e] = round(dic[e], 2)
    # sort the dic depend on value
    dic = sorted(dic.items(), key = lambda item:item[1])
    ele_lst = []
    amount_lst = []
    # put temp dic to result df
    for t in dic:
        amount_result = amount_result.append({'topic':i, 'ele_code':t[0], 'ele_amount':t[1]}, ignore_index=True)
        ele_lst.append(t[0])
        amount_lst.append(t[1])
    # draw funding amount histogram
    plt.barh(ele_lst, amount_lst)
    plt.title("Element Code Funding Amount Histogram of Topic #" + str(i), fontsize = 16)
    plt.xlabel("funding amount", fontweight = 'bold')
    plt.ylabel("element_code", fontweight = 'bold')
    plt.xticks(rotation = 10)
    figname = "fundAmount" + str(i) + ".png"
    plt.savefig(figname)
    plt.show()
    i += 1

amount_result.to_csv("ele_amount.csv")

