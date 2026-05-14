// This function adds the clicked button's value to the screen
function appendToDisplay(value) {
  const display = document.getElementById('display');
  display.value += value;
}

// This function clears the screen when 'C' is pressed
function clearDisplay() {
  const display = document.getElementById('display');
  display.value = '';
}