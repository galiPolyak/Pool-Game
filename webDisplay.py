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

js_svg = None

# Subclass BaseHTTPRequestHandler to handle GET and POST requests
class MyHandler(BaseHTTPRequestHandler):

    def add_balls(self, table):

        nudge = lambda: random.uniform(-1.5, 1.5)
        # Add balls to the table
        pos1 = Physics.Coordinate(Physics.TABLE_WIDTH / 2.0, Physics.TABLE_WIDTH / 2.0)
        sb1 = Physics.StillBall(1, pos1)
        table += sb1


        pos2 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 10.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER + 4.0) + nudge()
        )
        sb2 = Physics.StillBall(2, pos2)
        table += sb2

        pos3 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 10.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER + 4.0) + nudge()
        )
        sb3 = Physics.StillBall(3, pos3)
        table += sb3

        pos4 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - ((Physics.BALL_DIAMETER * 2) + 10.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * ((Physics.BALL_DIAMETER * 2)+ 6.0) + nudge()
        )
        sb4 = Physics.StillBall(4, pos4)
        table += sb4

        pos5 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + ((Physics.BALL_DIAMETER * 2) + 10.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * ((Physics.BALL_DIAMETER * 2)+ 6.0) + nudge()
        )
        sb5 = Physics.StillBall(5, pos5)
        table += sb5

        pos6 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0,
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * ((Physics.BALL_DIAMETER * 2)+ 10.0) + nudge()
        )
        sb6 = Physics.StillBall(8, pos6)
        table += sb6

        pos7 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER + 15.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 3 + 10.0) + nudge()
        )
        sb7 = Physics.StillBall(6, pos7)
        table += sb7

        pos8 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER + 15.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 3 + 10.0) + nudge()
        )
        sb8 = Physics.StillBall(7, pos8)
        table += sb8

        pos9 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER * 3 + 20.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 3 + 10.0) + nudge()
        )
        sb9 = Physics.StillBall(9, pos9)
        table += sb9

        pos10 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER * 3 + 20.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 3 + 10.0) + nudge()
        )
        sb10 = Physics.StillBall(10, pos10)
        table += sb10

        pos11 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0,
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * ((Physics.BALL_DIAMETER * 4)+ 15.0) + nudge()
        )
        sb11 = Physics.StillBall(11, pos11)
        table += sb11

        pos12 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER * 2 + 15.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 4 + 15.0) + nudge()
        )
        sb12 = Physics.StillBall(12, pos12)
        table += sb12

        pos13 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER * 2 + 15.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 4 + 15.0) + nudge()
        )
        sb13 = Physics.StillBall(13, pos13)
        table += sb13

        pos14 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 - (Physics.BALL_DIAMETER * 4 + 20.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 4 + 15.0) + nudge()
        )
        sb14 = Physics.StillBall(14, pos14)
        table += sb14

        pos15 = Physics.Coordinate(
            Physics.TABLE_WIDTH / 2.0 + (Physics.BALL_DIAMETER * 4 + 20.0) / 2.0 + nudge(),
            Physics.TABLE_WIDTH / 2.0 - math.sqrt(3.0) / 2.0 * (Physics.BALL_DIAMETER * 4 + 15.0) + nudge()
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
            
            elif parsed_url.path == '/get_svg_anim':
                print("Sending svgs")
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(js_svg.encode('utf-8'))

            else:
                # Generate 404 for GET requests that aren't the 3 files above
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("404: %s not found" % self.path, "utf-8"))
        except Exception as e:
            print("Error:", e)

    # Handle POST requests
    def do_POST(self):
        global current_game_id
       
        #global current_table_id

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

                #table = Table()
                #self.add_balls(table)
                
                db = Physics.Database( reset=True );
                db.createDB();

                #paste og html content CHANGE
                html_content = '''
                <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="700" height="1375" viewBox="-25 -25 1400 2750"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink">
<rect width="1350" height="2700" x="0" y="0" fill="#C0D0C0" /><rect width="1400" height="25" x="-25" y="-25" fill="darkgreen" />
<rect width="1400" height="25" x="-25" y="2700" fill="darkgreen" />
 <rect width="25" height="2750" x="-25" y="-25" fill="darkgreen" />
 <rect width="25" height="2750" x="1350" y="-25" fill="darkgreen" />
<circle cx="0" cy="0" r="114" fill="black" />
<circle cx="0" cy="1350" r="114" fill="black" />
<circle cx="0" cy="2700" r="114" fill="black" />
<circle cx="1350" cy="0" r="114" fill="black" />
<circle cx="1350" cy="1350" r="114" fill="black" />
<circle cx="1350" cy="2700" r="114" fill="black" />
<circle cx="675" cy="675" r="28" fill="YELLOW" />
<circle cx="640" cy="623" r="28" fill="BLUE" />
<circle cx="707" cy="621" r="28" fill="RED" />
<circle cx="612" cy="572" r="28" fill="PURPLE" />
<circle cx="735" cy="570" r="28" fill="ORANGE" />
<circle cx="675" cy="568" r="28" fill="BLACK" />
<circle cx="638" cy="518" r="28" fill="GREEN" />
<circle cx="710" cy="517" r="28" fill="BROWN" />
<circle cx="579" cy="519" r="28" fill="LIGHTYELLOW" />
<circle cx="771" cy="519" r="28" fill="LIGHTBLUE" />
<circle cx="675" cy="463" r="28" fill="PINK" />
<circle cx="610" cy="464" r="28" fill="MEDIUMPURPLE" />
<circle cx="738" cy="464" r="28" fill="LIGHTSALMON" />
<circle cx="549" cy="464" r="28" fill="LIGHTGREEN" />
<circle cx="800" cy="465" r="28" fill="SANDYBROWN" />
<circle cx="676" cy="2025" r="28" fill="WHITE" />
</svg>
                '''
                    
                html_content = html_content.replace("<svg width", ' <svg id="table" width')
                html_content = html_content.replace("<svg ", '<svg onmousemove="trackit(event);" onmousedown="startDrawing(event);" onmouseup="endDrawing(event);"')
                    
                # Create file name for the SVG
                file_name = "table.svg"

                # Write SVG content to file
                with open(file_name, "w") as svg_file:
                    svg_file.write(html_content)

                    # Move to the next segment
                    #CHANGE maybe
                #current_table_id = db.writeTable( table );

                game = Physics.Game( gameName=game_name, player1Name=player1, player2Name=player2 );
                current_game_id = game.gameID
                print("Current game Id: ", current_game_id)
                
                #db.writeGame(0, game_name, player1, player2)
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
    var svg;

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

    function showVelocities(initialXVelocity, initialYVelocity) {
        alert("Initial X Velocity: " + initialXVelocity + ", Initial Y Velocity: " + initialYVelocity);
        $('<div class="velocity-event">Initial X Velocity: ' + initialXVelocity + '</div>').appendTo("#events");
        $('<div class="velocity-event">Initial Y Velocity: ' + initialYVelocity + '</div>').appendTo("#events");
        sendDataToServer(initialXVelocity, initialYVelocity);
    }

    function sendDataToServer(initialXVelocity, initialYVelocity) {
        // Create an object containing the data to send
        console.log("Sending data to server...");
        // Create an object containing the data to send
        var data = {
            initialXVelocity: initialXVelocity,
            initialYVelocity: initialYVelocity,
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

    function getSvgAnimation() {
        $.ajax({
        type: "GET",
        url: "/get_svg_anim",
        success: function(response) {
            // Update SVG contents in HTML dynamically
            console.log('SVGs were received successfully:', response.js_svg);
            animateContents(response.js_svg);
        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
        }
    });
    }

    function animateContents(js_svg){
        let currentIndex = 0;
        const interval = 10; // Interval between displaying SVGs in milliseconds
        const animationInterval = setInterval(() => {
            if (currentIndex >= js_svg.length) {
                clearInterval(animationInterval);
                return;
            }

            document.getElementById('overwrite').innerHTML = js_svg[currentIndex];
            currentIndex++;
        }, interval);
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

        // Calculate initial x and y velocities
        var initialXVelocity = diffX;
        var initialYVelocity = diffY;

        showVelocities(initialXVelocity, initialYVelocity);
    }

    $(document).ready(function() {
        getSvgAnimation();
    });

    </script>
</head>
<body>
    <div id = "overwrite"></div>
    ball_content
                      
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

                # Do something with the received data (e.g., store it, process it)
                print("Received data:")
                print("Initial X Velocity:", initial_x_velocity)
                print("Initial Y Velocity:", initial_y_velocity)


                # Send a response back to the client if needed
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Data received successfully')

                db = Physics.Database();
                #db.printDatabase

                print("Current game Id2: ", current_game_id)
                
                #CHANGE - go into database and get the most highest table-id (join game shot and table)
                # get last table_id
                
                db = Physics.Database();
                cur = db.conn.cursor();

                cur.execute("SELECT TABLEID FROM TableShot ORDER BY TABLEID DESC LIMIT 1;")
                last_table_id = cur.fetchone()
                print("Last table id: ", last_table_id)

                if last_table_id is None:
                    print("Table is none")
                    table = Table()
                    self.add_balls(table)
                else:
                    print("Table exists")
                    print("Last table id: ", last_table_id[0])
                    table = db.readTable(last_table_id[0] )

                print("table read")

                #game = Physics.Game( gameName="Game 01", player1Name="Stefan", player2Name="Efren Reyes" );
                game_ID, game_name, player_name1, player_name2 = db.readGame(current_game_id - 1);

                print("Game ID:", game_ID)
                print("Game Name:", game_name)
                print("Player 1 Name:", player_name1)
                print("Player 2 Name:", player_name2)
                
                print("game read")

                game = Physics.Game( gameID=game_ID, gameName=game_name, player1Name=player_name1, player2Name=player_name2 );
                print("create da game")

                num_frame = game.shoot( game_name, player_name1, table, initial_x_velocity, initial_y_velocity);
                print("Num frames: ",num_frame)

                print("Game shot");

               # db = Physics.Database();

               # cur = db.conn.cursor();

                # retreive all tables (regardless of shot)
                cur.execute( """\
                SELECT TABLEID FROM TableShot;""");
                tableIDs = cur.fetchall();

                anim_content = "<html>\n<head>\n<title>Animation</title>\n</head>\n<body>\n"
                svg_list = []

                for i in range(1, num_frame ):
                    anim_content += db.readTable(i).svg()
                    #json.dumps(svg_list)
                    svg_list.append(db.readTable(i).svg())

                anim_content += "</body>\n</html>"
                js_svg = json.dumps(svg_list)

                with open('newAnim.html', 'w') as output_file:
                   output_file.write(anim_content)

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
