import cv2
import os 
import argparse
import sys
from glob import glob
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help="path for a image dir")
    parser.add_argument("--output-extract", help="path for a output dir")
    args = parser.parse_args()

    files = glob(os.path.join(args.dir, "*.jpg"))
    rez = []
    if not (args.output_extract is None):
        os.makedirs(args.output_extract, exist_ok=True)
    for file in tqdm(files):
        filename = os.path.basename(file)
        img = cv2.imread(file)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
       
        cv2.imwrite(os.path.join(args.output_extract, "rez"+filename), img)


if __name__ == "__main__":
    main()