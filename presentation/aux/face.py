#########################################################################################
# IMPORTS

import argparse
import cv2
import logging
from pathlib import Path
import random
import time

#########################################################################################
# PARAMETERS

FACE_MODEL = cv2.CascadeClassifier('model_faces.xml')
EYE_MODEL = cv2.CascadeClassifier('model_eyes.xml')


#########################################################################################
# ARGPARSER

def get_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-folder', type=str, required=True,
                        help='input folder where original pictures are placed')
    parser.add_argument('-o', '--output-folder', type=str, required=True,
                        help='output folder where processed pictures are placed')
    return parser.parse_args()


#########################################################################################
# FUNCTIONS

def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


#########################################################################################
# CODE

if __name__ == '__main__':

    logger = get_logger()
    args = get_cli()

    for img_path in Path(args.input_folder).glob('**/*.png'):
        logger.info(f'processing student picture: {img_path}')
        image_raw = cv2.imread(str(img_path))
        image = cv2.resize(image_raw, (300, 300))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = FACE_MODEL.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(image, img_path.stem.upper() +
                        ' '+ str(random.choice(range(50, 100))) + ' %',
                        (x, int(y + .09 * h)),
                        cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 255))
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = image[y:y + h, x:x + w]
            eyes = EYE_MODEL.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imwrite(str(Path(args.output_folder) / (img_path.stem + '.png')), image)
        cv2.imshow(str(img_path), image)
        time.sleep(0.5)
