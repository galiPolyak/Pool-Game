import sys
import cgi
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import math
import Physics
import random
import json

# Import physics.py module
from Physics import Coordinate, StillBall, RollingBall, Table, DRAG

# Subclass BaseHTTPRequestHandler to handle GET and POST requests
class MyHandler(BaseHTTPRequestHandler):

    def add_balls(self, table):

        nudge = lambda: random.uniform(-1.5, 1.5)
        # Add balls to the table
        pos1 = Physics.Coordinate(Physics.TABLE_WIDTH / 2.0, Physics.TABLE_WIDTH / 2.0)
        sb1 = Physics.StillBall(1, pos1)
        table += sb1


        pos2 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 4.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER + 4.0) + nudge()
        )
        sb2 = Physics.StillBall(2, pos2)
        table += sb2

        pos3 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 4.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER + 4.0) + nudge()
        )
        sb3 = Physics.StillBall(3, pos3)
        table += sb3

        pos4 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - ((Physics.BALL_DIAMETER * 2) + 8.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * ((Physics.BALL_DIAMETER * 2)+ 6.0) + nudge()
        )
        sb4 = Physics.StillBall(4, pos4)
        table += sb4

        pos5 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + ((Physics.BALL_DIAMETER * 2) + 8.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * ((Physics.BALL_DIAMETER * 2)+ 6.0) + nudge()
        )
        sb5 = Physics.StillBall(5, pos5)
        table += sb5

        pos6 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0,
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * ((Physics.BALL_DIAMETER * 2)+ 6.0) + nudge()
        )
        sb6 = Physics.StillBall(8, pos6)
        table += sb6

        pos7 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 4.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 3 + 6.0) + nudge()
        )
        sb7 = Physics.StillBall(6, pos7)
        table += sb7

        pos8 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 4.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 3 + 6.0) + nudge()
        )
        sb8 = Physics.StillBall(7, pos8)
        table += sb8

        pos9 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER * 3 + 4.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 3 + 10.0) + nudge()
        )
        sb9 = Physics.StillBall(9, pos9)
        table += sb9

        pos10 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER * 3 + 4.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 3 + 10.0) + nudge()
        )
        sb10 = Physics.StillBall(10, pos10)
        table += sb10

        pos11 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0,
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * ((Physics.BALL_DIAMETER * 4)+ 6.0) + nudge()
        )
        sb11 = Physics.StillBall(11, pos11)
        table += sb11

        pos12 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER * 2 + 8.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 4 + 10.0) + nudge()
        )
        sb12 = Physics.StillBall(12, pos12)
        table += sb12

        pos13 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER * 2 + 8.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 4 + 10.0) + nudge()
        )
        sb13 = Physics.StillBall(13, pos13)
        table += sb13

        pos14 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER * 4 + 8.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 4 + 10.0) + nudge()
        )
        sb14 = Physics.StillBall(14, pos14)
        table += sb14

        pos15 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER * 4 + 8.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 4 + 10.0) + nudge()
        )
        sb15 = Physics.StillBall(15, pos15)
        table += sb15

        pos0 = Physics.Coordinate(Physics.TABLE_WIDTH / 2.0 + random.uniform(-3.0, 3.0),
                                            Physics.TABLE_LENGTH - Physics.TABLE_WIDTH / 2.0)
        sb0 = Physics.StillBall(0, pos0)
        table += sb0

    # Handle GET requests
    def do_GET(self):
        try:
            parsed_url = urlparse(self.path)

            if parsed_url.path in ['/playerId.html']:
                # Open and read shoot.html file
                with open('.' + self.path, 'rb') as file:
                    content = file.read()
                # Send the response with appropriate headers
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Content-length', len(content))
                self.end_headers()
                self.wfile.write(content)

            
                for filename in os.listdir('.'):
                    if filename.startswith('table-') and filename.endswith('.svg'):
                        os.remove(filename)
                        print(f"Deleted file: {filename}")

            elif parsed_url.path.startswith('/table-') and parsed_url.path.endswith('.svg'):
                # Extract the table number from the path
                table_num = parsed_url.path.split('-')[1].split('.')[0]
                file_path = f'table-{table_num}.svg'

                if os.path.exists(file_path):
                    # Send the SVG file if it exists
                    self.send_response(200)
                    self.send_header('Content-type', 'image/svg+xml')
                    self.end_headers()
                    with open(file_path, 'rb') as f:
                        self.wfile.write(f.read())
                else:
                    # Send 404 if the file does not exist
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'404: File not found')

            elif parsed_url.path == '/display.html':
                # Generate HTML dynamically
                fp = open('.'+self.path)
                content = fp.read()

                # Send response
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))

            else:
                # Generate 404 for GET requests that aren't the 3 files above
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("404: %s not found" % self.path, "utf-8"))
        except Exception as e:
            print("Error:", e)

    # Handle POST requests
    def do_POST(self):
        try:
            parsed_url = urlparse(self.path)
            print("Requested path:", parsed_url.path)

            if parsed_url.path in ['/display.html']:
                # Parse form data
                form_data = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                # Check if game name and player names are provided
                if 'game_name' not in form_data or 'player1' not in form_data or 'player2' not in form_data:
                    # If any input is missing, send a response indicating bad request
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(bytes("400: Game name or player names are missing", "utf-8"))
                    return

                # Extract game name and player names
                game_name = form_data['game_name'].value
                player1 = form_data['player1'].value
                player2 = form_data['player2'].value

                # Concatenate the game name and player names into HTML format
                html_names = ''
                html_names = f'<h2>Game Name: {game_name}</h2>'
                html_names += f'<p>Player 1: {player1}</p>'
                html_names += f'<p>Player 2: {player2}</p>'

                table = Table()
                self.add_balls(table)
                
                db = Physics.Database( reset=True );
                db.createDB();

                html_content = table.svg()
                    
                html_content = html_content.replace("<svg width", ' <svg id="table" width')
                html_content = html_content.replace("<svg ", '<svg onmousemove="trackit(event);" onmousedown="startDrawing(event);" onmouseup="endDrawing(event);"')
                    
                # Create file name for the SVG
                file_name = "table.svg"

                # Write SVG content to file
                with open(file_name, "w") as svg_file:
                    svg_file.write(html_content)

                    # Move to the next segment
                db.writeTable( table );
                #game = Physics.Game( gameName=game_name, player1Name=player1, player2Name=player2 );
                db.writeGame(0, game_name, player1, player2)
                print("Game created");

                # Read the content of the HTML template file
                #with open('display.html', 'r') as template_file:
                #    html_response = template_file.read()

                html_response = '''
<html>
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>

    <script>
    var track = false; // Set tracking to false by default
    var startX, startY, endX, endY;

    function trackon() {
        track = true;
        alert("Tracking is now on.");
    }

    function trackoff() {
        track = false;
        startX = null;
        startY = null;
        endX = null;
        endY = null;
        clearLine();
    }

    function trackit(event) {
        if (track && event.buttons === 1) { // Check if the left mouse button is pressed
        $('#valx').remove();
        $('#valy').remove();
        var svg = document.getElementById('table');
        var point = svg.createSVGPoint();
        point.x = event.clientX;
        point.y = event.clientY;
        var ctm = svg.getScreenCTM();
        var svgPoint = point.matrixTransform(ctm.inverse());

        $('<div id="valx">' + svgPoint.x + '</div>').appendTo("#x");
        $('<div id="valy">' + svgPoint.y + '</div>').appendTo("#y");

        if (startX && startY) {
            endX = svgPoint.x;
            endY = svgPoint.y;
            drawLine(startX, startY, endX, endY, true);
        }
        }
    }

    function drawLine(startX, startY, endX, endY, visible) {
        var svgNS = "http://www.w3.org/2000/svg";
        var svg = document.getElementById('table');
        var line = svg.querySelector('line');
        if (!line) {
        line = document.createElementNS(svgNS, 'line');
        line.setAttribute('stroke', 'black');
        line.setAttribute('stroke-width', '5'); // Increased line width
        svg.appendChild(line);
        }
        line.setAttribute('x1', startX);
        line.setAttribute('y1', startY);
        line.setAttribute('x2', endX);
        line.setAttribute('y2', endY);
        line.style.display = visible ? 'inline' : 'none'; // Set line visibility
    }

    function clearLine() {
        var svg = document.getElementById('table');
        var line = svg.querySelector('line');
        if (line) {
        line.parentNode.removeChild(line);
        }
    }

    function startDrawing(event) {
        var target = event.target;
        if (target.tagName === 'circle' && target.getAttribute('fill') === 'WHITE') {
        var svg = document.getElementById('table');
        var point = svg.createSVGPoint();
        point.x = event.clientX;
        point.y = event.clientY;
        var ctm = svg.getScreenCTM();
        var svgPoint = point.matrixTransform(ctm.inverse());

        startX = svgPoint.x;
        startY = svgPoint.y;
        }
    }

    function showVelocities(initialXVelocity, initialYVelocity, accX, accY) {
        alert("Initial X Velocity: " + initialXVelocity + "Initial Y Velocity: " + initialYVelocity + "Acceleration X: " + accX + "Acceleration Y: " + accY);
        $('<div class="velocity-event">Initial X Velocity: ' + initialXVelocity + '</div>').appendTo("#events");
        $('<div class="velocity-event">Initial Y Velocity: ' + initialYVelocity + '</div>').appendTo("#events");
        $('<div class="velocity-event">Acceleration X: ' + accX + '</div>').appendTo("#events");
        $('<div class="velocity-event">Acceleration Y: ' + accY + '</div>').appendTo("#events");
        sendDataToServer(initialXVelocity, initialYVelocity, accX, accY);
    }

    function sendDataToServer(initialXVelocity, initialYVelocity, accelerationX, accelerationY) {
        // Create an object containing the data to send
        console.log("Sending data to server...");
        // Create an object containing the data to send
        var data = {
            initialXVelocity: initialXVelocity,
            initialYVelocity: initialYVelocity,
            accelerationX: accelerationX,
            accelerationY: accelerationY
        };

        console.log("Data:", data);

        // Send an AJAX POST request to the server
        $.ajax({
            type: "POST",
            url: "/data",  // Update this URL with the appropriate endpoint on your server
            data: JSON.stringify(data),
            contentType: "application/json",
            success: function(response) {
                // Handle successful response from the server if needed
                console.log("Data sent successfully:", response);
            },
            error: function(xhr, status, error) {
                // Handle errors if any
                console.error("Error sending data:", error);
            }
        });
    }

    function endDrawing(event) {
        var target = event.target;
        if (target.tagName === 'circle' && target.getAttribute('fill') === 'WHITE' && startX && startY) {
        trackit(event);
        startX = null;
        startY = null;
        endX = null;
        endY = null;

        trackit(event);
        startX = null;
        startY = null;
        endX = null;
        endY = null;
        clearLine();
        }
        clearLine();
        var diffX = endX - startX;
        var diffY = endY - startY;

        // Calculate initial velocity based on the difference between release position and cue ball position
        var initialVelocity = Math.sqrt(diffX * diffX + diffY * diffY);

        // Calculate initial x and y velocities
        var initialXVelocity = diffX;
        var initialYVelocity = diffY;

        const DRAG = 150.0;
        var speed = Math.sqrt(initialXVelocity * initialXVelocity + initialYVelocity * initialYVelocity);
        var accX = -initialXVelocity / speed * DRAG;
        var accY = -initialYVelocity / speed * DRAG;

        showVelocities(initialXVelocity, initialYVelocity, accX, accY);
    }

    </script>
</head>
<body>
    <div id = "overwrite">
    ball_content
    </div>

    <button id="b1" onclick="trackon();">Start Drawing</button>
    <button id="b2" onclick="trackoff();">Stop Drawing</button>
    <div id="x">x=</div>
    <div id="y">y=</div>

</body>
</html>
                '''
         
                # Concatenate the HTML names with the SVG content
                html_content_with_names = html_names + html_content

                # Replace the placeholder with the SVG content in the HTML response
                html_response = html_response.replace("ball_content", html_content_with_names)

                # Write the modified HTML response back to the file
                with open('display.html', 'w') as output_file:
                    output_file.write(html_response)
                
                
                self.send_response(302)
                self.send_header('Location', '/display.html')
                self.end_headers()

                # Send the HTML response with 200 OK status
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html_response.encode('utf-8'))
                    
            elif parsed_url.path == '/data':
                # Parse the incoming JSON data
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                # Extract the values from the received JSON data
                initial_x_velocity = data['initialXVelocity']
                initial_y_velocity = data['initialYVelocity']
                acceleration_x = data['accelerationX']
                acceleration_y = data['accelerationY']

                # Do something with the received data (e.g., store it, process it)
                print("Received data:")
                print("Initial X Velocity:", initial_x_velocity)
                print("Initial Y Velocity:", initial_y_velocity)
                print("Acceleration X:", acceleration_x)
                print("Acceleration Y:", acceleration_y)


                # Send a response back to the client if needed
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Data received successfully')

                db = Physics.Database();
                #db.printDatabase

                table_id = 0;
                table = db.readTable( table_id );
                print("table read")

                #game = Physics.Game( gameName="Game 01", player1Name="Stefan", player2Name="Efren Reyes" );
                game_info = db.readGame(table_id);
                gameID, game_name, player_name1, player_name2 = db.readGame(table_id)

                print("Game ID:", gameID)
                print("Game Name:", game_name)
                print("Player 1 Name:", player_name1)
                print("Player 2 Name:", player_name2)
                
                print("game read")

                game = Physics.Game( gameName=game_name, player1Name=player_name1, player2Name=player_name2 );
                #game = Physics.Game( gameName=game_name, player1Name= player_name1, player2Name=player_name2 );
                print("create da game")

                game.shoot( game_name, player_name1, table, initial_x_velocity, initial_y_velocity);

                print("Game shot");
            
                ##ex: 
                def write_svg( table_id, table ):
                    with open( "table%d.svg" % table_id, "w" ) as fp:
                        fp.write( table.svg() );

                db = Physics.Database();

                cur = db.conn.cursor();

                # retreive all tables (regardless of shot)
                cur.execute( """\
                SELECT TABLEID FROM TableShot;""");
                tableIDs = cur.fetchall();


                # this should print a few hundered table IDs
                print( len(tableIDs) );

                # this should print the first 10 frames of the shot
                # the cue ball starts at pos.y=2025.0, with a starting vel.y=-1000.0
                # and moves about 10mm upwards each 0.01s while gradually slowing down
                for i in range( 10 ):
                    print( i, db.readTable( i ) );
                    write_svg(i,db.readTable( i ));

                # this should print 10 frames of the shot as the cue ball hits the racked balls
                for i in range( 143, 153 ):
                    print( i, db.readTable( i ) );
                    write_svg(i,db.readTable( i ));

                cur.close();
                db.conn.commit();
                db.conn.close();              

            else:
                # Generate 404 for POST requests that aren't the file above
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("404: %s not found" % self.path, "utf-8"))
        
        except Exception as e:
            print("Error:", e)


# Main function to start the server
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python server.py <port>')
        sys.exit(1)

    port = int(sys.argv[1])
    server_address = ('', port)

    # Start the server
    httpd = HTTPServer(server_address, MyHandler)
    print(f'Server running on port {port}')
    sys.stdout.flush()  # Flush the output buffer
    httpd.serve_forever()
