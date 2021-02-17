#散布図
#説明変数[独立変数]xと目的変数[従属変数]y
#独立変数はあるシステムに対する入力(input)
#従属変数はシステムからの出力(output)

#散布図は回帰分析や2変数の数式モデルを求める数理モデル化につかえる
data(women)
plot(women) #height:xとweight:y

data(iris)
plot(iris[,1:4])

#petal.Lengthとpetal.Widthの相関がつよい