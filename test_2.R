#t検定

#血糖値データ
x <- c(97.8, 93.5, 121.1, 102.2, 107.1, 105.4, 98.7, 92.8)
y <- c(148.1, 141.2, 158.5, 151.3, 165.4, 156.6, 194.9, 168.198)

summary(x)
summary(y)

#正規性の検定
ks.test(x, "pnorm", mean = mean(x), sd=sd(x)) #-> p-value=0.9309 正規分布
ks.test(y, "pnorm", mean = mean(y), sd=sd(y))

#