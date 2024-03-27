#include "phylib.h"
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <stdio.h>

// Allocate memory for a new phylib_object, set its type to PHYLIB_STILL_BALL,
// and transfer the information provided in the function parameters into the structure.
// Return a pointer to the phylib_object. Return NULL if malloc fails.
phylib_object *phylib_new_still_ball(unsigned char number, phylib_coord *pos) {
    // Implementation here

    // Allocate memory for a new phylib_object
    phylib_object *new_object = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if malloc was successful
    if (new_object == NULL) {
        return NULL; // Return NULL if malloc fails
    }

    // Set the type of the new object to PHYLIB_STILL_BALL
    new_object->type = PHYLIB_STILL_BALL;

    // Transfer information from parameters to the structure
    new_object->obj.still_ball.number = number;
    new_object->obj.still_ball.pos = *pos;

    // Return a pointer to the phylib_object
    return new_object;

}

// Allocate memory for a new phylib_object, set its type to PHYLIB_ROLLING_BALL,
// and transfer the information provided in the function parameters into the structure.
// Return a pointer to the phylib_object. Return NULL if malloc fails.
phylib_object *phylib_new_rolling_ball(unsigned char number, phylib_coord *pos, phylib_coord *vel, phylib_coord *acc) {
    // Implementation here

    //Memory leak here 
    phylib_object *new_object = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if malloc was successful
    if (new_object == NULL) {
        return NULL; // Return NULL if malloc fails
    }

    // Set the type of the new object to PHYLIB_ROLLING_BALL
    new_object->type = PHYLIB_ROLLING_BALL;

    // Transfer information from parameters to the structure
    new_object->obj.rolling_ball.number = number;
    new_object->obj.rolling_ball.pos = *pos;
    new_object->obj.rolling_ball.vel = *vel;
    new_object->obj.rolling_ball.acc = *acc;

    // Return a pointer to the phylib_object
    return new_object;
}

// Allocate memory for a new phylib_object, set its type to PHYLIB_HOLE,
// and transfer the information provided in the function parameters into the structure.
// Return a pointer to the phylib_object.
phylib_object *phylib_new_hole(phylib_coord *pos) {
    // Implementation here

    // Allocate memory for a new phylib_object
    phylib_object *new_object = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if malloc was successful
    if (new_object == NULL) {
        return NULL; // Return NULL if malloc fails
    }

    // Set the type of the new object to PHYLIB_HOLE
    new_object->type = PHYLIB_HOLE;

    // Transfer information from parameters to the structure
    new_object->obj.hole.pos = *pos;

    // Return a pointer to the phylib_object
    return new_object;
}

// Allocate memory for a new phylib_object, set its type to PHYLIB_HCUSHION,
// and transfer the information provided in the function parameters into the structure.
// Return a pointer to the phylib_object.
phylib_object *phylib_new_hcushion(double y) {
    // Implementation here

    phylib_object *new_object = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if malloc was successful
    if (new_object == NULL) {
        return NULL; // Return NULL if malloc fails
    }

    // Set the type of the new object to PHYLIB_HCUSHION
    new_object->type = PHYLIB_HCUSHION;

    // Transfer information from parameters to the structure
    new_object->obj.hcushion.y = y;

    // Return a pointer to the phylib_object
    return new_object;
}

// Allocate memory for a new phylib_object, set its type to PHYLIB_VCUSHION,
// and transfer the information provided in the function parameters into the structure.
// Return a pointer to the phylib_object. 
phylib_object *phylib_new_vcushion(double x) {
    // Implementation here

    phylib_object *new_object = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if malloc was successful
    if (new_object == NULL) {
        return NULL; // Return NULL if malloc fails
    }

    // Set the type of the new object to PHYLIB_VCUSHION
    new_object->type = PHYLIB_VCUSHION;

    // Transfer information from parameters to the structure
    new_object->obj.vcushion.x = x;

    // Return a pointer to the phylib_object
    return new_object;
}

