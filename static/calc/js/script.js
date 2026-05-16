function appendToDisplay(value) {
  const display = document.getElementById('display');
  if (display.value === "Error" || display.value === "Invalid Input") {
    display.value = "";
  }
  display.value += value;
}

function clearDisplay() {
  document.getElementById('display').value = '';
}