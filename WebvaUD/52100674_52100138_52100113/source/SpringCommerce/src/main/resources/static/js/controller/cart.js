const renderCartItems = () => {
	const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
	let contentHTML = `
		<div
			class="d-flex justify-content-between align-items-center mb-5">
			<h1 class="fw-bold mb-0 text-black">Shopping Cart</h1>
			<h6 class="mb-0 text-muted">${JSON.parse(localStorage.getItem("cartItems")).length <= 0 ? "0 item" : JSON.parse(localStorage.getItem("cartItems")).length + " items"}</h6>
		</div>
		<hr class="my-4">
	`
	cartItems.map((prod) => {
		contentHTML += `
			<div
				class="row mb-4 d-flex justify-content-between align-items-center">
				<div class="col-md-2 col-lg-2 col-xl-2">
					<img
						src="${prod.image}"
						class="img-fluid rounded-3" alt="Cotton T-shirt">
				</div>
				<div class="col-md-3 col-lg-3 col-xl-3">
					<h6 class="text-muted">${prod.name}</h6>
					<h6 class="text-black mb-0">${prod.description}</h6>
					<p class="text-muted mb-0">Size: ${prod.size}</p>
				</div>
				<div class="col-md-3 col-lg-3 col-xl-2 d-flex">
					
					<input id="form1" min="0" name="quantity" value="${prod.quantity}"
						type="number" class="form-control form-control-sm" onchange="updateCartItemQuantity(${prod.id}, ${prod.size}, this.value)"/>

					
				</div>
				<div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
					<h6 class="mb-0">$ ${Number(prod.price)}</h6>
				</div>
				<div class="col-md-1 col-lg-1 col-xl-1 text-end">
					<a class="text-muted" onclick="removeProduct(${prod.id}, ${prod.size})"><i class="fas fa-times"></i></a>
				</div>
			</div>

			<hr class="my-4">
		`
	})
	contentHTML += `
		<div class="pt-5 d-flex justify-content-between">
			<h6 class="mb-0">
				<a href="/" class="text-body" style="cursor: pointer"><i
					class="fas fa-long-arrow-alt-left me-2"></i>Back to shop</a>
			</h6>
			<a href="/checkout"><button class="btn btn-dark text-white">Check Out</button></a>
		</div>
	`
	document.querySelector(".cart-row").innerHTML = contentHTML;
}

renderCartItems()

const removeProduct = (id, size) => {
	let cartItems = JSON.parse(localStorage.getItem('cartItems'));
	let newCartItems = cartItems.filter((item) => {
		return !(Number(item.id) === Number(id) && item.size === size);
	})
	localStorage.setItem('cartItems', JSON.stringify(newCartItems));
	document.querySelector(".small-quantity").innerText = "(" + JSON.parse(localStorage.getItem("cartItems")).length + ")"
	// re-render the cart items list after removing the product
	renderCartItems();
}

document.querySelector(".small-quantity").innerText = "(" + JSON.parse(localStorage.getItem("cartItems")).length + ")"


const updateCartItemQuantity = (id, size, quantity) => {
	let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

	// Tìm sản phẩm trong giỏ hàng
	let updatedCartItem = cartItems.find(item => Number(item.id) === Number(id) && Number(item.size) === Number(size));
	console.log(quantity)
	console.log(updatedCartItem)
	if (updatedCartItem) {
		// Nếu sản phẩm được tìm thấy, cập nhật số lượng sản phẩm
		updatedCartItem.quantity = Number(quantity);

		// Cập nhật lại localStorage
		localStorage.setItem('cartItems', JSON.stringify(cartItems));

		// Render lại giỏ hàng
		renderCartItems();
	}
}



