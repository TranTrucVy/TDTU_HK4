package com.SpringCommerce.service;
import java.util.List;
import java.util.Map;
import com.SpringCommerce.models.MyPageInfo;
import com.SpringCommerce.models.Product;
public interface ProductServiceInterface {
    List<Product> getAllProducts();
    Map<String, Object> getProductById(int id);
    void createProduct(Product product);
    void updateProduct(int id, Product product);
    void deleteProduct(int id);
    int getCountProduct();
    List<Map<String, Object>> getProductPage(MyPageInfo myPageInfo);
}
