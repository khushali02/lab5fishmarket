document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('predictionForm').addEventListener('submit', function(e) {
        e.preventDefault();

        let length1 = document.getElementById('length1').value;
        let length2 = document.getElementById('length2').value;
        let length3 = document.getElementById('length3').value;
        let height = document.getElementById('height').value;
        let width = document.getElementById('width').value;

        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ length1, length2, length3, height, width })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').textContent = `Predicted Weight: ${data.weight} grams`;
        });
    });
});
