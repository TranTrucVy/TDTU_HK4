const renderCartCheckout = () => {
	let totalPrice = 0;
	const cartItems = JSON.parse(localStorage.getItem('cartItems'));
	let contentHTML = `
		<h4 class="d-flex justify-content-between">
			Cart <span class="price" style="color: black"> <i
				class="fa fa-shopping-cart"></i> <b>4</b>
			</span>
		</h4>
	`;

	cartItems.map((item) => {
		totalPrice += item.quantity * item.price
		contentHTML += `
			<p class="d-flex justify-content-between">
				<a class="text-dark fw-bolder">${item.name}</a> 
				
				<span class="size">Size: ${item.size}</span>
				
				<span class="quantity">x${item.quantity}</span>
				
				<span class="price">$${item.quantity * item.price}</span>
			</p>
		`
	})
	contentHTML += `
		<hr>
		<p class="d-flex justify-content-between">
			Total <span class="price fs-5" style="color: black"><b>$${totalPrice}</b></span>
		</p>
	`
	console.log(contentHTML)
	document.querySelector('.container.cart').innerHTML = contentHTML

}

renderCartCheckout();