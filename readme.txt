Mandelbrot is the name of the project.  For (ovbious?) reasons.

Gulliver was the name of the first python script to calculate the mandelbrot set.  Eventually I wished the program to be able to remeber a path you follow and then in the background re-run the path at a video frame like speed.  It's too laborious to do by hand due to calculation time.  These paths I've deemed "Walks" which is a nice little word to describe the journey through the mandelbrot set.  Gulliver's Travels came to mind and I liked it so I've used it.



Down to it.

	Gulliver.py
This version is the latest working script that I'm sure of.  It requires a folder called "Images," which may or may not come along with the project clone.  It exists to store every frame generated while running the script.  The naming scheme is based off of the "current walk" which is a number incremented every time the program runs.  The filename also is based off of the current window center coordinate and the number of iterations.  A couple other things too.  Very handy.

The interface is keypad driven, and I think "enter" tells the window to recalculate.  The mouse will recenter the window where clicked.  You can perform many actions in a row before telling the window to refresh.  Such as:  Zoom out twice and click on a new center.  



	Color Gradients:
There are many gradient#.py scripts which define different gradient types.  They used to be compatible with other versions of the scripts, but no longer are.  For now gradient6.py is the current functioning color gradient generator.

	ShowGradient.py
A viewer for the gradient scripts.  Only compatible with newest version gradient7.py

	Other scripts:
Really not sure what they all are at this moment.  Some were attempst at cross script communications...the others, who cares.

	Folder Gulliver3000
The folder GUlliver3000 is where the newest scripts are being written.  I was planning on redesigning the Main interface so that you can manipulate window during the calculations.  In other words I want to make the calculations transparent and continuously running in the background.  
	Gulliver3001.py
Tests the mandelPixel.py class.  No other functionality yet.
	
	mandelPixel Class
A first crack at creating a class to contain all the functions.  
		mandelPixel class
	defines a single point which can iterate itself and manage its values.  current z value, origin (c), iteration count.
		grid class
	defines a grid (array/matrix) of mandelPixels.  The size is intended to be linked to the window size in pixels.  Defined by Top Left (CoordTL) corner and Bottom Right (CoordBR) coordinates as complex numbers.  The grid is then generated from these two coordinates.
