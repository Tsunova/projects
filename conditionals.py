# WRITTEN AS REFERENCED IN THE EXAM SHEET
# Ethan

#1
FOREVER {
    GO TO X: MOUSE_X, MOUSE_Y
    if x_POSITION < 0:
        SEN PEN COLOR TO RED()
    else
        SET PEN COLOR TO ORANGE
}

#2
FOREVER {
    if (DIRECTION < 90):
        SET PEN SIZE TO 5
    else
        SET PEN SIZE TO 1
    MOVE 1 STEPS
    TURN 1 DEGREES
}

#3
FOREVER {
    if (DIRECTION = 30 or DIRECTION = 60):
        SET PEN SIZE TO 10
        SET PEN COLOR TO BLUE
    else
        SET PEN SIZE TO 1
        SET PEN COLOR TO RED
}


# EXPLANATION




#1
it repeats the code.
    first the sprite goes to MOUSE_X and MOUSE_Y.
    if the SPRITE_X position is < 0
        the PEN_COLOR changes to RED
    else if the SPRITE_X position is ~= 0 then
        the PEN_COLOR changes to GREEN

#2
it repeats the code.
    if the sprite direction is < 90;
        the PEN_SIZE set to 5;
    else if the sprite direction is ~= 90 then
        the PEN_SIZE is set to 1
afterwards, the sprite moves 1 step and turns 1 degree to the right

#3
it repeats the code.
    if the SPRITE_DIRECTION is greater than 180 and less than 270
        the PEN_COLOR is set to RED
    else if the SPRITE_DIRECTION ~= 180 or 270 then
        the PEN_COLOR is set to GREEN
afterwards, the sprite moves 1 step and turns 1 degree to the right

#4
it repeats the code.
    if the SPRITE_DIRECTION = 30 or SPRITE_DIRECTION = 60 then
        the PEN_SIZE is set to 10 and
        the PEN_COLOR is set to BLUE
    else if the SPRITE_DIRECTION ~= 30 or 60 then
        the PEN_SIZE is set to 1 and
        the PEN_COLOR is set to RED
afterwards, it moves 1 step and turns 1 degree to the right
