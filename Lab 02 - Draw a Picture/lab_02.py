import arcade

arcade.open_window(600,600,"Drawing")
arcade.set_background_color(arcade.color.BLACK_OLIVE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(100,500,500,100,arcade.csscolor.BLACK)
arcade.draw_lrtb_rectangle_filled(350,450,150,100,arcade.csscolor.DARK_GOLDENROD)
arcade.draw_line(350,135,450,135,arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(400,135,15,25, arcade.csscolor.BLACK)
arcade.draw_rectangle_filled(400,135,10,20,arcade.csscolor.SILVER)
arcade.draw_rectangle_filled(200,200,10,50,arcade.csscolor.DARK_GOLDENROD)
arcade.draw_circle_filled(200,225,7,arcade.csscolor.GOLD)
arcade.finish_render()
arcade.run()