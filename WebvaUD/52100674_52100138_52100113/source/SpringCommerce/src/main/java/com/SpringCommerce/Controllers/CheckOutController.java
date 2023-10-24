package com.SpringCommerce.Controllers;


import java.time.LocalDateTime;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;



@Controller
public class CheckOutController {
		
	@GetMapping("/checkout")
	public ModelAndView checkout() {
		ModelAndView modelAndView = new ModelAndView("pages/checkout");
		return modelAndView;
	}
	
	@PostMapping("/submit-order")
	public ModelAndView submitOrder(@RequestParam("address") String shippingAddress,
	                                 @RequestParam("product_ids") String productIds,
	                                 @RequestParam("total_price") double totalPrice) {
		
	    // Tạo đối tượng Order và lưu thông tin đơn hàng vào đối tượng này
//	    Order order = new Order();
//	    order.setCustomerId(1); // Sử dụng ID mặc định của khách hàng
//	    order.setShippingAddress(shippingAddress);
//	    order.setOrderDate(LocalDateTime.now());
//	    order.setTotalPrice(totalPrice);
//	    order.setItems(productIds);
//	    order.setStatus("Pending");

	    // Gọi hàm insertOrder() trong mapper để lưu thông tin đơn hàng vào database
//	    orderService.addOrder(order);

	    // Hiển thị thông báo xác nhận đặt hàng thành công cho người dùng
	    ModelAndView modelAndView = new ModelAndView("pages/order-success");
	    return modelAndView;
	}

}
