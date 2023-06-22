let carroItems = []; // Array para almacenar los productos del carrito

function addToCart(productName, price) {
  // Verificar si el producto ya está en el carrito
  const existingItem = carroItems.find(item => item.name === productName);

  if (existingItem) {
    // Si el producto ya está en el carrito, solo se actualiza la cantidad y el total
    existingItem.quantity += 1;
    existingItem.total += price;
  } else {
    // Si el producto no está en el carrito, se agrega como un nuevo elemento
    carroItems.push({ name: productName, price: price, quantity: 1, total: price });
  }

  // Actualizar la interfaz de usuario
  updateCartUI();
}

function removeFromCart(productName) {
  // Buscar el producto en el carrito
  const itemIndex = carroItems.findIndex(item => item.name === productName);

  if (itemIndex !== -1) {
    // Si se encuentra el producto, se elimina del carrito
    const removedItem = carroItems.splice(itemIndex, 1)[0];

    // Actualizar la interfaz de usuario
    updateCartUI();

    // Realizar cualquier otra acción necesaria al eliminar el producto
    console.log('Producto eliminado:', removedItem);
  }
}

function updateCartUI() {
  const cartItemsElement = document.getElementById('carro-items');
  const cartTotalElement = document.getElementById('carro-total');

  // Limpiar la lista de elementos del carrito
  cartItemsElement.innerHTML = '';

  // Recorrer los productos del carrito y agregarlos a la lista
  carroItems.forEach(item => {
    const listItem = document.createElement('li');
    listItem.textContent = `${item.name} (x${item.quantity}) - $${item.total}`;

    // Agregar un botón para eliminar el producto
    const removeButton = document.createElement('button');
    removeButton.textContent = 'Eliminar';
    removeButton.addEventListener('click', () => removeFromCart(item.name));

    listItem.appendChild(removeButton);
    cartItemsElement.appendChild(listItem);
  });

  // Calcular el total del carrito
  const cartTotal = carroItems.reduce((total, item) => total + item.total, 0);
  cartTotalElement.textContent = '$' + cartTotal;
}