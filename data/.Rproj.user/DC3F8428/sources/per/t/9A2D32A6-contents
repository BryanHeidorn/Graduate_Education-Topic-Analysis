# combine all 4 years data
library(tidyverse)
data18 <- read.csv("EDU-SD/Edu_18.csv")
data19 <- read.csv("EDU-SD/Edu_19.csv")
data20 <- read.csv("EDU-SD/Edu_20.csv")
data21 <- read.csv("EDU-SD/Edu_21.csv")
myData <- rbind(data18, data19, data20, data21)
write.csv(myData, "All_Edu_DataSD.csv", row.names = FALSE)

# compare
result <- as.data.frame(table(myData$AwardNumber))

write.csv(result, "Level_SD.csv", row.names = FALSE)