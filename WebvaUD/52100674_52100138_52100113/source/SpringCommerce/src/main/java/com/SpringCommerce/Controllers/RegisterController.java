package com.SpringCommerce.Controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class RegisterController {
	
	@GetMapping("/register")
	public ModelAndView register () {
		return new ModelAndView("pages/register");
	}
}
