const url = 'https://swapi-api.hbtn.io/api/films/6/?format=json';
const listCharacters = document.querySelector('#list_characters');

fetch(url)
  .then(response => response.json())
  .then(data => {
    const characters = data.characters;
    characters.forEach(characterUrl => {
      fetch(characterUrl)
        .then(res => res.json())
        .then(characterData => {
          const li = document.createElement('li');
          li.textContent = characterData.name;
          listCharacters.appendChild(li);
        });
    });
  });
