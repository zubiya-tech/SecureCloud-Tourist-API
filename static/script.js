function searchCity() {

// Get city entered by user
let city =
    document.getElementById("cityInput").value;

// Send request to Flask API
fetch("/spots/" + city)

    // Convert response into JSON format
    .then(response => response.json())

    .then(data => {

        // Get results section
        let resultsDiv =
            document.getElementById("results");

        // Show number of destinations found
        resultsDiv.innerHTML =
            "<h2>Found " +
            data.results.length +
            " destinations</h2>";

        // If no destinations found
        if (data.results.length === 0) {

            resultsDiv.innerHTML =
                "<p>No tourist spots found.</p>";

        } else {

            // Loop through every destination
            data.results.forEach(spot => {

                // Convert destination name into URL format
                // Example:
                // Taj Mahal -> Taj-Mahal
                let urlName =
                    spot.name.replaceAll(" ", "-");

                // Create image section
                let imageHTML = "";

                // Only show image if image_url exists
                if (spot.image_url) {

                    imageHTML =
                        "<img src='" +
                        spot.image_url +
                        "' " +
                        "onerror='this.style.display=\"none\"'>";

                }

                // Add destination card
                resultsDiv.innerHTML +=

                    "<div class='card'>" +

                    imageHTML +

                    "<h3>" +

                    "<a href='/spot/" +
                    urlName +
                    "'>" +

                    spot.name +

                    "</a>" +

                    "</h3>" +

                    "<p><b>Category:</b> " +
                    spot.category +
                    "</p>" +

                    "<p>" +
                    spot.description +
                    "</p>" +

                    "</div>";
            });
        }
    })

    // Show error message if something goes wrong
    .catch(error => {

        document.getElementById("results").innerHTML =
            "<p>Error loading destinations.</p>";

        console.log(error);
    });

}                
