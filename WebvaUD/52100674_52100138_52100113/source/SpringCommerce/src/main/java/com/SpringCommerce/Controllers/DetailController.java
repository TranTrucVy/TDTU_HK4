package com.SpringCommerce.Controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.SpringCommerce.service.ProductService;

import java.util.*;

@Controller
public class DetailController {

	@Autowired
	ProductService productService;

	@GetMapping("/detail")
	public ModelAndView showDetail(@RequestParam("id") int id) {
		Map<String, Object> product = productService.getProductById(2);		
	    String sizeString = (String) product.get("size");
	    String[] sizeArray = Arrays.copyOfRange(sizeString.split(","), 1, sizeString.split(",").length - 1);
	    for (String n : sizeArray) {
	    	System.out.println(n);
	    }
	    product.put("sizeArray", sizeArray);
		ModelAndView modelAndView = new ModelAndView("pages/detail");
	    modelAndView.addObject("product", product);
		return modelAndView;
	}
}
