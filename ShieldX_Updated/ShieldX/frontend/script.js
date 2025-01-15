function loadThreatPredictions() {
    fetch("/predict-threats")
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById("result");
            resultDiv.innerHTML = `<h3>Ameaças Previstos:</h3><ul>${data.predicted_threats.map(t => `<li>${t.threat_type}: ${t.likelihood}</li>`).join('')}</ul>`;
        });
}