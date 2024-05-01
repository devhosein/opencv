# Import libraries
import cv2
import os
import numpy as np

# Define the data path
data_path = "a:/Python/MY_projects/opencv/p2/ac/WIN_20240130_20_31_17_Pro (2).jpg"

# Get the list of folders (each folder corresponds to a person)
folders = os.listdir(data_path)

# Initialize the lists of images and labels
images = []
labels = []

# Loop over the folders
for folder in folders:
    # Get the path of the folder
    folder_path = os.path.join(data_path, folder)
    # Get the list of image files in the folder
    files = os.listdir(folder_path)
    # Loop over the files
    for file in files:
        # Get the path of the image file
        file_path = os.path.join(folder_path, file)
        # Read the image
        image = cv2.imread(file_path)
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Append the image to the list of images
        images.append(gray)
        # Append the label (folder name) to the list of labels
        labels.append(folder)

# Convert the lists to numpy arrays
images = np.array(images)
labels = np.array(labels)

# Create a LBPH face recognizer object
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the recognizer with the images and labels
recognizer.train(images, labels)

# Read the input image
input_image = cv2.imread("input.jpg")

# Convert the input image to grayscale
input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Create a Haar Cascade face detector
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Detect faces in the input image
faces = detector.detectMultiScale(input_gray)

# Loop over the detected faces
for (x, y, w, h) in faces:
    # Crop the face from the image
    face = input_gray[y:y+h, x:x+w]
    # Predict the label and confidence for the face
    label, confidence = recognizer.predict(face)
    # Get the name of the person from the label
    name = folders[label]
    # Draw a rectangle around the face
    cv2.rectangle(input_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Draw the name and confidence

    cv2.putText(input_image, f"{name} ({confidence:.2f})", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    # Show the output image
    cv2.imshow("Output", input_image)
    # Wait for a key press to exit
    cv2.waitKey(0)
    # Destroy all windows
    cv2.destroyAllWindows()
