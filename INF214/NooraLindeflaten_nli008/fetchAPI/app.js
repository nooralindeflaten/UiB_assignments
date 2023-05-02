const calculatorForm = document.querySelector("#newtoncalc-form");

const resultContainer = document.querySelector(".result-container");
const resultExpression = document.querySelector("#result-expression");
const result = document.querySelector("#result");

const urlvar = "https://newton.now.sh/api/v2/simplify/"; // we want to simplify



calculatorForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(calculatorForm);
    const expressioninput = formData.get("expression");
    const exprlist = expressioninput.split(";");
    for(let i = 0; i < exprlist.length; i++) {
        expression = encodeURIComponent(exprlist[i])
        const url = `${urlvar}${expression}`;
        let response = await fetch(url).then((response) => {
            return response.json();
        });
        if (response.result.includes("?")) {
            calculatorForm.reset();
        }
        else {
            resultExpression.innerHTML = "Expression: " + expression;
            result.innerHTML = "Result: " + response.result;
            break;
        }
    }
});



