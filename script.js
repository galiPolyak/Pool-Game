// Function to track mouse movement and send data to the server for white circles
function trackMouse(event) {
    // Check if the target element is a white circle
    if (event.target.tagName === 'circle' && event.target.getAttribute('fill') === 'WHITE') {
        // Get the SVG element
        var svgElement = document.getElementById('table');

        // Get the position of the SVG element
        var svgRect = svgElement.getBoundingClientRect();

        // Calculate the mouse position relative to the SVG element
        var relX = event.clientX - svgRect.left;
        var relY = event.clientY - svgRect.top;

        // Display the relative mouse position
        console.log('Relative X:', relX);
        console.log('Relative Y:', relY);

        // Update the HTML element to display the mouse position
        var positionElement = document.getElementById('mouse-position');
        positionElement.textContent = 'Mouse Position: X=' + relX + ', Y=' + relY;

        // Create a JSON object with the mouse position data
        var mouseData = {
            x: relX,
            y: relY
        };

        // Convert the JSON object to a string
        var jsonData = JSON.stringify(mouseData);

        // Send an AJAX POST request to the server
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/mouse_hover_endpoint', true); // Change the endpoint URL accordingly
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(jsonData);
    }
}
