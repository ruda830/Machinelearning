#相関係数
height <- c(175, 179, 162, 184, 170, 167)
weight <- c(75, 80, 60, 80, 66, 55)
cor(height, weight, method="pearson")

#無相関検定
cor.test(height, weight, method="pearson")

#t = 4.4471, df = 4, p-value = 0.01127  cor 0.9120128 
#tはt値、dfは自由度、p-valueはp値、cor相関係数