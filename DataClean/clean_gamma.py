# filter the gamma value larger than 0.1
# Author: Jiahui Wang
import pandas as pd
import numpy as np

# read in file
data = pd.read_csv("/Users/jiahuiwang/Desktop/2022Spring/Capstone/top_documents.csv")

# create result data frame
result = pd.DataFrame()

# filter the gamma value larger than 0.1
i = 1
while(i < 26):
    # cnt = 0
    # separate temp df for each topic
    temp = data.loc[data["topic"] == i]
    for j in range(len(temp)):
        if temp.iloc[j,2] > 0.1:
            result = result.append(temp[j:j+1])

    i += 1


# write the data to csv file
result.to_csv("clean_gamma.csv")


