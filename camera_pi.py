import io
import time
import picamera
from base_camera import BaseCamera

width = 640 #640
height = 480 #480


class Camera(BaseCamera):
	@staticmethod
	def frames():
		with picamera.PiCamera() as camera:
			camera.resolution = (width, height)
			camera.vflip = True	
			camera.hflip = True	
			# let camera warm up
			time.sleep(2)
		
			stream = io.BytesIO()
			for _ in camera.capture_continuous(stream, 'jpeg',
												 use_video_port=True):
				# return current frame
				stream.seek(0)
				yield stream.read()
				
				# reset stream for next frame
				stream.seek(0)
				stream.truncate()
	