// Allocate memory for a new phylib_table.
// Set its time member variable to 0.0 and initialize its object array.
// Return a pointer to the phylib_table. 
phylib_table *phylib_new_table(void) {
    // Implementation here
    phylib_table *table = (phylib_table *)malloc(sizeof(phylib_table));

    phylib_coord lowLeftHole, lowRightHole, medLeftHole, medRightHole, upperLeftHole, upperRightHole;

    //Define position of holes
    lowLeftHole.x = 0;
    lowLeftHole.y = PHYLIB_TABLE_LENGTH;

    lowRightHole.x = PHYLIB_TABLE_WIDTH;
    lowRightHole.y = PHYLIB_TABLE_LENGTH;

    medLeftHole.x = 0;
    medLeftHole.y = PHYLIB_TABLE_WIDTH;

    medRightHole.x = PHYLIB_TABLE_WIDTH;
    medRightHole.y = PHYLIB_TABLE_WIDTH;

    upperLeftHole.x = 0;
    upperLeftHole.y = 0;

    upperRightHole.x = PHYLIB_TABLE_WIDTH;
    upperRightHole.y = 0;

    table->time = 0;

    // Check if malloc was successful
    if (table == NULL) {
        return NULL; // Return NULL if malloc fails
    }

    for (int i =0; i < PHYLIB_MAX_OBJECTS; i++)
    {
        table->object[i] = NULL;
    }

    //Add objects to table
    table->time = 0.0;
    table->object[0] = phylib_new_hcushion(0.0);
    table->object[1] = phylib_new_hcushion(PHYLIB_TABLE_LENGTH);
    table->object[2] = phylib_new_vcushion(0.0);
    table->object[3] = phylib_new_vcushion(PHYLIB_TABLE_WIDTH);
    table->object[4] = phylib_new_hole(&upperLeftHole);
    table->object[5] = phylib_new_hole(&medLeftHole);
    table->object[6] = phylib_new_hole(&lowLeftHole);
    table->object[7] = phylib_new_hole(&upperRightHole);
    table->object[8] = phylib_new_hole(&medRightHole);
    table->object[9] = phylib_new_hole(&lowRightHole);

    for (int i = 0; i < 10; i++){
        if (table->object[i] == NULL)
        {
            return NULL;
        }
    }

    return table;
}

// Allocate new memory for a phylib_object.
// Save the address of that object at the location pointed to by dest,
// and copy over the contents of the object from the location pointed to by src.
// If src points to a location containing a NULL pointer, then dest should be assigned the value of NULL.
void phylib_copy_object(phylib_object **dest, phylib_object **src) {
    // Implementation here
    if (*src == NULL)
    {
        *dest = NULL;
        return;
    }
    
    *dest = (phylib_object *)malloc(sizeof(phylib_object));
    memcpy(*dest,*src,sizeof(phylib_object));  
}


// Allocate memory for a new phylib_table, returning NULL if malloc fails.
// Copy the contents pointed to by table to the new memory location and return the address.
phylib_table *phylib_copy_table(phylib_table *table) {
    // Implementation here

    if (table == NULL) {
        return NULL;
    }


    phylib_table *copy_table = (phylib_table *)malloc(sizeof(phylib_table));
    
    if (copy_table == NULL) {
        return NULL;  //Memory allocation failed
    }

    //Set copy table time
    copy_table->time = table->time;

    //Loop through array and add each object
    for (int i = 0; i < PHYLIB_MAX_OBJECTS; i++) {
        if (table->object[i] != NULL) {
            phylib_copy_object(&copy_table->object[i], &table->object[i]);
        } else {
            copy_table->object[i] = NULL;
        }
    }

    return copy_table;
}

// Iterate over the object array in the table until finding a NULL pointer.
// Assign that pointer to be equal to the address of object.
// If there are no NULL pointers in the array, do nothing.
void phylib_add_object(phylib_table *table, phylib_object *object) {
    // Implementation here
    if (table == NULL || object == NULL) {
        return;
    }

    // Iterate over the object array
    for (int i = 0; i < PHYLIB_MAX_OBJECTS; i++) {
        // Check if the current pointer is NULL
        if (table->object[i] == NULL) {
            // Assign the current pointer to the address of the object
            table->object[i] = object;
            return; // Break out of the loop after adding the object
        }
    }
  
}

// Free every non-NULL pointer in the object array of table.
// Also free the table itself.
void phylib_free_table(phylib_table *table) {
    // Implementation here

    // Check if the input table is NULL
    if (table == NULL) {
        return;
    }

    // Iterate over the object array
    for (int i = 0; i < PHYLIB_MAX_OBJECTS; i++) {
        // Check if the current pointer is not NULL
        if (table->object[i] != NULL) {
            // Free the memory allocated for the current object
            free(table->object[i]);
            //table->object[i] = NULL; // Set the pointer to NULL after freeing
        }
    }

    // Free the memory allocated for the table itself
    free(table);
}

// Return the difference between c1 and c2.
// The result’s x value should be c1.x-c2.x and similarly for y.
phylib_coord phylib_sub(phylib_coord c1, phylib_coord c2) {
    // Implementation here

    phylib_coord result;
    result.x = c1.x - c2.x;
    result.y = c1.y - c2.y;
    return result;
}

