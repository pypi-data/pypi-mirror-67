# Image2ASCII
 
img2ascii is a library written in python which can convert image or video files to ASCII

Option list:

- `-h` or `--help`       : To generate this help text
- `-m` or `--mode`       : Select the mode of operation -- `i` for image, `v` for video and `w` for webcam input
- `-c` or `--color`      : Optional parameter to select color mode. 0 - B/W, 1 - Grayscale and 2 - RGB. Default color mode is B/W
- `-k` or `--kernel`     : Optional parameter to set the kernel size, default is 7px
- `-d` or `--density`    : Optional parameter to set the ASCII text density on image, default is 0.3 units; Range - (0,1) (exclusive)
- `-i` or `--ifile`      : Path to the input file for image and video modes
- `-o` or `--ofile`      : Path to the output file for image and video modes
- `-s` or `--cam_source` : Camera to be used for webcam mode. Use 0,1,2,3... to select cameras connected to the PC. Default value is 0

Installation:
- <b>Direct install : </b>
<t>- `pip install img2ascii`
- <b>From Git : </b><br>
<t>1. `git clone https://github.com/gopaljigaur/img2ascii.git`<br>
<t>2. `cd img2ascii`<br>
<t>3. `python3 setup.py build`<br>
<t>4. `python3 setup.py install`

Usage :

- <b>For image :</b> `img2ascii.py -m <mode>[i=image] -c[color mode (optional)] -i <inputfile> -o <outputfile> -k <kernel_size>[optional] -d <text_density>[optional]`
- <b>For video :</b> `img2ascii.py -m <mode>[v=video] -c[color mode (optional)] -i <inputfile> -o <outputfile> -k <kernel_size>[optional] -d <text_density>[optional]`
- <b>For webcam :</b> `img2ascii.py -m <mode>[w=webcam] -c[color mode (optional)] -k <kernel_size>[optional] -d <text_density>[optional -s <source_camera (0,1,2...)>[optional]`

Usage in python code:

- <b>For image :</b> `from img2ascii import image_gen`<br> 
<t>then `image_gen.generate_ascii_i(color, kernel, density, inputfile, outputfile)`<br>
- <b>For video :</b> `from img2ascii import video_gen`<br> 
<t>then `video_gen.generate_ascii_v(color, kernel, density, inputfile, outputfile)`<br>
- <b>For webcam :</b> `from img2ascii import image_gen`<br> 
<t>then `image_gen.generate_ascii_w(color, kernel, density, cam_source)`
