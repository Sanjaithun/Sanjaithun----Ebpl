document.getElementById('predictionForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const area = document.getElementById('area').value;
  const bedrooms = document.getElementById('bedrooms').value;
  const bathrooms = document.getElementById('bathrooms').value;
  const location = document.getElementById('location').value;

  const features = [parseFloat(area), parseInt(bedrooms), parseInt(bathrooms), location];

  fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ features: features }),
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById('result').innerText = `🏷️ Predicted Price: ₹ ${data.price.toLocaleString()} Lakhs`;
    })
    .catch(err => {
      document.getElementById('result').innerText = '❌ Error fetching prediction.';
      console.error(err);
    });
});
