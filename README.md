# Pan-tilt and video streaming.

This is a first release of a Flask application to control the Pimoroni pan and tilt, using their hat
and stream video.

The video streaming uses miguel grinberg post at https://blog.miguelgrinberg.com/post/video-streaming-with-flask

Pan and tilt control uses the Pimoroni web application example.

This release has been tested to confirm that it streams video, it was created for a cooleague who has the
 Pimoroni Hat. Currently I do not have one, when a pan/tilt button is pressed an i2c error is generated.
 As the application is based on Pimoroni code, I am assuming that if you have their hat it will work.
I plan on extending the project to process video using opencv, and use other pan / tilt hats.

