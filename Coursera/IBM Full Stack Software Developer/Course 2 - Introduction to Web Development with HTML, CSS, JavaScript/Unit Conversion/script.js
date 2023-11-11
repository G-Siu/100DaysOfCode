function temperature() {
    // Convert Celsius to Fahrenheit
    // (CEL * 9/5) + 32
    var celsius = document.getElementById("celsius").value;
    var fahrenheit = (celsius * 9/5) + 32
    document.getElementById("fahrenheit").value = fahrenheit;
}

function weight() {
    // Convert kg to pounds
    // kg * 2.2
    var kg = document.getElementById("kg").value;
    var pounds = kg * 2.2
    document.getElementById("lbs").value = pounds
}

function distance() {
    // Convert km to miles
    // km * 0.62137
    var km = document.getElementById("km").value;
    var miles = km * 0.62137
    document.getElementById("miles").value = miles;
}
