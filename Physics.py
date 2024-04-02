import phylib
import sqlite3
import os
import math

HEADER = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="700" height="1375" viewBox="-25 -25 1400 2750"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink">
<rect width="1350" height="2700" x="0" y="0" fill="#C0D0C0" />""";
FOOTER = """</svg>\n""";

################################################################################
# import constants from phylib to global varaibles
BALL_RADIUS  = phylib.PHYLIB_BALL_RADIUS
BALL_DIAMETER = phylib.PHYLIB_BALL_DIAMETER
HOLE_RADIUS = phylib.PHYLIB_HOLE_RADIUS
TABLE_LENGTH = phylib.PHYLIB_TABLE_LENGTH
TABLE_WIDTH = phylib.PHYLIB_TABLE_WIDTH
MAX_OBJECTS = phylib.PHYLIB_MAX_OBJECTS
DRAG = phylib.PHYLIB_DRAG
VEL_EPSILON = phylib.PHYLIB_VEL_EPSILON

#A3 additions
FRAME_INTERVAL = 0.01

################################################################################
# the standard colours of pool balls
# if you are curious check this out:  
# https://billiards.colostate.edu/faq/ball/colors/

BALL_COLOURS = [ 
    "WHITE",
    "YELLOW",
    "BLUE",
    "RED",
    "PURPLE",
    "ORANGE",
    "GREEN",
    "BROWN",
    "BLACK",
    "LIGHTYELLOW",
    "LIGHTBLUE",
    "PINK",             # no LIGHTRED
    "MEDIUMPURPLE",     # no LIGHTPURPLE
    "LIGHTSALMON",      # no LIGHTORANGE
    "LIGHTGREEN",
    "SANDYBROWN",       # no LIGHTBROWN 
    ];

################################################################################
class Coordinate( phylib.phylib_coord ):
    """
    This creates a Coordinate subclass, that adds nothing new, but looks
    more like a nice Python class.
    """
    def __init__(self, x=0.0, y=0.0):
        """
        Constructor function. Requires x and y coordinates as arguments.
        """
        phylib.phylib_coord.__init__(self, x, y);
    
        self.__class__ = Coordinate;

    pass;


################################################################################
class StillBall( phylib.phylib_object ):
    """
    Python StillBall class.
    """

    def __init__( self, number, pos ):
        """
        Constructor function. Requires ball number and position (x,y) as
        arguments.
        """

        # this creates a generic phylib_object
        phylib.phylib_object.__init__( self, 
                                       phylib.PHYLIB_STILL_BALL, 
                                       number, 
                                       pos, None, None, 
                                       0.0, 0.0 );
      
        # this converts the phylib_object into a StillBall class
        self.__class__ = StillBall;


    # add an svg method here
    def svg(self):
        """
        Returns an SVG representation of the StillBall object.
        """
        color = BALL_COLOURS[self.obj.still_ball.number]
        return """<circle cx="%d" cy="%d" r="%d" fill="%s" />\n""" % (self.obj.still_ball.pos.x, self.obj.still_ball.pos.y, BALL_RADIUS, color)



################################################################################
class RollingBall( phylib.phylib_object ):
    """
    Python RollingBall class.
    """

    def __init__( self, number, pos , vel, acc):
        """
        Constructor function. Requires ball number and position (x,y) as
        arguments.
        """

        # this creates a generic phylib_object
        phylib.phylib_object.__init__( self, 
                                       phylib.PHYLIB_ROLLING_BALL, 
                                       number, 
                                       pos, vel, acc, 
                                       0.0, 0.0 );
      
        # this converts the phylib_object into a StillBall class
        self.__class__ = RollingBall;


    # add an svg method here
    def svg(self):
        """
        Returns an SVG representation of the RollingBall object.
        """
        color = BALL_COLOURS[self.obj.rolling_ball.number]
        return """<circle cx="%d" cy="%d" r="%d" fill="%s" />\n""" % (self.obj.rolling_ball.pos.x, self.obj.rolling_ball.pos.y, BALL_RADIUS, color)


################################################################################

class Hole( phylib.phylib_object ):
    """
    Python Hole class.
    """

    def __init__( self, pos ):
        """
        Constructor function. Requires position (x,y) as argument.
        """
        phylib.phylib_object.__init__( self, 
                                       phylib.PHYLIB_HOLE, 
                                       0, 
                                       pos, 
                                       None, 
                                       None, 
                                       0.0, 0.0 );
        self.__class__ = Hole;


    # add an svg method here
    def svg(self):
        """
        Returns an SVG representation of the Hole object.
        """
        return """<circle cx="%d" cy="%d" r="%d" fill="black" />\n""" % (self.obj.hole.pos.x, self.obj.hole.pos.y, HOLE_RADIUS)

################################################################################

class HCushion( phylib.phylib_object ):
    """
    Python HCushion class.
    """

    def __init__( self, y ):
        """
        Constructor function. Requires y position as argument.
        """
        phylib.phylib_object.__init__( self, 
                                       phylib.PHYLIB_HCUSHION, 
                                       0, 
                                       None, 
                                       None, 
                                       None, 
                                       0.0, 
                                       y );
        self.__class__ = HCushion;
        

    def svg(self):
        """
        Returns an SVG representation of the HCushion.
        """
        y = -25 if self.obj.hcushion.y < 100 else 2700  # Set y value based on the cushion position
        return """<rect width="1400" height="25" x="-25" y="%d" fill="darkgreen" />\n""" %y 


################################################################################
    
class VCushion( phylib.phylib_object ):
    """
    Python VCushion class.
    """

    def __init__( self, x ):
        """
        Constructor function. Requires x position as argument.
        """
        phylib.phylib_object.__init__( self, 
                                       phylib.PHYLIB_VCUSHION, 
                                       0, 
                                       None, 
                                       None, 
                                       None, 
                                       x, 
                                       0.0 );
        self.__class__ = VCushion;
        self.x = x

    def svg(self):
        """
        Returns an SVG representation of the VCushion object.
        """

        x = -25 if self.obj.vcushion.x < 100 else 1350
        return """ <rect width="25" height="2750" x="%d" y="-25" fill="darkgreen" />\n""" %x


################################################################################

class Table( phylib.phylib_table ):
    """
    Pool table class.
    """

    def __init__( self ):
        """
        Table constructor method.
        This method call the phylib_table constructor and sets the current
        object index to -1.
        """
        phylib.phylib_table.__init__( self );
        self.current = -1;

    def __iadd__( self, other ):
        """
        += operator overloading method.
        This method allows you to write "table+=object" to add another object
        to the table.
        """
        self.add_object( other );
        return self;

    def __iter__( self ):
        """
        This method adds iterator support for the table.
        This allows you to write "for object in table:" to loop over all
        the objects in the table.
        """
        return self;

    def __next__( self ):
        """
        This provides the next object from the table in a loop.
        """
        self.current += 1;  # increment the index to the next object
        if self.current < MAX_OBJECTS:   # check if there are no more objects
            return self[ self.current ]; # return the latest object

        # if we get there then we have gone through all the objects
        self.current = -1;    # reset the index counter
        raise StopIteration;  # raise StopIteration to tell for loop to stop

    def __getitem__( self, index ):
        """
        This method adds item retreivel support using square brackets [ ] .
        It calls get_object (see phylib.i) to retreive a generic phylib_object
        and then sets the __class__ attribute to make the class match
        the object type.
        """
        result = self.get_object( index ); 
        if result==None:
            return None;
        if result.type == phylib.PHYLIB_STILL_BALL:
            result.__class__ = StillBall;
        if result.type == phylib.PHYLIB_ROLLING_BALL:
            result.__class__ = RollingBall;
        if result.type == phylib.PHYLIB_HOLE:
            result.__class__ = Hole;
        if result.type == phylib.PHYLIB_HCUSHION:
            result.__class__ = HCushion;
        if result.type == phylib.PHYLIB_VCUSHION:
            result.__class__ = VCushion;
        return result;

    def __str__( self ):
        """
        Returns a string representation of the table that matches
        the phylib_print_table function from A1Test1.c.
        """
        result = "";    # create empty string
        result += "time = %6.1f;\n" % self.time;    # append time
        for i,obj in enumerate(self): # loop over all objects and number them
            result += "  [%02d] = %s\n" % (i,obj);  # append object description
        return result;  # return the string

    def segment( self ):
        """
        Calls the segment method from phylib.i (which calls the phylib_segment
        functions in phylib.c.
        Sets the __class__ of the returned phylib_table object to Table
        to make it a Table object.
        """

        result = phylib.phylib_table.segment( self );
        #if result is None:
         #   print("result is none")
        #else:
        #    print("result: ", result)

        if result:
            #print("We should not be here")
            result.__class__ = Table;
            result.current = -1;
        return result;

    # add svg method here
    def svg(self):
        """
        Generate SVG representation of the table.
        """
        svg_content = HEADER  # Add the HEADER constant to the Physics module
        for obj in self:
            if obj is not None:
                svg_content += obj.svg()  # Assuming each object has an svg() method
        svg_content += FOOTER  # Add the FOOTER constant to the Physics module
        return svg_content
    
    def roll( self, t ):
        new = Table();
        for ball in self:
            if isinstance( ball, RollingBall ):
                # create4 a new ball with the same number as the old ball
                #print("Before rolling: Ball number:", ball.obj.rolling_ball.number)
                #
                new_ball = RollingBall( ball.obj.rolling_ball.number,
                Coordinate(0,0),
                Coordinate(0,0),
                Coordinate(0,0) );
                # compute where it rolls to
                phylib.phylib_roll( new_ball, ball, t );

                #print("After rolling: Ball number:", new_ball.obj.rolling_ball.number)
                
                # add ball to table
                new += new_ball;
            if isinstance( ball, StillBall ):
                # create a new ball with the same number and pos as the old ball
                new_ball = StillBall( ball.obj.still_ball.number,
                Coordinate( ball.obj.still_ball.pos.x,
                ball.obj.still_ball.pos.y ) );
                # add ball to table
                new += new_ball;
        # return table
        return new;

    def cueBall(self):
        """
        Retrieve the cue ball object from the table.

        Returns:
            Ball: The cue ball object.
        """
        for ball in self:
            if isinstance( ball, RollingBall ):  
                if ball.obj.rolling_ball.number == 0:
                    return ball 
            elif isinstance( ball, StillBall ):
                if ball.obj.still_ball.number == 0:
                    return ball  
        # return table
        return None;

class Database:
    def __init__(self, reset=False):
        if reset and os.path.exists('phylib.db'):
            os.remove('phylib.db')
        
        self.conn = sqlite3.connect("phylib.db")
        self.cursor = self.conn.cursor()

    def createDB(self):
        
        self.conn = sqlite3.connect('phylib.db')
        self.cursor = self.conn.cursor()

         # Create Ball 
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Ball (
                BALLID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                BALLNO INTEGER NOT NULL,
                XPOS FLOAT NOT NULL,
                YPOS FLOAT NOT NULL,
                XVEL FLOAT,
                YVEL FLOAT
            )
        """)

        # Create TTable 
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS TTable (
                TABLEID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                TIME FLOAT NOT NULL
            )
        """)

        # SQL query to create the BallTable
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS BallTable (
                BALLID INTEGER NOT NULL,
                TABLEID INTEGER NOT NULL,
                FOREIGN KEY (BALLID) REFERENCES Ball(BALLID),
                FOREIGN KEY (TABLEID) REFERENCES TTable(TABLEID)
            )
        """)

        # SQL query to create the Shot
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Shot (
                SHOTID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                PLAYERID INTEGER NOT NULL,
                GAMEID INTEGER NOT NULL,
                FOREIGN KEY (PLAYERID) REFERENCES Player(PLAYERID),
                FOREIGN KEY (GAMEID) REFERENCES Game(GAMEID)
            )
        """)

        # SQL query to create the TableShot
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS TableShot (
                TABLEID INTEGER NOT NULL,
                SHOTID INTEGER NOT NULL,
                FOREIGN KEY (TABLEID) REFERENCES TTable(TABLEID),
                FOREIGN KEY (SHOTID) REFERENCES Shot(SHOTID)
            )
        """)

        # SQL query to create the Game
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Game (
                GAMEID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                GAMENAME VARCHAR(64) NOT NULL
            )
        """)

        # SQL query to create the Player
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Player (
                PLAYERID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                GAMEID INTEGER NOT NULL,
                PLAYERNAME VARCHAR(64) NOT NULL,
                FOREIGN KEY (GAMEID) REFERENCES Game(GAMEID)
            )
        """)

        #data = self.cursor.execute( """SELECT * FROM sqlite_master;""" );
        #print( data.fetchone() );
        self.cursor.close();
        self.conn.commit();
    
    def readTable(self, tableID):

        # Initialize a Table object
        table = Table()
        self.cursor = self.conn.cursor()

        # Retrieve time attribute from TTable
        self.cursor.execute("SELECT TIME FROM TTable WHERE TABLEID = ?", (tableID + 1,))
        time_result = self.cursor.fetchone()
        if time_result:
            table.time = time_result[0]  # Assign the time attribute from the query result
        else:
            print("Time result is None")
            return None  # If TABLEID does not exist in the BallTable table, return None

        # Retrieve balls from BallTable for the given tableID
        self.cursor.execute("""
            SELECT Ball.BALLID, Ball.BALLNO, Ball.XPOS, Ball.YPOS, Ball.XVEL, Ball.YVEL
            FROM Ball
            JOIN BallTable ON Ball.BALLID = BallTable.BALLID
            WHERE BallTable.TABLEID = ?
        """, (tableID + 1,))

        balls_result = self.cursor.fetchall()
        for ball_data in balls_result:
            ball = None
            ballID, ballNO, xPos, yPos, xVel, yVel = ball_data
            if xVel is None or 0 and yVel is None or 0:
                ball = StillBall(ballNO, Coordinate(xPos, yPos))
            else:
                speed = math.sqrt(xVel*xVel + yVel*yVel)
                rb_acc_x = -xVel/speed * DRAG
                rb_acc_y = -yVel/speed * DRAG
                ball = RollingBall(ballNO, Coordinate(xPos, yPos), Coordinate(xVel, yVel), Coordinate(rb_acc_x, rb_acc_y))
            table += ball

        
        #print(table.__str__())

        return table

    def writeTable(self, table):

        self.cursor = self.conn.cursor()

        # Insert data into TTable
        self.cursor.execute("INSERT INTO TTable (TIME) VALUES (?)", (table.time,))

        # Retrieve the last inserted TABLEID
        table_id = self.cursor.lastrowid

        # Insert data into BALL for each ball in the table
        for ball in table:
            if isinstance(ball, StillBall):
                self.cursor.execute("INSERT INTO Ball (BALLNO, XPOS, YPOS, XVEL, YVEL) VALUES (?, ?, ?, ?, ?)",
                                    (ball.obj.still_ball.number, ball.obj.still_ball.pos.x, ball.obj.still_ball.pos.y,
                                    None, None))
                self.cursor.execute("INSERT INTO BallTable (BALLID, TABLEID) VALUES (?, ?)", (self.cursor.lastrowid, table_id))

            elif isinstance(ball, RollingBall):
                self.cursor.execute("INSERT INTO Ball (BALLNO, XPOS, YPOS, XVEL, YVEL) VALUES (?, ?, ?, ?, ?)",
                                    (ball.obj.rolling_ball.number, ball.obj.rolling_ball.pos.x, ball.obj.rolling_ball.pos.y,
                                    ball.obj.rolling_ball.vel.x, ball.obj.rolling_ball.vel.y))
                self.cursor.execute("INSERT INTO BallTable (BALLID, TABLEID) VALUES (?, ?)", (self.cursor.lastrowid, table_id))

        #print(table.__str__())

        # Close the cursor and the connection
        self.cursor.close()
        self.conn.commit()

        return table_id - 1


    def close(self):
        self.conn.commit()
        self.conn.close()

    def readGame(self, gameID):
        
        print("entered read game");

        game = None
        self.cursor = self.conn.cursor()

        # Retrieve game name from the Game table
        self.cursor.execute("SELECT GAMENAME FROM Game WHERE GAMEID = ?", (gameID + 1,))
        game_name_result = self.cursor.fetchone()

        if not game_name_result:
            print("Game with ID {} does not exist.".format(gameID))
            return None;
        

        self.cursor.execute("SELECT PLAYERNAME, PLAYERID FROM Player WHERE GAMEID = ? ORDER BY PLAYERID", (gameID + 1, ))
        player_result = self.cursor.fetchall()

        if len(player_result) != 2:
            return None;

        player_id1,player_name1 = player_result[0]
        player_id2, player_name2 = player_result[1]


        game_name = game_name_result[0]

        #print("Game ID:", gameID)
        #print("Game Name:", game_name)
        #print("Player 1 Name:", player_id1)
        #print("Player 2 Name:", player_id2)


        game_info = (gameID, game_name, player_id1, player_id2)
        # Initialize a Game object with the retrieved game name
        #game = Game(gameID=gameID, gameName=game_name, player1Name=player_name1, player2Name=player_name2)

        self.cursor.close()
        self.conn.commit()
        return game_info


    def writeGame(self, game_id, gName, p1Name, p2Name):
        self.cursor = self.conn.cursor()

        # Insert game name into the Game table
        self.cursor.execute("INSERT INTO Game (GAMENAME) VALUES (?)", (gName,))
        game_id = self.cursor.lastrowid

        # Insert player names into the Player table
        self.cursor.execute("INSERT INTO Player (GAMEID, PLAYERNAME) VALUES (?, ?)", (game_id, p1Name))
        self.cursor.execute("INSERT INTO Player (GAMEID, PLAYERNAME) VALUES (?, ?)", (game_id, p2Name))

        self.cursor.close()
        self.conn.commit()

        return game_id
    
    def newShot(self, gameName, playerName):
        self.cursor = self.conn.cursor()

        # Retrieve the game ID based on the game name
        self.cursor.execute("SELECT GAMEID FROM Game WHERE GAMENAME = ?", (gameName,))
        game_id_result = self.cursor.fetchone()


        if game_id_result:
            game_id = game_id_result[0]

            # Retrieve the player ID based on the player name
            self.cursor.execute("SELECT PLAYERID FROM Player WHERE PLAYERNAME = ? AND GAMEID = ?", (playerName, game_id))
            player_id_result = self.cursor.fetchone()

            if player_id_result:
                player_id = player_id_result[0]

                # Insert a new entry into the Shot table
                self.cursor.execute("INSERT INTO Shot (PLAYERID, GAMEID) VALUES (?, ?)", (player_id, game_id))
                shot_id = self.cursor.lastrowid

                self.cursor.close()
                self.conn.commit()

                return shot_id
            else:
                print("Player with name '{}' does not exist in game '{}'.".format(playerName, gameName))
        else:
            print("Game with name '{}' does not exist.".format(gameName))

        self.cursor.close()
        self.conn.commit()
        return None

