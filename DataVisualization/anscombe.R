str(anscombe)
anscombe

apply(anscombe[, 1:4], 2, mean)
apply(anscombe[, 1:4], 2, var)
apply(anscombe[, 1:4], 2, sd)

apply(anscombe[, 5:8], 2, mean)
apply(anscombe[, 5:8], 2, var)
apply(anscombe[, 5:8], 2, sd)

with(anscombe, cor(x1, y1))
with(anscombe, cor(x2, y2))
with(anscombe, cor(x3, y3))
with(anscombe, cor(x4, y4))
     
lm.1 <- lm(y1~x1, data=anscombe)
lm.2 <- lm(y2~x2, data=anscombe)
lm.3 <- lm(y3~x3, data=anscombe)
lm.4 <- lm(y4~x4, data=anscombe)
coef(lm.1)
coef(lm.2)
coef(lm.3)
coef(lm.4)

library(ggplot2)

p1 <- ggplot(anscombe) +
    geom_point(aes(x=x1, y=y1),
               color="orange", size=3) +
    geom_abline(intercept=coef(lm.1)[1],
                slope=coef(lm.1)[2],
                color="blue") 

p2 <- ggplot(anscombe) +
    geom_point(aes(x=x2, y=y2),
               color="orange", size=3) +
    geom_abline(intercept=coef(lm.2)[1],
                slope=coef(lm.2)[2],
                color="blue") 

p3 <- ggplot(anscombe) +
    geom_point(aes(x=x3, y=y3),
               color="orange", size=3) +
    geom_abline(intercept=coef(lm.3)[1],
                slope=coef(lm.3)[2],
                color="blue") 

p4 <- ggplot(anscombe) +
    geom_point(aes(x=x4, y=y4),
               color="orange", size=3) +
    geom_abline(intercept=coef(lm.4)[1],
                slope=coef(lm.4)[2],
                color="blue") 

library(gridExtra)
grid.arrange(grobs = list(p1, p2, p3, p4),
             ncol = 2,
             top = "Anscombe's Quartet")