// Return the length of the vector/coordinate c.
// Calculate this length using the Pythagorean theorem.
double phylib_length(phylib_coord c) {
    // Implementation here
    return sqrt(c.x * c.x + c.y * c.y);
}

// Compute the dot-product between two vectors.
// The dot product is equal to the sum of the product of the x-values and the product of the y-values.
double phylib_dot_product(phylib_coord a, phylib_coord b) {
    // Implementation here
    return a.x * b.x + a.y * b.y;
}


double phylib_distance(phylib_object *obj1, phylib_object *obj2) {
    // Implementation here
    if (obj1 == NULL || obj2 == NULL) {
        return -1.0;  // Invalid objects
    }

    if (obj1->type != PHYLIB_ROLLING_BALL) {
        return -1.0;  // obj1 is not a PHYLIB_ROLLING_BALL
    }

    //Get center one and center two
    phylib_coord center1 = obj1->obj.rolling_ball.pos;
    phylib_coord center2;

    switch (obj2->type) {
        case PHYLIB_STILL_BALL:
            center2 = obj2->obj.still_ball.pos;
            return phylib_length(phylib_sub(center1, center2)) - PHYLIB_BALL_DIAMETER;

        case PHYLIB_ROLLING_BALL:
            center2 = obj2->obj.rolling_ball.pos;
            return phylib_length(phylib_sub(center1, center2)) - PHYLIB_BALL_DIAMETER;

        case PHYLIB_HOLE:
            center2 = obj2->obj.hole.pos;
            return phylib_length(phylib_sub(center1, center2)) - PHYLIB_HOLE_RADIUS;

        case PHYLIB_HCUSHION:
            return fabs(center1.y - obj2->obj.hcushion.y) - PHYLIB_BALL_RADIUS;

        case PHYLIB_VCUSHION:
            return fabs(center1.x - obj2->obj.vcushion.x) - PHYLIB_BALL_RADIUS;

        default:
            return -1.0;  // Invalid obj2 type
    }
}

void phylib_roll( phylib_object *new, phylib_object *old, double time ){

    if (old == NULL || new == NULL){
        return;
    }

    //Check if rolling ball
    if (old->type != PHYLIB_ROLLING_BALL || new->type != PHYLIB_ROLLING_BALL){
        return;
    } 

    //Set new ball position 
    new->obj.rolling_ball.pos.x = old->obj.rolling_ball.pos.x + (old->obj.rolling_ball.vel.x * time) + 
    0.5*old->obj.rolling_ball.acc.x * time * time;
    new->obj.rolling_ball.pos.y = old->obj.rolling_ball.pos.y + (old->obj.rolling_ball.vel.y * time) + 
    0.5*old->obj.rolling_ball.acc.y * time * time;

    //Set new ball velocity 
    new->obj.rolling_ball.vel.x = old->obj.rolling_ball.vel.x + old->obj.rolling_ball.acc.x * time;
    new->obj.rolling_ball.vel.y = old->obj.rolling_ball.vel.y + old->obj.rolling_ball.acc.y * time;

    //Set new ball acceleration
    new->obj.rolling_ball.acc = old->obj.rolling_ball.acc;

    //printf("\n\nOld x velocity: %10.5lf and New x velocity: %10.5lf\n", old->obj.rolling_ball.vel.x ,new->obj.rolling_ball.vel.x);
    //printf("New position x: %10.5lf, New position y: %10.5lf\n", new->obj.rolling_ball.pos.x, new->obj.rolling_ball.pos.y);
    //printf("Acceleration x: %10.5lf\n" ,new->obj.rolling_ball.acc.x );

    //Set velocities and acceleration to zero if negative
    if ((new->obj.rolling_ball.vel.x * old->obj.rolling_ball.vel.x) <= 0)
    {
        new->obj.rolling_ball.vel.x = 0;
        new->obj.rolling_ball.acc.x = 0;
    }
    
    if ((new->obj.rolling_ball.vel.y * old->obj.rolling_ball.vel.y) <= 0)
    {
        //printf("\nVelocity y set to zero");
        new->obj.rolling_ball.vel.y = 0;
        new->obj.rolling_ball.acc.y = 0;
    }
}

unsigned char phylib_stopped( phylib_object *object ){

    if (object == NULL)
    {
        return 0;
    }
    
    if (object->type != PHYLIB_ROLLING_BALL){
        return 0;
    }

    //if velocity is zero set to still ball
    if (object->obj.rolling_ball.vel.x == 0 && object->obj.rolling_ball.vel.y == 0 )
    {
        int ballNumber = object->obj.rolling_ball.number;
        phylib_coord ballPos =  object->obj.rolling_ball.pos;

        object->type = PHYLIB_STILL_BALL;

        object->obj.still_ball.number = ballNumber;
        object->obj.still_ball.pos = ballPos;
        
        return 1;
    }
    return 0;
}

