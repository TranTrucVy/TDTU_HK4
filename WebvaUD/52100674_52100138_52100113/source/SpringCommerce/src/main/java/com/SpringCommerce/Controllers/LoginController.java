package com.SpringCommerce.Controllers;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

import com.SpringCommerce.config.AES;
import com.SpringCommerce.mapper.ProductMapper;
import com.SpringCommerce.models.MyPageInfo;
import com.SpringCommerce.service.ProductService;

@Controller
public class LoginController {
	@Autowired
	ProductService productService; 
	
	@GetMapping("/login")
	public ModelAndView login() {
		ModelAndView modelAndView = new ModelAndView("pages/login");
		Map<String, Object> products = productService.getProductById(1);
		System.out.println(products.toString());
//		System.out.println(AES.encrypt("jdbc:mysql://localhost:3307/spring_commerce", "Killa@1510"));
		return modelAndView;
	}
}
