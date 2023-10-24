package com.SpringCommerce.Controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class ShoppingCartController {
	@GetMapping("/cart")
	public ModelAndView cart() {
		ModelAndView modelAndView = new ModelAndView("pages/cart");
		return modelAndView;
	}
}