void phylib_bounce( phylib_object **a, phylib_object **b ){
    //Declare variables outside of switch
    phylib_coord r_ab, v_rel;
    unsigned char ballNum = (*b)->obj.still_ball.number;        
    phylib_coord ballPos =  (*b)->obj.still_ball.pos;
    phylib_coord n;

    switch((*b)->type)
    {
        case PHYLIB_HCUSHION: 
            // Horizontal cushion bounce (switch sign)
            (*a)->obj.rolling_ball.vel.y = (*a)->obj.rolling_ball.vel.y * -1;
            (*a)->obj.rolling_ball.acc.y = (*a)->obj.rolling_ball.acc.y * -1;
            break;

        case PHYLIB_VCUSHION: 
            // Vertical cushion bounce (switch sign)
            (*a)->obj.rolling_ball.vel.x = (*a)->obj.rolling_ball.vel.x * -1;
            (*a)->obj.rolling_ball.acc.x = (*a)->obj.rolling_ball.acc.x * -1;
            break;

        case PHYLIB_HOLE:
            // free hole
            free(*a);    // Free the memory of object a
            *a = NULL;   // Set it to NULL
            break;

        case PHYLIB_STILL_BALL:
            //Convert to rolling ball
            (*b)->type = PHYLIB_ROLLING_BALL;

            (*b)->obj.rolling_ball.number = ballNum;
            (*b)->obj.rolling_ball.pos = ballPos;

            (*b)->obj.rolling_ball.vel.y = 0;
            (*b)->obj.rolling_ball.acc.y = 0;

            (*b)->obj.rolling_ball.vel.x = 0;
            (*b)->obj.rolling_ball.acc.x = 0;

        case PHYLIB_ROLLING_BALL:
            // Compute the position of object a with respect to object b (r_ab)
            r_ab = phylib_sub((*a)->obj.rolling_ball.pos,(*b)->obj.rolling_ball.pos);

            // Compute the relative velocity of object a with respect to object b (v_rel)
            v_rel = phylib_sub((*a)->obj.rolling_ball.vel,(*b)->obj.rolling_ball.vel);
        
            // Calculate the length of r_ab and normalize
            n = vector_normalize(r_ab);
            
            //get dot product
            double v_rel_n = phylib_dot_product(v_rel, n);
        
             // Update the velocities of objects a and b
            (*a)->obj.rolling_ball.vel.x -= v_rel_n * n.x;
            (*a)->obj.rolling_ball.vel.y -= v_rel_n * n.y;

            (*b)->obj.rolling_ball.vel.x += v_rel_n * n.x;
            (*b)->obj.rolling_ball.vel.y += v_rel_n * n.y;

            // Compute the speed of objects a and b
            double speed_a = phylib_length((*a)->obj.rolling_ball.vel);
            double speed_b = phylib_length((*b)->obj.rolling_ball.vel);
            
            // Check if the speed is greater than PHYLIB_VEL_EPSILON
            if (speed_a > PHYLIB_VEL_EPSILON) {
                // Set the acceleration of the ball to the negative velocity divided by the speed multiplied by PHYLIB_DRAG
                (*a)->obj.rolling_ball.acc.x = -(*a)->obj.rolling_ball.vel.x / speed_a * PHYLIB_DRAG;
                (*a)->obj.rolling_ball.acc.y = -(*a)->obj.rolling_ball.vel.y / speed_a * PHYLIB_DRAG;
            }
            else{
                (*a)->obj.rolling_ball.acc.x = 0;
                (*a)->obj.rolling_ball.acc.y = 0;
            }

            if (speed_b > PHYLIB_VEL_EPSILON) {
                // Set the acceleration of the ball b to the negative velocity divided by the speed multiplied by PHYLIB_DRAG
                (*b)->obj.rolling_ball.acc.x = -(*b)->obj.rolling_ball.vel.x / speed_b * PHYLIB_DRAG;
                (*b)->obj.rolling_ball.acc.y = -(*b)->obj.rolling_ball.vel.y / speed_b * PHYLIB_DRAG;
            }
            else{
                (*b)->obj.rolling_ball.acc.x = 0;
                (*b)->obj.rolling_ball.acc.y = 0;
            }

            break;
    }
}

