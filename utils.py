import os
import face_recognition
import pyttsx3

BASE_PATH = os.getcwd()


def get_all_files(file_loc=os.path.join(BASE_PATH, 'images')):
    return os.listdir(file_loc)


def get_face_encoding():
    face_encoding = {}
    images = get_all_files()
    for image in images:
        face = face_recognition.load_image_file(os.path.join(BASE_PATH, "images", image))
        face_encoding[image] = face_recognition.face_encodings(face[0])
    return face_encoding


def compare_face(face_encoding):
    face_recognition.compare_faces(get_face_encoding(), face_encoding)








