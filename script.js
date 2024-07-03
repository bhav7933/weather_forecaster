document.getElementById('weatherForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const cityName = document.getElementById('cityName').value;
    fetch(`/getWeather?city=${cityName}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('weatherReport').textContent = data;
        })
        .catch(error => {
            document.getElementById('weatherReport').textContent = 'Error Occurred';
        });
});
