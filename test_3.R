#ポアソン分布
#発現頻度の低い事象はポアソン分布に従う
#平均と分散が等しい(発生回数λが少ないため、グラフがとんがってる。)

#確率質量関数
par(ann=F)
plot(1:50, dpois(1:50, lambda = 1), type="l", ylim=c(0,0.4), xlim=c(0, 25))

par(new=T)
plot(1:50, dpois(1:50, lambda = 4), type="l", ylim=c(0,0.4), xlim=c(0, 25))

par(new=T)
plot(1:50, dpois(1:50, lambda = 10), type="l", ylim=c(0,0.4), xlim=c(0, 25))

