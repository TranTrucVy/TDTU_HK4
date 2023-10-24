package com.SpringCommerce.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.SpringCommerce.mapper.ProductMapper;
import com.SpringCommerce.models.MyPageInfo;
import com.SpringCommerce.models.Product;
import com.SpringCommerce.models.ProductExample;


@Service
public class ProductService implements ProductServiceInterface {

	@Autowired
	ProductMapper productMapper;
	
	@Override
	public List<Product> getAllProducts() {
		// TODO Auto-generated method stub
		return productMapper.selectByExample(new ProductExample());
	}

	@Override
	public Map<String, Object> getProductById(int id) {
		return productMapper.getProductById(id);
	}

	@Override
	public void createProduct(Product product) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void updateProduct(int id, Product product) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void deleteProduct(int id) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public int getCountProduct() {
		// TODO Auto-generated method stub
		return productMapper.getCountProduct();
	}
	@Override
	public List<Map<String, Object>> getProductPage(MyPageInfo myPageInfo) {
		return productMapper.getProductPage(myPageInfo);
	}
	
	

}
