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
  }


document.getElementById('checkout-total').innerHTML ='R'+ totalPrice;
document.getElementById('checkout-totals').innerHTML ='R'+ totalPrice;




