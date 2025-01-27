from turtle import *

move_distance = 20
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
Up = 90
Down = 270
Right = 0
Left = 180


class Snake:

    def __init__(self):
        self.list_segments = []
        self.create_snake()
        self.head = self.list_segments[0]

    def create_snake(self):

        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color("red")
        new_segment.penup()
        new_segment.setpos(position)
        self.list_segments.append(new_segment)  # type: ignore

    def extend(self):
        self.add_segment(self.list_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.list_segments)-1, 0, -1):
            new_x = self.list_segments[seg_num - 1].xcor()
            new_y = self.list_segments[seg_num - 1].ycor()
            self.list_segments[seg_num].setpos(new_x, new_y)

        self.list_segments[0].forward(move_distance)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)
    
    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)