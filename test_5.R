#相関係数
height <- c(175, 179, 162, 184, 170, 167)
weight <- c(75, 80, 60, 80, 66, 55)
cor(height, weight, method="pearson")

#無相関検定
cor.test(height, weight, method="pearson")
