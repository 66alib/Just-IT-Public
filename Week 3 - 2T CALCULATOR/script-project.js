
const sixtyToOne = document.getElementById("sixtyToOne");
const fiftyToOne = document.getElementById("fiftyToOne");
const fourtyToOne = document.getElementById("fourtyToOne");
const thirtyToOne = document.getElementById("thirtyToOne");
const twentyfiveToOne = document.getElementById("twentyfiveToOne");
const twentyL = document.getElementById("twentyL");
const fifteenL = document.getElementById("fifteenL");
const tenL = document.getElementById("tenL");
const fiveL = document.getElementById("fiveL");
const userInputSubmit = document.getElementById("userInputSubmit");
const fuelOilRatio = document.getElementById("fuelOilRatio");
const jerryCanSize = document.getElementById("jerryCanSize");
const amountOfOilNeeded = document.getElementById("amountOfOilNeeded");
const predefInputReset = document.getElementById("predefInputReset");




userInputSubmit.addEventListener("click", (e) => {
    e.preventDefault ()
    userInputRatio = fuelOilRatio.value     /* this line is not necessary as the variable.value can be directly injected into the formula */
    userInputFuel = jerryCanSize.value      /* this line is not necessary as the variable.value can be directly injected into the formula */ 
    let calcOilNeeded = 1 / userInputRatio * 1000 * userInputFuel;
    amountOfOilNeeded.innerText = `You need ${calcOilNeeded} ml of oil.`;
});

// function resetAll() {
//     getElementById("amountOfOilNeeded").innerText = "";
// };

// predefInputReset.addEventListener("click", () => {
//     getElementById("amountOfOilNeeded"). = "";
// });

const ratioFuelCustom = document.getElementById("ratioFuelCustom");
const partsOilCustom = document.getElementById("partsOilCustom");
const customCalcResult = document.getElementById("customCalcResult");
const userInputSubmitCustom = document.getElementById("userInputSubmitCustom");
const userInputResetCustom = document.getElementById("userInputResetCustom");
const FuelInputCustom = document.getElementById("FuelInputCustom");
const customAmountOilNeeded = document.getElementById("customAmountOilNeeded");

userInputSubmitCustom.addEventListener("click", (e) => {
    e.preventDefault ()
    let customCalcOilNeeded = 1 / ratioFuelCustom.value * 1000 * FuelInputCustom.value;
customAmountOilNeeded.innerText = `You need ${customCalcOilNeeded} ml of oil.`;
});

