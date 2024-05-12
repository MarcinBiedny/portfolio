async function sendForm() {
    const form = document.getElementById('passwordGeneratorForm');
    const url = new URL('api/v1/password/generate', window.location.origin);

    const params = {
        passwordLength: form.passwordLength.value,
        includeUppercase: form.includeUppercase.checked,
        includeNumbers: form.includeNumbers.checked,
        includeSpecialChars: form.includeSpecialChars.checked
    };
    url.search = new URLSearchParams(params).toString()

    try {
        const response = await fetch(url, {
            method: 'GET'
        });
        const result = await response.json()
        if (response.ok) {
            document.getElementById('result').textContent = 'Generate Password: ' + result.password;
        } else {
            let errorText = 'Error: '

            for (const key in result.errors) {
                errorText += result.errors[key] + ' ';
            }
            document.getElementById('result').textContent = errorText;
        }
    } catch (error) {
        console.log(error.message);
        document.getElementById('result').textContent = "Unexpected error ocurred...";
    }
}
