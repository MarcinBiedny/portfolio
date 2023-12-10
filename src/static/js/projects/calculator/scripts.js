function appendDigit(digit) {
    document.getElementById('calculatorDisplay').value += digit;
}

function appendOperator(operator) {
    document.getElementById('calculatorDisplay').value += operator;
}

function clearDisplay() {
    document.getElementById('calculatorDisplay').value = '';
}

function calculateResult() {
    try {
        document.getElementById('calculatorDisplay').value = eval(document.getElementById('calculatorDisplay').value)
    } catch (e) {
        document.getElementById('calculatorDisplay').value = 'Error'
    }
}
