import sys
import dlib
from skimage to import io

#Take the image file name from the command line
file_name = sys.argv[1]

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()

win = dlib.image_window()

#Load image into an array
image = io.imread(file_name)

# Run the HOG face detector on the image data.
# The result will be the bounding boxes of the faces in our image.

detected_faces = face_detector(image, 1)

print("I found {} faces in the file {}").format(len(detected_faces), file_name))

#Open a window on the desktop showing the image
win.set_image(image)

# Loop through face we found in the image
for i, face_rect in enumerate(detected_faces):


