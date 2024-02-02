const searchInput = document.getElementById("search-input");
const searchButton = document.getElementById("search-button");
const pokemonName = document.getElementById("pokemon-name");
const pokemonId = document.getElementById("pokemon-id");
const weight = document.getElementById("weight");
const height = document.getElementById("height");
const sprite = document.getElementsByClassName("sprite");
const types = document.getElementById("types");

let pokemonCheck = [];

const formatInput = () => {
    const regex = /\s?[a-zA-Z0-9]+(?:♀|♂)?/g;
    if (!regex.test(searchInput.value)) {
        alert("Invalid input");
        return false;
    }
    let regexInput = searchInput.value.match(regex).join("").toLowerCase().split(" ").join("-");
    
    if (regexInput.slice(-1) === "♂") {
        regexInput = regexInput.replace("♂", "-♂");
    } else if (regexInput.slice(-1) === "♀") {
        regexInput = regexInput.replace("♀", "-♀")
    }
    return regexInput;
}

const getApi = (pokemon) => {
    fetch(`https://pokeapi-proxy.freecodecamp.rocks/api/pokemon/${pokemon}`)
    .then((res) => res.json())
    .then((list) => {
        display(list);
    })
    .catch((err) => {
        alert("Pokémon not found")
    })
}

const display = (obj) => {
    const { _experience, height, id, name, _order, sprites, stats, types, weight } = obj;
    spriteFront = sprites["front_default"]
    sprite.innerHTML += `<img id="sprite" src="${spriteFront}" alt="${name} front default sprite">`
    // console.log(obj)
    // console.log(sprites)
    // console.log(stats)
    // console.log(types)
}


const checkInput = () => {
    getApi(formatInput());
}

searchButton.addEventListener("click", checkInput)

