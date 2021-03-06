##分類問題を解く

'''
用意したデータを原点から近い/遠いで2つのクラスに分け、
さらに学習データとテストデータの計4種類に分割する。

近い/遠いの両方の学習テーマで学習し、テストデータで分類期の性能を見ます。
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

#-----------------------------------------------------

#クラスの閾値、原点からの半径
CLASS_RADIUS = 0.6

#近い/遠いでクラス分け。近いとTrue,遠いとFalse
labels =( data_x**2 + data_vy**2 ) < CLASS_RADIUS**2

#学習データとテストデータに分割
label_train = labels[idx_train]
label_test = labels[idx_test]

##グラフ描画

#近い、遠いクラス、学習、テストの4種類の散布図を重ねる

plt.scatter(x_train[label_train], y_train[label_train],
            c='black', s=30, marker='*', label='near train')
plt.scatter(x_train[label_train != True], y_train[label_train != True],
            c='black', s=30, marker='+', label='far train')

plt.scatter(x_test[label_test], y_test[label_test],
            c='black', s=30, marker='^', label='near test')
plt.scatter(x_test[label_test != True], y_test[label_test != True],
            c='black', s=30, marker='x', label='far test')

#-----------------------------------------------------

#元の線を表示
plt.plot(data_x, data_ty, linestyle=':', label='non noise curve')

#分離円
circle = plt.Circle((0, 0), CLASS_RADIUS, alpha=0.1, label='near area')
ax = plt.gca()
ax.add_patch(circle)


#x軸/y軸の範囲を指定
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

#凡例の表示位置を指定
plt.legend(bbox_to_anchor=(0.7, 1), loc='upper left', borderaxespad=0)

#グラフを表示
plt.show()

#-----------------------------------------------------

##学習
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score

data_train = np.c_[x_train, y_train]
data_test = np.c_[x_test, y_test]

# SVMの分類期を作製、学習
classifier = svm.SVC(gamma=1)
classifier.fit(data_train, label_train.reshape(-1))

#Testデータで評価
pred_test = classifier.predict(data_test)

#Accuracを表示
print('accuracy_score:\n', accuracy_score(label_test.reshape(-1), pred_test))

#混同行列を表示
print('Confusion matrix:\n', confusion_matrix(label_test.reshape(-1), pred_test))