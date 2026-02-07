const addItemTrigger = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItemTrigger.addEventListener('click', () => {
  const newListItem = document.createElement('li');
  newListItem.textContent = 'Item';
  myList.appendChild(newListItem);
});
