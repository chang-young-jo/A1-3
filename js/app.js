const analyzeBtn = document.getElementById("analyzeBtn");
const symptomInput = document.getElementById("symptom");
const conditionInput = document.getElementById("condition");
const resultBox = document.getElementById("result");

function showResult(message) {
    resultBox.innerHTML = "<h3>AI 분석 결과</h3>";

    const text = document.createElement("p");
    text.style.whiteSpace = "pre-line";
    text.textContent = message;

    resultBox.appendChild(text);
}

analyzeBtn.addEventListener("click", async () => {
    const symptom = symptomInput.value.trim();
    const condition = conditionInput.value.trim();

    if (!symptom) {
        showResult("분석할 이상 현상을 입력해주세요.");
        return;
    }

    analyzeBtn.disabled = true;
    analyzeBtn.textContent = "분석 중...";
    showResult("AI가 분석 중입니다. 잠시만 기다려주세요...");

    try {
        const response = await fetch("http://127.0.0.1:5000/api/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                symptom: symptom,
                condition: condition
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        showResult(data.result);

    } catch (error) {
        showResult(
            error.message ||
            "서버에 연결하지 못했습니다. Python 서버가 실행 중인지 확인해주세요."
        );
    } finally {
        analyzeBtn.disabled = false;
        analyzeBtn.textContent = "AI 분석하기";
    }
});