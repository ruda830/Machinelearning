data(USArrests)
#distで相互の変数間の距離を求める
USArrests.d <- dist(USArrests)
USArrests.hc <- hclust(USArrests.d)
plot(USArrests.hc)
