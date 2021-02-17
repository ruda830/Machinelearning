# 重回帰分析
#halcはヘモグロビンalc
bloods <- c(120,100,150,200)
weight <- c(65,70,80,82)
halc <- c(8,5,10,11)
dmdata <- data.frame(bloods,weight,halc)
dmdata

#相関行列
round(cor(dmdata),4)

#対散布図
pairs(dmdata)

#重回帰分析
(bloods.lm <- lm(bloods~.,data=dmdata))
# -> -86.657 + weight * 1.848 + halc * 10.821
#回帰分析における残差
#回帰分析の際に、推定されたモデルのパラメーターでは説明できない部分。
#観測値から推定値を引いたものとして算出される。


#作製したモデルの評価
summary(bloods.lm)
