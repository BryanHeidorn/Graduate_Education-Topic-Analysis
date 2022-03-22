import pandas as pd
import numpy as np

# read SimilarTitles.csv (dataset contains data records which dist<25)
similar_data = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/data/Edu/SimilarAbstract.csv")

# export the x1 value list and x2 value list
x1 = similar_data["X1"]
x2 = similar_data["X2"]

# A 2D list contains similar project grants as each group. (e.g. [[grant1], [grant2]...])
result = []

# add each grant group to 2D list "result"
for i in range(0, len(similar_data)):
    x1_v = x1[i]
    x2_v = x2[i]
    if(len(result) == 0):
        result.append([x1_v, x2_v])
    else:
        j = 0
        while(j < len(result)):
            if (x1_v in result[j] and x2_v not in result[j]):
                result[j].append(x2_v)
                break
            elif(x2_v in result[j] and x1_v not in result[j]):
                result[j].append(x1_v)
                break
            j += 1

        if j == len(result):
            result.append([x1_v, x2_v])

# merge similar groups (e.g. [1,2,3] & [2,3,4] should merge to [1,2,3,4])
i = 0
while(i < len(result)):
    j = i + 1
    temp = result[i]
    while(j < len(result)):
        if list(set(result[i]).intersection(set(result[j]))) != []:
            result[i] = list(set(result[i]+ result[j]))
            result.remove(result[j])
        j += 1
    if result[i] == temp:
        i += 1

# "dupli_idx" contains all duplicated AwardNumber
dupli_idx = []
for n in result:
    dupli_idx += n


# read Edu.csv
edu_data = pd.read_csv("/Users/zhengsongyi/Desktop/2022Spring/Capstone/data/Edu.csv")

# create dictionary [key(group[0]) : value(sum(total group's grants amount))]
dic = {}
for i in range(0, len(result)):
    valid_line = edu_data.loc[edu_data["AwardNumber"].isin(result[i])]
    amount = sum(valid_line["AwardedAmountToDate"].array)
    dic[result[i][0]] = amount

# write new dataset and then export
# First, make a dataframe for get all data records which AwardNumbers not in duplicated list ("dupli_idx")
non_dupli_df = edu_data.loc[~(edu_data["AwardNumber"].isin(dupli_idx) ) ]
# Secondly, make a dataframe for get all first AwardNumber of each grant group (e.g. [1,2,3], only keep 1)
dupli_df = edu_data.loc[(edu_data["AwardNumber"].isin(dic.keys()) )]
# change the each award amount to total amount
for n in dic.keys():
    dupli_df.loc[dupli_df["AwardNumber"] == n, "AwardedAmountToDate"] = dic.get(n)

# Additional: get the dataset "duplicated_df" contains all duplicated records
# duplicated_df = edu_data.loc[(edu_data["AwardNumber"].isin(dupli_idx) ) ]
# duplicated_df.to_csv("duplicated.csv")


# join two data frames as a new clean dataset "clean_edu.csv"
clean_edu = non_dupli_df.append(dupli_df)
# export the clean_edu data frame as .csv file
clean_edu.to_csv("clean_edu.csv")



















