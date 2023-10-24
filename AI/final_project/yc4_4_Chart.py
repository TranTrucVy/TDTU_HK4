from keras.datasets import mnist
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import numpy as np

(train_X, train_y), (test_X, test_y) = mnist.load_data()

class Decision:
    model = DecisionTreeClassifier()
    model.fit(train_X.reshape(train_X.shape[0], -1), train_y)

    train_pred = model.predict(train_X.reshape(train_X.shape[0], -1))
    test_pred = model.predict(test_X.reshape(test_X.shape[0], -1))

    train_acc = accuracy_score(train_y, train_pred)
    test_acc = accuracy_score(test_y, test_pred)

class KNN:
    train_X = train_X.reshape(-1, 784)
    test_X = test_X.reshape(-1, 784)

    k = 3
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(train_X, train_y)

    train_acc = model.score(train_X, train_y)
    test_acc = model.score(test_X, test_y)

class Bayes:
    X_train = np.reshape(train_X, (train_X.shape[0], -1)) / 255.0
    X_test = np.reshape(test_X, (test_X.shape[0], -1)) / 255.0

    model = GaussianNB()
    model.fit(X_train, train_y)

    train_acc = model.score(X_train, train_y)
    test_acc = model.score(X_test, test_y)

dec = Decision()
bay = Bayes()
k = KNN()
# accuracy data for Decision Tree, Naïve Bayes classifier and KNN
train_acc = [dec.train_acc, bay.train_acc, k.train_acc]
test_acc = [dec.test_acc, bay.test_acc, k.test_acc]
 
# set height of bar
train_bars = train_acc
test_bars = test_acc

# # Set position of bar on X axis
# r1 = np.arange(len(train_bars))
# r2 = [x + barWidth for x in r1]
 
# # Make the plot
# plt.bar(r1, train_bars, color='#7f6d5f', width=barWidth, edgecolor='white', label='Training Accuracy')
# plt.bar(r2, test_bars, color='#557f2d', width=barWidth, edgecolor='white', label='Testing Accuracy')

# for i, v in enumerate(train_acc):
#     plt.text(i - 0.1, v + 1, str(v) + '%', color='black', fontweight='bold')
 
# for i, v in enumerate(test_acc):
#     plt.text(i + 0.15, v + 1, str(v) + '%', color='black', fontweight='bold')

# # Add xticks on the middle of the group bars
# plt.xlabel('Model', fontweight='bold')
# plt.xticks([r + barWidth for r in range(len(train_bars))], ['Decision Tree', 'Naïve Bayes', 'KNN'])
# # Create legend & Show graphic
# plt.legend()
# plt.show()
# ------------------------------------------------------------------
models = ['Decision Tree', 'Naive Bayes', 'KNN']
 
# Thiết lập độ rộng của các cột trong biểu đồ
barWidth = 0.25
 
# Vẽ biểu đồ cột
plt.bar(models, train_acc, width=barWidth, label='Training Accuracy')
plt.bar([model + barWidth for model in range(len(models))], test_acc, width=barWidth, label='Test Accuracy')

# Hiển thị phần trăm chính xác trên mỗi cột
for i, v in enumerate(train_acc):
    plt.text(i-0.1, v+0.01, "{:.2f}%".format(v*100), color='black', fontweight='bold', fontsize=5)
 
for i, v in enumerate(test_acc):
    plt.text(i+0.15, v+0.01, "{:.2f}%".format(v*100), color='black', fontweight='bold', fontsize=5)
 
# Thiết lập tiêu đề, nhãn trục và chú thích cho biểu đồ
plt.xlabel('Models')
plt.ylabel('Accuracy (%)')
plt.title('Accuracy of Different Models on Training and Test Sets')
plt.xticks([r + barWidth for r in range(len(models))], models)
plt.legend()
 
# Hiển thị biểu đồ
plt.show()