class Game:
    def __init__(self, gameID=None, gameName=None, player1Name=None, player2Name=None):

        print("Entered Game")

        self.gameID = None
        self.gameName = None
        self.player1Name = None
        self.player2Name = None

        self.dBase = Database()
        self.dBase.createDB()

        if gameID is not None:
            #game = self.dBase.readGame(self, gameID)
            self.gameID, self.game_name, self.player1Name, player2Name = self.dBase.readGame(gameID)
            print("She reads the Game")
        
        elif isinstance(gameName, str) and isinstance(player1Name, str) and isinstance(player2Name, str):
            self.gameName = gameName
            self.player1Name = player1Name
            self.player2Name = player2Name
            self.gameID = self.dBase.writeGame(gameID, gameName, player1Name, player2Name)
        else:
            raise TypeError("Invalid combination of arguments for Game constructor")
    
    def shoot(self, gameName, playerName, table, xvel, yvel):
        # Call helper method in Database class to add new entry to Shot table
        # Determine playerID from playerName
        print("Entered shoot heeh")

        # Retrieve the cue ball from the table
        cue_ball = table.cueBall()

        if cue_ball is None:
            print("cue ball is none")
            return None;
    
        shot_id = self.dBase.newShot(gameName, playerName)
    
        # Store cue ball position
        xpos = cue_ball.obj.still_ball.pos.x
        ypos = cue_ball.obj.still_ball.pos.y

        # Set type attribute of cue ball
        cue_ball.type = phylib.PHYLIB_ROLLING_BALL
        #set rolling ball number to zero
        cue_ball.obj.rolling_ball.number = 0
        
        # Set attributes of cue ball
        cue_ball.obj.rolling_ball.pos.x = xpos
        cue_ball.obj.rolling_ball.pos.y = ypos
        cue_ball.obj.rolling_ball.vel.x = xvel
        cue_ball.obj.rolling_ball.vel.y = yvel
        
        # Recalculate acceleration parameters
        speed = math.sqrt(xvel*xvel + yvel*yvel)
        xacc = -xvel/speed * DRAG
        yacc = -yvel/speed * DRAG

        if speed > VEL_EPSILON:
            cue_ball.obj.rolling_ball.acc.x = xacc
            cue_ball.obj.rolling_ball.acc.y = yacc
        else:
            cue_ball.obj.rolling_ball.acc.x = 0
            cue_ball.obj.rolling_ball.acc.y = 0

        #next_table = Table()
        num = 0;

        # Save the table to the database
        table_id = self.dBase.writeTable(table)
                
        # Record the table in the TableShot table
        self.dBase.cursor = self.dBase.conn.cursor()
        self.dBase.cursor.execute("INSERT INTO TableShot (TABLEID, SHOTID) VALUES (?, ?)", (table_id, shot_id))
        self.dBase.conn.commit()

        # Create HTML content for animation
        html_content = "<html>\n<head>\n<title>Animation</title>\n</head>\n<body>\n"


        segnum = 0
        # Start a loop that loops until the segment method returns None
        while True:

            startTime = table.time;

            tabSegment = table.segment();

            if tabSegment is None:
                print("left loop")
                break


            endTime = tabSegment.time;
            segnum = segnum + 1
            
            #print("Segment: ", segnum)

            segment_length = endTime - startTime
            
            # Determine the number of frames in the segment
            num_frames = math.floor(segment_length / FRAME_INTERVAL)
            
            #print("Num frames:  ",num_frames)
            
            # Loop over each frame
            for i in range(num_frames):

                # Calculate the time for the next frame
                frame_time =  i * FRAME_INTERVAL
                
                # Call the roll method to create a new Table object for the next frame
                next_table = table.roll(frame_time)

                 # Set the time of the returned table
                next_table.time = frame_time + startTime

                if next_table is None:
                    print("Next_table is none");
                
                # Save the table to the database
                table_id = self.dBase.writeTable(next_table)
                
                # Record the table in the TableShot table
                self.dBase.cursor = self.dBase.conn.cursor()
                self.dBase.cursor.execute("INSERT INTO TableShot (TABLEID, SHOTID) VALUES (?, ?)", (table_id, shot_id))

                
            
            #if (segment_length > 0.001):
            html_content += tabSegment.svg()
                
            table = tabSegment
            
            self.dBase.conn.commit()
            num += num_frames
            # Get the next segment
            print(num)
            
        # Finish the HTML content
        self.dBase.cursor.close()

        return num;