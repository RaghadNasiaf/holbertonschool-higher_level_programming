/* global fetch */

document.addEventListener('DOMContentLoaded', () => {
  const button = document.querySelector('#btn_translate');
  const select = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  const fetchHello = () => {
    const lang = select.value;

    if (!lang) {
      helloDiv.textContent = '';
      return;
    }

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${encodeURIComponent(lang)}`)
      .then((response) => response.json())
      .then((data) => {
        helloDiv.textContent = data.hello;
      })
      .catch(() => {
        helloDiv.textContent = '';
      });
  };

  button.addEventListener('click', fetchHello);
});
