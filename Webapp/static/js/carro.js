let carroItems = [];

// Al cargar la página, intenta recuperar los datos del carrito almacenados en localStorage
document.addEventListener('DOMContentLoaded', () => {
  const storedItems = localStorage.getItem('carroItems');
  if (storedItems) {
    carroItems = JSON.parse(storedItems);
    updateCartUI();
  }
});

function addToCart(idProducto, price, nombre) {
  const existingItem = carroItems.find(item => item.id === idProducto);

  if (existingItem) {
    existingItem.quantity += 1;
    existingItem.total += price;
  } else {
    carroItems.push({ id: idProducto, price: price, quantity: 1, total: price, nombre: nombre });
  }

  updateCartUI();
  saveCartData();
}

function removeFromCart(idProducto) {
  const itemIndex = carroItems.findIndex(item => item.id === idProducto);

  if (itemIndex !== -1) {
    const removedItem = carroItems.splice(itemIndex, 1)[0];

    updateCartUI();
    saveCartData();

    console.log('Producto eliminado:', removedItem);
  }
}

function updateCartUI() {
  const cartItemsElement = document.getElementById('carro-items');
  const cartTotalElement = document.getElementById('carro-total');

  cartItemsElement.innerHTML = '';

  carroItems.forEach(item => {
    const listItem = document.createElement('li');
    listItem.setAttribute('data-idproducto', item.id);
    listItem.setAttribute('data-cantidad', item.quantity);
    listItem.setAttribute('data-total', item.total);

    listItem.textContent = `${item.nombre} (x${item.quantity}) - $${item.total}`;

    const removeButton = document.createElement('button');
    removeButton.textContent = 'Eliminar';
    removeButton.addEventListener('click', () => removeFromCart(item.id));

    listItem.appendChild(removeButton);
    cartItemsElement.appendChild(listItem);
  });

  const cartTotal = carroItems.reduce((total, item) => total + item.total, 0);
  cartTotalElement.textContent = '$' + cartTotal;
}

// Guarda los datos del carrito en localStorage
function saveCartData() {
  localStorage.setItem('carroItems', JSON.stringify(carroItems));
}