unsigned char phylib_rolling( phylib_table *t ){

    if (t == NULL) {
        // Handle the case where the table pointer is NULL
        return 0;
    }

    unsigned char rollingBallCount = 0;

    for (int i = 0; i < PHYLIB_MAX_OBJECTS; i++) {
        // Check if the current pointer is not NULL

        if (t->object[i] != NULL && t->object[i]->type == PHYLIB_ROLLING_BALL) 
        {
            // Check if the object is not NULL and its type is ROLLING_BALL
            rollingBallCount++;
        }
    }   
    return rollingBallCount;
}

phylib_table *phylib_segment(phylib_table *table)
{
    bool endSegment = false;

    if (phylib_rolling(table) == 0){
        //printf("C returns NULL :)");
        return NULL;
    }

    //Create new table
    phylib_table *newTable = phylib_copy_table( table );

    double new_time = PHYLIB_SIM_RATE;

    //WHile newTable time is below max time
    while (new_time < PHYLIB_MAX_TIME)
    { 
        
        //Increment time
        new_time += PHYLIB_SIM_RATE;

        for (int i=0; i < PHYLIB_MAX_OBJECTS; ++i)
        {
            //Check if object is not null and and it is a rolling ball
            if (newTable->object[i] != NULL && newTable->object[i]->type == PHYLIB_ROLLING_BALL 
            && table->object[i]->type == PHYLIB_ROLLING_BALL && table->object[i] != NULL)
            {
                //Roll the ball
                phylib_roll(newTable->object[i], table->object[i], new_time);
            }
        }

        //Loop through rolling balls (start at 10)
        for (int i=10; i < PHYLIB_MAX_OBJECTS; ++i)
        {
            if (newTable->object[i] == NULL)
                continue;

            //Check if rolling ball stopped (not in phylib roll) MOVE THIS
            if (phylib_stopped( newTable->object[i] ) == 1){
                endSegment = true;
            }

            //Loop through object array
            for (int j=0; j < PHYLIB_MAX_OBJECTS; ++j)
            {
                //free after entering
                if (newTable->object[j] == NULL || newTable->object[i] == NULL){
                    continue;
                }

                if ((j == i) || (newTable->object[i] != NULL && newTable->object[i]->type != PHYLIB_ROLLING_BALL)
                    || ((newTable->object[j] != NULL && newTable->object[j]->type == PHYLIB_ROLLING_BALL) && (j < i))){
                     continue;
                }

                //Get distance if two objects
                double dist = phylib_distance( newTable->object[i], newTable->object[j]);
                
                //printf("Distance %d to %d = %10.5lf\n", i,j,dist);
                //If distance is less than zero than call phylib bounce
                if (dist < 0){
                    phylib_bounce( &newTable->object[i], &newTable->object[j]);

                    endSegment = true;
                }
            }
        }
        if (endSegment == true){ 
            newTable->time += new_time;
            return newTable;
        }
    }

    return newTable;
}

//Normalize the vector
phylib_coord vector_normalize(phylib_coord vector) {
    double length = phylib_length(vector);
    phylib_coord normalized_vector;
    normalized_vector.x = vector.x / length;
    normalized_vector.y = vector.y / length;
    return normalized_vector;
}

char *phylib_object_string( phylib_object *object )
{
    static char string[80];
    
    if (object==NULL)
    {
        snprintf( string, 80, "NULL;" );
        return string;
    }
    
    switch (object->type)
    {
    case PHYLIB_STILL_BALL:
        snprintf( string, 80,
        "STILL_BALL (%d,%6.1lf,%6.1lf)",
        object->obj.still_ball.number,
        object->obj.still_ball.pos.x,
        object->obj.still_ball.pos.y );
        break;
    case PHYLIB_ROLLING_BALL:
        snprintf( string, 80,
        "ROLLING_BALL (%d,%6.1lf,%6.1lf,%6.1lf,%6.1lf,%6.1lf,%6.1lf)",
        object->obj.rolling_ball.number,
        object->obj.rolling_ball.pos.x,
        object->obj.rolling_ball.pos.y,
        object->obj.rolling_ball.vel.x,
        object->obj.rolling_ball.vel.y,
        object->obj.rolling_ball.acc.x,
        object->obj.rolling_ball.acc.y );
        break;
    case PHYLIB_HOLE:
        snprintf( string, 80,
        "HOLE (%6.1lf,%6.1lf)",
        object->obj.hole.pos.x,
        object->obj.hole.pos.y );
        break;
    case PHYLIB_HCUSHION:
        snprintf( string, 80,
        "HCUSHION (%6.1lf)",
        object->obj.hcushion.y );
        break;
    case PHYLIB_VCUSHION:
        snprintf( string, 80,
        "VCUSHION (%6.1lf)",
        object->obj.vcushion.x );
        break;
    }
    
    return string;
}
