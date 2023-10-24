package com.SpringCommerce.Controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

public class InvoiceController {
	
	@GetMapping
	public ModelAndView invoice() {
		return new ModelAndView("pages/order-success");
	}
	
}
