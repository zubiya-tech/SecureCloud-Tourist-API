// API key - needed to access our protected Flask API
const API_KEY = "zt-8f3k9x2m7q1w4e6r0p5n";

// Stores the last search results so category filter works without re-fetching
let allResults = [];

// Counts how many API requests were made this session
let requestCount = 0;


function searchCity() {

    let city = document.getElementById("cityInput").value.trim();

    // Stop if user clicked search with empty input
    if (!city) {
        document.getElementById("results").innerHTML =
            "<p class='no-results'>Please enter a city name.</p>";
        return;
    }

    // Show loading while waiting for server response
    document.getElementById("results").innerHTML =
        "<p class='loading'>Loading...</p>";
    document.getElementById("stats").innerHTML = "";

    // Call our Flask API - send API key in request header for authentication
    fetch("/spots/" + city, {
        headers: {
            "X-API-Key": API_KEY
        }
    })
    .then(response => response.json())
    .then(data => {

        // Track number of requests made
        requestCount++;
        document.getElementById("requestCount").innerText = requestCount;

        // API returns results inside "data" key
        if (!data.data || data.data.length === 0) {
            document.getElementById("results").innerHTML =
                "<p class='no-results'>No tourist spots found for " + city + ".</p>";
            document.getElementById("stats").innerHTML = "";
            return;
        }

        // Save results so filters can use them without calling API again
        allResults = data.data;

        // Reset filter buttons to All
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

        // Convert "Taj Mahal" to "Taj-Mahal" for the detail page URL
        let urlName = spot.name.replaceAll(" ", "-");

        // Only add image tag if image exists in database
        let imageHTML = "";
        if (spot.image_url) {
            imageHTML = "<img src='" + spot.image_url +
                "' onerror='this.style.display=\"none\"'>";
        }

        resultsDiv.innerHTML +=
            "<div class='card'>" +
            imageHTML +
            "<div class='card-body'>" +
            "<span class='badge'>" + spot.category + "</span>" +
            "<h3><a href='/spot/" + urlName + "'>" + spot.name + "</a></h3>" +
            "<p>" + spot.description + "</p>" +
            "</div>" +
            "</div>";
    });
}


function filterByCategory(category) {

    // Do nothing if user hasn't searched yet
    if (allResults.length === 0) return;

    setActiveFilter(category);

    if (category === "All") {
        displayResults(allResults);
    } else {
        // Filter from saved results - no new API call needed
        let filtered = allResults.filter(spot => spot.category === category);
        displayResults(filtered);
    }
}


function setActiveFilter(category) {
    // Remove active class from all buttons, add it to selected one
    document.querySelectorAll(".filter-btn").forEach(btn => {
        btn.classList.remove("active");
        if (btn.innerText === category) {
            btn.classList.add("active");
        }
    });
}


// Allow pressing Enter key to trigger search
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("cityInput").addEventListener("keypress", function(e) {
        if (e.key === "Enter") {
            searchCity();
        }
    });
});
