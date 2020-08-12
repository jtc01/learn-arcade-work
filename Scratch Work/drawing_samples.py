"""
This program will show how to draw
using arcade and python
"""
#import arcade
import arcade
#open an arcade window
#set width, height, and title
arcade.open_window(600,600, "Drawing example")

#choose backround color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
#start drawing
arcade.start_render()
#draw left right top bottom rectangle for ground
arcade.draw_lrtb_rectangle_filled(0,599,300,0,arcade.csscolor.GREEN)
#draw rectangle with height, width, and center for tree
arcade.draw_rectangle_filled(100,330,20,60,arcade.csscolor.SIENNA)
#draw a circle with center and radius for leaves
arcade.draw_circle_filled(100,360,30,arcade.csscolor.DARK_GREEN)
#draw another tree
arcade.draw_rectangle_filled(200,350,20,100,arcade.csscolor.SIENNA)
#draw leaves with ellipsed circle
arcade.draw_ellipse_filled(200,400,60,80,arcade.csscolor.DARK_GREEN)
#draw ANOTHER tree
arcade.draw_rectangle_filled(300,330,20,60,arcade.csscolor.SIENNA)
#Draw wierd looking leaves
arcade.draw_arc_filled(300,360,60,100,arcade.csscolor.DARK_GREEN,-0,180)
#Yes, draw another tree
arcade.draw_rectangle_filled(400,330,20,60,arcade.csscolor.SIENNA)
#CHRISTMAS TREE LEAVES
#(350,360)(450,360)(400,460)
arcade.draw_triangle_filled(350,360,450,360,400,450,arcade.csscolor.DARK_GREEN)
#Another tree
arcade.draw_rectangle_filled(500, 330, 20, 60, arcade.csscolor.SIENNA)
#draw leaves
arcade.draw_polygon_filled(((500, 440),(480, 400),(470, 360),(530, 360),(520, 400)),arcade.csscolor.DARK_GREEN)
#draw sun
arcade.draw_circle_filled(500,550,40,arcade.csscolor.YELLOW)
#draw rays
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)
#draw text at 150, 230 with a font size of 24 pts
arcade.draw_text("Thats a lot of wierd looking trees",100, 230,arcade.color.BLACK, 24)
#finish drawing
arcade.finish_render()
#keep window open until someone closes it
arcade.run()
