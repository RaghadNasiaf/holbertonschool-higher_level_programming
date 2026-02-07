const updateHeaderTrigger = document.querySelector('#update_header');
const headerElement = document.querySelector('header');

updateHeaderTrigger.addEventListener('click', () => {
  headerElement.textContent = 'New Header!!!';
});
