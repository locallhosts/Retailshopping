 // Get the updated cart from local storage
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
    function increaseQuantity(index) {
      cart[index].quantity++;
      localStorage.setItem('cart', JSON.stringify(cart));
      window.location.reload();
    }

    function decreaseQuantity(index) {
      if (cart[index].quantity > 1) {
        cart[index].quantity--;
        localStorage.setItem('cart', JSON.stringify(cart));
        window.location.reload();
      }
    }

    let totalPrice = 0;
    for (let item_carts = 0; item_carts < cart.length; item_carts++) {
  let item__carts = cart[item_carts];
  let itemTotalPrice = item__carts.price * item__carts.quantity;
  totalPrice += itemTotalPrice;

  document.write(`
    <tr>
      <td><img src="${item__carts.image}" /></td>
      <td>${item__carts.name}</td>
      <td>${item__carts.price}</td>
      <td>${item__carts.description}</td>
      <td>
        <button class="btn-min" onclick="decreaseQuantity(${item_carts})"> - </button>
        ${item__carts.quantity}
        <button class="btn-increase" onclick="increaseQuantity(${item_carts})"> + </button>
      </td>
      <td>${itemTotalPrice}</td>
    </tr>
  `);
}

document.write(`

  <tr>
    <td colspan="5">Total Price</td>
    <td>${totalPrice}</td>
  </tr>


   <tr>

    <td colspan="6">
      <button class="btn btn-dark" onclick="myFunction()" >Continue to Checkout</button>


    </td>
  </tr>
`);



function myFunction() {
  location.replace("/checkout/")
}
