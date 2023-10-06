document.addEventListener("DOMContentLoaded", function () {
    const getWeatherBtn = document.getElementById("getWeatherBtn");
    const locationInput = document.getElementById("location");
    const minTempInput = document.getElementById("minTemp");
    const maxTempInput = document.getElementById("maxTemp");
    const weatherResult = document.getElementById("weatherResult");

    getWeatherBtn.addEventListener("click", function () {
        const location = locationInput.value;
        const minTemp = minTempInput.value;
        const maxTemp = maxTempInput.value;

        fetch(`/get_weather?city=${location}&min_temp=${minTemp}&max_temp=${maxTemp}`)
            .then((response) => response.json())
            .then((data) => {
                if (data.alert) {
                    weatherResult.textContent = `Temperature Alert: ${data.message}`;
                } else {
                    weatherResult.textContent = data.message;
                }
            })
            .catch((error) => {
                console.error("Error fetching weather data:", error);
            });
    });
});
