import pandas as pd
import numpy as np

# read in file
data = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/data/Edu/top_documents.csv")

# create result data frame
result = pd.DataFrame()

# keep documents whose gamma > 0.1
i = 1
while(i < 26):
    # cnt = 0
    # separate temp df for each topic
    temp = data.loc[data["topic"] == i]
    for j in range(len(temp)):
        # cnt += temp.iloc[j,2]
        if temp.iloc[j,2] > 0.1:
            result = result.append(temp[j:j+1])

    # result = result.append(temp[:j+1])
    i += 1

print(result)

result.to_csv("clean_gamma.csv")


