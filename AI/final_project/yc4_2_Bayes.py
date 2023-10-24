from keras.datasets import mnist
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Bước 1: Tải dữ liệu
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# Bước 2: Học dữ liệu
# Chuẩn hoá dữ liệu
X_train = np.reshape(train_X, (train_X.shape[0], -1)) / 255.0
X_test = np.reshape(test_X, (test_X.shape[0], -1)) / 255.0

# Sử dụng Gaussian Naive Bayes classifier
model = GaussianNB()
model.fit(X_train, train_y)

# Bước 3: Đánh giá độ chính xác
train_acc = model.score(X_train, train_y)
test_acc = model.score(X_test, test_y)

print("Độ chính xác trên tập huấn luyện: ", train_acc)
print("Độ chính xác trên tập kiểm tra: ", test_acc)

# Bước 4: Lưu mô hình
with open('Naive_bayes_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Bước 5: Load mô hình
with open('Naive_bayes_model.pkl', 'rb') as f:
    model_loaded = pickle.load(f)

# Bước 6: Chạy inference cho 5 input samples
n_samples = 5
sample_indices = np.random.choice(len(test_X), n_samples, replace=False)
figure, axes = plt.subplots(nrows=1, ncols=5, figsize=(10, 3))
for i, idx in enumerate(sample_indices):
    sample = test_X[idx]
    prediction = model_loaded.predict(sample.reshape(1, -1))
    print(f"Dự đoán {i+1}: {prediction}")
    axes[i].imshow(sample, cmap='gray')
    axes[i].set_title('Dự đoán: {}'.format(prediction[0]))
    # plt.imshow(sample, cmap='gray')
    # plt.title('Dự đoán: ' + str(prediction[0]))
plt.show()