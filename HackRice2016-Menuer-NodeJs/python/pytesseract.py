"""
Module that parses the text in an image
"""

import argparse
import subprocess
import cv2


def execute_cmd(cmd):
    """
    Help function that executes a command in the terminal
    """
    return subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]


def preprocessing(in_img_dir, out_img_dir):
    """
    Function that preprocess an image
    """
    # read in image
    img = cv2.imread(in_img_dir)
    
    # convert to gray scale and apply Guassian Filtering
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)
    
    # threshold the image
    #im_th = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    res, im_th = cv2.threshold(im_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    # determine if need to reverse the image
    reverse_img = cv2.bitwise_not(im_th)
    white_count = cv2.countNonZero(im_th)
    total_pixel = white_count + cv2.countNonZero(reverse_img)
    black_ratio = 1 - float(white_count) / total_pixel
    output_img = reverse_img if black_ratio > 0.5 else im_th
    
    # write out image
    cv2.imwrite(out_img_dir,output_img)



def main():
    """
    Top level function
    """
    # arg parser
    parser = argparse.ArgumentParser(description='Python Image Text Parser v1')
    parser.add_argument('-f', required=True, help='image file directory')
    parser.add_argument('-t', default=None, help='tesseract dir')
    parser.add_argument('-o', default=None, help='output file dir')
    parser.add_argument('-p', type=int, default=1, help='pre-preocessing')
    args = parser.parse_args()
        
    # retrieve the file name
    file_name = args.f
    out_name = "out.png" if args.o is None else args.o
    tesseract = "/opt/local/bin/tesseract" if args.t is None else args.t
    
    # preprocessing
    if args.p == 1:
        preprocessing(file_name, out_name)
    else:
        out_name = file_name
    
    # build up command line
    cmd = [tesseract, out_name, "stdout"]
    
    # print output to stdout
    print execute_cmd(cmd)
    



if __name__ == "__main__":
    main()