function generateRandomNumber() {
    return Math.floor(Math.random() * 9000000) + 1000000;
}

const prefix = 86070204;
const generatedNumbers = new Set();

const imeiList = document.getElementById("imeiList");

for (let i = 0; i < 100; i++) {
    let randomNumber = generateRandomNumber();
    
    while (generatedNumbers.has(randomNumber)) {
        randomNumber = generateRandomNumber();
    }

    generatedNumbers.add(randomNumber);

    const imei = document.createElement("div");
    imei.textContent = prefix + randomNumber;
    imeiList.appendChild(imei);
}
