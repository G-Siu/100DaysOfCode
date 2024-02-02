const searchInput = document.getElementById("search-input");
const searchButton = document.getElementById("search-button");
const pokemonName = document.getElementById("pokemon-name");
const pokemonId = document.getElementById("pokemon-id");
const weightValue = document.getElementById("weight");
const heightValue = document.getElementById("height");
const sprite = document.querySelector(".sprite");
const typesValue = document.getElementById("types");
const hpValue = document.getElementById("hp");
const attackValue = document.getElementById("attack");
const defenseValue = document.getElementById("defense");
const specialAttackValue = document.getElementById("special-attack");
const specialDefenseValue = document.getElementById("special-defense");
const speedValue = document.getElementById("speed");

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

const getApi = async (pokemon) => {
    try {
        const res = await fetch(`https://pokeapi-proxy.freecodecamp.rocks/api/pokemon/${pokemon}`);
        if (!res.ok) {
            alert("Pokémon not found");
            throw new Error("Couldn't fetch data");
            
        }
        const data = await res.json();
        display(data);
    }
    catch(err) {
        console.error("General error:", err);
    }
}

const display = (obj) => {
    typesValue.innerHTML = ""
    const { _experience, height, id, name, _order, sprites, stats, types, weight } = obj;
    pokemonName.textContent = `${name}`;
    pokemonId.textContent = `#${id}`;
    weightValue.textContent = `Weight: ${weight}`;
    heightValue.textContent = `Height: ${height}`;
    sprite.innerHTML = `<img id="sprite" src="${sprites["front_default"]}" alt="${name} front default sprite">`
    for (let i = 0; i < types.length; i++) {
        typesValue.innerHTML += `<span class="types ${types[i]["type"]["name"]}">${types[i]["type"]["name"]}</span>`
    }
    const [ hp, attack, defense, specialAttack, specialDefense, speed ] = stats;
    hpValue.textContent = hp["base_stat"];
    attackValue.textContent = attack["base_stat"];
    defenseValue.textContent = defense["base_stat"];
    specialAttackValue.textContent = specialAttack["base_stat"];
    specialDefenseValue.textContent = specialDefense["base_stat"];
    speedValue.textContent = speed["base_stat"];
}


const checkInput = () => {
    getApi(formatInput());
}

searchButton.addEventListener("click", checkInput);