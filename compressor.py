from PIL import Image
import os

# change the path to your images folder
PATH = "C:/Users/ferna/Downloads/"

if __name__ == '__main__':
    for filename in os.listdir(PATH):
        name, extension = os.path.splitext(PATH + filename)

        if extension in ['.jpg', '.jpeg', '.png']:
            IMAGES_FOLDER = "C:/Users/ferna/Downloads/images/"
            image = Image.open(PATH + filename)
            image.save(IMAGES_FOLDER + 'compressed ' + filename,
                       optimize=True, quality=85)
            os.remove(PATH + filename)

        if extension in ['.mp3', '.WAV']:
            MUSIC_FOLDER = "C:/Users/ferna/Downloads/music/"
            os.rename(PATH + filename, MUSIC_FOLDER + filename)

        if extension in ['.WMV', '.mp4', '.AVI']:
            VIDEO_FOLDER = "C:/Users/ferna/Downloads/videos/"
            os.rename(PATH + filename, VIDEO_FOLDER + filename)
