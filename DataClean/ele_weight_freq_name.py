# draw element code weight frequency and name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1:
# read in the file "ele_freq.csv" [topic, ele_code, frequency]
ele_w_freq_df = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/DataClean/ele_weight_freq.csv")
# read in the file "ele_name.csv"
ele_name_df = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/data/ele_name.csv")
# join two dfs
data = ele_w_freq_df.join(ele_name_df.set_index("ele_code"), on = "ele_code")
#data.to_csv("ele_name_weight_freq.csv")

# Step 2:
# read in the topic name file and make a list contains all topic names
topic_name_df = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/data/topic_names.csv")
topic_names_lst = topic_name_df["Name"].tolist()

# Step 3:
# loop each topic and then draw the histograms
i = 1
while(i < 26):
    # loop each documents
    temp_df = data.loc[data["topic"] == i]
    plt.figure(figsize=(25,10))
    plt.barh(temp_df["name"], temp_df["weight_freq"])
    plt.title("Element Code Weight Frequency Histogram of \n Topic #" + str(i) + ": " + topic_names_lst[i-1], fontsize = 16)
    plt.xlabel("weight frequency", fontweight = 'bold')
    plt.ylabel("element_code_name", fontweight = 'bold')
    figname = "weight_freq" + str(i) + ".png"
    plt.savefig(figname)
    plt.show()
    i += 1