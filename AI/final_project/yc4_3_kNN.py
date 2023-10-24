from keras.datasets import mnist
from sklearn.neighbors import KNeighborsClassifier
import pickle
import matplotlib.pyplot as plt
import numpy as np

# Load dữ liệu
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# Reshape dữ liệu từ mảng 2 chiều 28x28 thành mảng 1 chiều 784
train_X = train_X.reshape(-1, 784)
test_X = test_X.reshape(-1, 784)

# Tạo mô hình KNN
k = 3
model = KNeighborsClassifier(n_neighbors=k)

# Học mô hình trên tập training
model.fit(train_X, train_y)

# Tính độ chính xác trên tập training và tập test
train_acc = model.score(train_X, train_y)
test_acc = model.score(test_X, test_y)
print('Độ chính xác trên tập huấn luyện:', train_acc)
print('Độ chính xác trên tập kiểm tra:', test_acc)

# Lưu mô hình vào file knn_model.pkl
with open('model_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Load mô hình từ file knn_model.pkl
with open('model_model.pkl', 'rb') as file:
    model_loaded = pickle.load(file)

# Chạy inference (tính prediction) cho ít nhất 05 input samples
n_samples = 5
sample_indices = np.random.choice(len(test_X), n_samples, replace=False)
# predictions = model_loaded.predict(test_X[:5])
# print('Dự đoán:', predictions)

# Hiển thị kết quả dự đoán bằng matplotlib
figure, axes = plt.subplots(nrows=1, ncols=5, figsize=(10, 3))
for i, idx in enumerate(sample_indices):
    sample = test_X[idx]
    prediction = model_loaded.predict(sample.reshape(1, -1))
    print(f"Dự đoán {i+1}: {prediction}")
    axes[i].imshow(sample.reshape(28, 28), cmap='gray')
    axes[i].set_title('Prediction: {}'.format(prediction[0]))
plt.show()