package com.SpringCommerce.Controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class ProfileController {
	
	@GetMapping("/profile")
	public ModelAndView profile() {
		return new ModelAndView("pages/profile");
	}
}
