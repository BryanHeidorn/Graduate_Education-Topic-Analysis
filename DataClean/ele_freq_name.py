# draw element code frequency and name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1:
# read in the file "ele_freq.csv" [topic, ele_code, frequency]
ele_freq_df = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/DataClean/ele_freq.csv")
# read in the file "ele_name.csv"
ele_name_df = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/data/ele_name.csv")
# join two dfs
data = ele_freq_df.join(ele_name_df.set_index("ele_code"), on = "ele_code")
#data.to_csv("ele_name_freq.csv")


# Step 2:
# loop each topic and then draw the histograms
i = 1
while(i < 26):
    # loop each documents
    temp_df = data.loc[data["topic"] == i]
    plt.figure(figsize=(25,10))
    plt.barh(temp_df["name"], temp_df["freq"])
    plt.title("Element Code Frequency Histogram of Topic #" + str(i), fontsize = 16)
    plt.xlabel("frequency", fontweight = 'bold')
    plt.ylabel("element_code_name", fontweight = 'bold')
    figname = "freq" + str(i) + ".png"
    plt.savefig(figname)
    plt.show()
    i += 1
