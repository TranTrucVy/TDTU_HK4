package com.SpringCommerce.Controllers;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.SpringCommerce.service.ProductService;
import com.SpringCommerce.models.MyPageInfo;

@Controller
public class HomePageController {

	@Autowired
	private ProductService productService;

	@GetMapping("/")
	public ModelAndView index(@RequestParam(name = "page", defaultValue = "1") int pageNumber) {
		ModelAndView modelAndView = new ModelAndView("pages/index");
		int pageSize = 9;
		int totalItems = productService.getCountProduct();
		int totalPages = (int) Math.ceil((double) totalItems / pageSize);
		MyPageInfo myPageInfo = new MyPageInfo(pageNumber, pageSize, totalItems, totalPages);
		modelAndView.addObject("myPageInfo", myPageInfo);
		List<Map<String, Object>> products = productService.getProductPage(myPageInfo);
		modelAndView.addObject("products", products);
		return modelAndView;
	}
}
