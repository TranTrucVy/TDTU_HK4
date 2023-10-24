let quantity = 0;

/**
 * renderRelateProduct(): render UI
 * @param {*} arrListRelate: input an array which contains data of cards to display on screen
*/

console.log(localStorage.getItem("cartItems"))

console.log(document.getElementById('number').value);
// Function to check limit quantity on button click
document.querySelector('#increase').onclick = () => {
	console.log('increase')
	let value = parseInt(document.getElementById('number').value, 10);
	value = isNaN(value) ? 0 : value;
	if (value < 1000) {
		value += 1;
		document.getElementById('number').value = value;
	}
	else if (value === 1000) {
		value += 0;
	}
	else {
		alert('Quá số lượng tồn kho !!!')
	}
};
document.querySelector('#decrease').onclick = () => {
	let value = parseInt(document.getElementById('number').value, 10);
	value = isNaN(value) ? 0 : value;
	value < 1 ? value = 1 : '';
	value--;
	document.getElementById('number').value = value;
};


// Lưu giá trị size được chọn vào biến selectedSize
let selectedSize;
const sizeButtons = document.querySelectorAll('#size button');
sizeButtons.forEach((button) => {
	button.addEventListener('click', function() {
		selectedSize = button.getAttribute('data-size-id');
		console.log('Selected size:', selectedSize);
	});
});


// Lấy nút "Add to cart"
const addToCartBtn = document.getElementById('btn-cart');

// Thêm sự kiện click vào nút "Add to cart"
addToCartBtn.addEventListener('click', function() {
	
	if (!selectedSize) {
		alert('Please select a size.');
		return;
	}
	
	// Lấy thông tin sản phẩm từ các thuộc tính dữ liệu
	const productId = addToCartBtn.getAttribute('data-id');
	const productName = addToCartBtn.getAttribute('data-name');
	const productDesc = addToCartBtn.getAttribute('data-shortdes');
	const productPrice = addToCartBtn.getAttribute('data-price');
	const productImage = addToCartBtn.getAttribute('data-image');
	const productQuantity = document.getElementById('number').value;

	// Lưu thông tin sản phẩm vào localStorage
	const product = {
		id: productId,
		name: productName,
		description: productDesc,
		price: parseInt(productPrice),
		image: productImage,
		size: parseInt(selectedSize),
		quantity: parseInt(productQuantity)
	};

	console.log(product)

	// Get existing cart items from local storage or set an empty array
	let cartItems = JSON.parse(localStorage.getItem("cartItems")) || [];

	// Check if the product is already in the cart
	const existingProduct = cartItems.find((item) => item.id === product.id && item.size === product.size);

	if (existingProduct) {
		// If the product is already in the cart with the same size, update its quantity
		existingProduct.quantity += parseInt(product.quantity);
		console.log(existingProduct)
	} else {
		// Otherwise, add the product to the cart
		cartItems.push(product);
	}
	document.querySelector(".small-quantity").innerText = "(" + cartItems.length + ")"

	// Save the updated cart items to local storage
	localStorage.setItem("cartItems", JSON.stringify(cartItems));

	// Thông báo thành công
	alert('Product added to cart!');
});

document.querySelector(".small-quantity").innerText = "(" + JSON.parse(localStorage.getItem("cartItems")).length + ")"








