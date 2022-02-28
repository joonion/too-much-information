library(datasauRus)

str(datasaurus_dozen)
head(datasaurus_dozen)

library(dplyr)

datasaurus_dozen %>%
    group_by(dataset) %>%
    summarise(
        mean_x = mean(x),
        mean_y = mean(y),
        sd_x = sd(x),
        sd_y = sd(y),
        cor_xy = cor(x, y)
    )

library(ggplot2)

ggplot(datasaurus_dozen, 
       aes(x = x, y = y, color = dataset)) +
    geom_point() +
    theme_void() +
    theme(legend.position = "none") +
    facet_wrap(~dataset, ncol = 5)

dino <- subset(datasaurus_dozen, dataset=="dino")
ggplot(dino, aes(x = x, y = y)) +
    geom_point(color = "blue", size=8) +
    theme_void() +
    theme(legend.position = "none")


library(datasauRus)
str(datasaurus_dozen)

mydf <- datasaurus_dozen
table(mydf$dataset)

dino <- subset(mydf, dataset == "dino")
plot(dino$x, dino$y)

data <- split(mydf, f = mydf$dataset)
with(data$dino, plot(x, y))

aggregate(x ~ dataset, mydf, mean)
aggregate(y ~ dataset, mydf, mean)
aggregate(y ~ dataset, mydf, mean)
