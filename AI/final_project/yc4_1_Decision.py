# Nhập thư viện
from keras.datasets import mnist
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Tải tập dữ liệu MNIST
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# Sử dụng Decision Tree để học trên tập dữ liệu huấn luyện
# Do Decision Tree chỉ hoạt động được với dữ liệu 1 chiều, nên ta cần reshape lại dữ liệu huấn luyện thành 1 mảng 1 chiều.
model = DecisionTreeClassifier()
model.fit(train_X.reshape(train_X.shape[0], -1), train_y)

# Dự đoán kết quả trên tập huấn luyện và tập kiểm tra
train_pred = model.predict(train_X.reshape(train_X.shape[0], -1))
test_pred = model.predict(test_X.reshape(test_X.shape[0], -1))

# Tính độ chính xác trên tập huấn luyện và tập kiểm tra
train_acc = accuracy_score(train_y, train_pred)
test_acc = accuracy_score(test_y, test_pred)
print("Độ chính xác trên tập huấn luyện:", train_acc)
print("Độ chính xác trên tập kiểm tra:", test_acc)

# Bước 4: Lưu mô hình
with open('Decision_tree_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Bước 5: Load mô hình
with open('Decision_tree_model.pkl', 'rb') as f:
    model_loaded = pickle.load(f)

# Chạy inference (tính prediction) cho ít nhất 05 input samples
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
plt.show() #test - tab to normal

# Trực quan hoá cây quyết định
plt.figure(figsize=(20,10))
# ở đây chúng ta chỉ hiển thị cây quyết định với độ sâu tối đa là 3 để dễ quan sát.
# Nếu muốn hiển thị toàn bộ cây quyết định, ta chỉ cần bỏ tham số max_depth.
plot_tree(model, max_depth=3, fontsize=10, filled=True)
plt.title('CÂY TRỰC QUAN', color = 'r')
plt.show()