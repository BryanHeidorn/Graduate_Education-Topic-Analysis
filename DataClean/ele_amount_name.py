# draw element code funding amount in each topic
# Author: Jiahui Wang


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read the file
ele_amount_df = pd.read_csv("/Users/jiahuiwang/Desktop/2022Spring/Capstone/ele_amount.csv")
ele_name_df = pd.read_csv("/Users/jiahuiwang/Desktop/2022Spring/Capstone/ele_name.csv")
topic_name_df = pd.read_csv("/Users/jiahuiwang/Desktop/2022Spring/Capstone/topic_names.csv")

# join the data
amount_data = ele_amount_df.join(ele_name_df.set_index("ele_code"), on = "ele_code")

# write the data to csv file
#amount_data.to_csv("ele_name_amount.csv")

# create the topic names list 
topic_names_lst = topic_name_df["Name"].tolist()


# draw the histograms
i = 1
while(i < 26):
    topic_df = amount_data.loc[amount_data["topic"] == i]
    plt.figure(figsize=(25,10))
    plt.barh(topic_df["name"], topic_df["ele_amount"])
    plt.title("Element Code Funding Amount Histogram of \n Topic #" + str(i) + ": " + topic_names_lst[i-1], fontsize = 16)
    plt.xlabel("funding amount", fontweight = 'bold')
    plt.ylabel("element_code_name", fontweight = 'bold')
    plt.xticks(rotation = 10)
    figname = "fundAmount" + str(i) + ".png"
    plt.savefig(figname)
    plt.show()
    i += 1
