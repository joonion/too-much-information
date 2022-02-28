#install.packages("datasauRus")
library(datasauRus)

str(datasaurus_dozen)
head(datasaurus_dozen, 3)
tail(datasaurus_dozen)
table(datasaurus_dozen$dataset)
datanames <- unique(datasaurus_dozen$dataset)

library(dplyr)
datasaurus_dozen %>%
    group_by(dataset) %>%
    summarize(mean(x), 
              mean(y), 
              sd(x), 
              sd(y), 
              cor(x,y))

library(ggplot2)
ggplot(datasaurus_dozen) +
    geom_point(aes(x=x, y=y, color=dataset)) +
    facet_wrap(~dataset, nrow=3)
