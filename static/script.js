// API key to access our protected Flask API
const API_KEY = "zt-8f3k9x2m7q1w4e6r0p5n";

// Saves last search results so filters work without calling API again
let allResults = [];

// Counts requests made this session
let requestCount = 0;


function searchCity() {

    let city = document.getElementById("cityInput").value.trim();

    // Don't search if input is empty
    if (!city) {
        document.getElementById("results").innerHTML =
            "<p class='no-results'>Please enter a city name.</p>";
        return;
    }

    document.getElementById("results").innerHTML =
        "<p class='loading'>Loading...</p>";
    document.getElementById("stats").innerHTML = "";

    // Send request to Flask API with API key in header
    fetch("/spots/" + city, {
        headers: {
            "X-API-Key": API_KEY
        }
    })
    .then(response => response.json())
    .then(data => {

        requestCount++;
        document.getElementById("requestCount").innerText = requestCount;

        // API sends results inside "data" key
        if (!data.data || data.data.length === 0) {
            document.getElementById("results").innerHTML =
                "<p class='no-results'>No tourist spots found for " + city + ".</p>";
            document.getElementById("stats").innerHTML = "";
            return;
        }

        allResults = data.data;
        setActiveFilter("All");
        displayResults(allResults);
    })
    .catch(error => {
        document.getElementById("results").innerHTML =
            "<p class='no-results'>Error loading destinations.</p>";
        console.log(error);
    });
}


function displayResults(spots) {

    let resultsDiv = document.getElementById("results");
    let statsDiv = document.getElementById("stats");

    if (spots.length === 0) {
        resultsDiv.innerHTML = "<p class='no-results'>No spots found in this category.</p>";
        statsDiv.innerHTML = "";
        return;
    }

    statsDiv.innerHTML = "Showing " + spots.length + " destination(s)";
    resultsDiv.innerHTML = "";

    spots.forEach(spot => {

        // Convert "Taj Mahal" to "Taj-Mahal" for the URL
        let urlName = spot.name.replaceAll(" ", "-");

        resultsDiv.innerHTML +=
            "<div class='card'>" +
            "<div class='card-body'>" +
            "<span class='badge'>" + spot.category + "</span>" +
            "<h3><a href='/spot/" + urlName + "'>" + spot.name + "</a></h3>" +
            "<p>" + spot.description + "</p>" +
            "</div>" +
            "</div>";
    });
}


function filterByCategory(category) {

    // Do nothing if no search has been done yet
    if (allResults.length === 0) return;

    setActiveFilter(category);

    if (category === "All") {
        displayResults(allResults);
    } else {
        // Filter saved results - no new API call needed
        let filtered = allResults.filter(spot => spot.category === category);
        displayResults(filtered);
    }
}


function setActiveFilter(category) {
    // Remove active style from all buttons, add it to selected one
    document.querySelectorAll(".filter-btn").forEach(btn => {
        btn.classList.remove("active");
        if (btn.innerText === category) {
            btn.classList.add("active");
        }
    });
}


// Press Enter to search instead of clicking button
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("cityInput").addEventListener("keypress", function(e) {
        if (e.key === "Enter") {
            searchCity();
        }
    });
});
