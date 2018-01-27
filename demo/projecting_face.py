import sys
import dlb
import cv2
import openface

predictor_model = "../models/shape_predictor_68_face_landmarks.dat"

#Take the image file name from the command line
file_name = sys.argv[1]

#Create a HOG face detector using the build-in dlib class
face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlb.shape_predictor(predictor_model)
face_aligner = openface.AlignDlib(predictor_model)

# Take the image file name from the command line
file_name = sys.argv[1]

# Load the image
image = cv2.imread(file_name)

# Run the HOG face detetor on the image data
detected_faces = face_detector(image, 1)

print("Found {} faces in the image fiel {}".format(len(detected_faces), file_name))

# Loop through the each faces we found in the image
for i, face_rect in enumrate(detected_faces):
	#Detected faces are returned as an object with the coordinates
	# of the top, left, right and bottom edeges
	print("- Face #{} found at Left: {} Right{}: Bottom: {}".format(i, face_rect.left(), face_rect.top(), face_rect.right(), face_rect.bottom()))


pose_landmarks = frontal_pose_detector(image, face_rect)

# Get the face's pose
pose_landmarks = face_pose_predictor(image. face_rect)

# Use openface to calculate and perform the face alignment
alignedFace = face_aligner.align(534, image, face_rect, landmarkIndices = openface.AlignDlib.OUTER_EYES_AND_NOSE)
# Save the aligned image to a file
cv2.imwrite("align_face_{}.jpg".format(i), alignedFace)
