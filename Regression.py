##回帰問題を解く

'''
1次元、2次元、9次元の多項式で回帰させる。

'''
import matplotlib.pyplot as plt
import numpy as np

##各種定義
#x軸の定義範囲
x_max = 1
x_min = -1

#y軸の定義範囲
y_max = 2
y_min = -1

#スケール、1単位に何点使うか
SCALE = 50

#train/testでTestデータの割合を指定
TEST_RATE = 0.3

##データ生成

data_x = np.arange(x_min, x_max, 1 / float(SCALE)).reshape(-1, 1) #reshape(-1, 1)は縦ベクトルにする用

data_ty = data_x ** 2
data_vy = data_ty + np.random.randn(len(data_ty), 1) * 0.5 #ノイズを乗せる

###分類、回帰問題用
#学習データ/テストデータに分割
def split_train_test(array):
    length = len(array) #テストデータの長さ
    n_train = int(length * (1-TEST_RATE))

    indices = list(range(length))
    np.random.shuffle(indices)
    idx_train = indices[:n_train]
    idx_test = indices[n_train:]

    return sorted(array[idx_train]), sorted(array[idx_test])

#インデックスリストを分割
indices = np.arange(len(data_x))
idx_train, idx_test = split_train_test(indices)

#学習データ
x_train = data_x[idx_train]
y_train = data_vy[idx_train]

#テストデータ
x_test = data_x[idx_test]
y_test = data_vy[idx_test]

#-----------------------------------

from sklearn import linear_model

##1次式で回帰させる場合
X1_TRAIN = x_train
X1_TEST = x_test

#学習
model = linear_model.LinearRegression()
model.fit(X1_TRAIN, y_train)

#グラフに描画
plt.plot(x_test, model.predict(X1_TEST), linestyle='-.', label='poly deg 1')

'''
##次は2次式で回帰させる場合
X2_TRAIN = np.c_[x_train**2, x_train]
X2_TEST = np.c_[x_test**2, x_test]

#学習
model = linear_model.LinearRegression()
model.fit(X2_TRAIN, y_train)

#グラフに描画
plt.plot(x_test, model.predict(X2_TEST), linestyle='--', label='poly deg 2')


##次は9次式で回帰させる場合
X9_TRAIN = np.c_[x_train**9, x_train**8, x_train**7, x_train**6, x_train**5, x_train**4,
                 x_train**3, x_train**2, x_train]
X9_TEST = np.c_[x_test**9, x_test**8, x_test**7, x_test**6, x_test**5, x_test**4,
                x_test**3, x_test**2, x_test]

#学習
model = linear_model.LinearRegression()
model.fit(X9_TRAIN, y_train)

#グラフに描画
plt.plot(x_test, model.predict(X9_TEST), linestyle='-', label='poly deg 9')

'''

##データの表示
plt.scatter(x_train, y_train, c='black', s=30, marker='v', label='train')
plt.scatter(x_test, y_test, c='black', s=30, marker='x', label='test')
#元の線を表示
plt.plot(data_x, data_ty, linestyle=':', label='non noise curve')

#x軸/y軸の範囲を指定
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#凡例の表示位置を指定
plt.legend(bbox_to_anchor=(0.7, 1), loc='upper left', borderaxespad=0)

#グラフを表示
plt.show()