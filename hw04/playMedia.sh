#
#   playMedia.sh
#   Sophia Harrison 1/9/23
#   This bash file plays video, displays an image an text
#

export SDL_VIDEODRIVER=fbcon 
export SDL_FBDEV=/dev/fb0

# display image
sudo fbi -noverbose -T 1 -a dog-beagle-portrait.jpg

# rotate and display
TMP_FILE=/tmp/rotate.png
convert dog-beagle-portrait.jpg -rotate 90 $TMP_FILE
sudo fbi -noverbose -T 1 -a $TMP_FILE

# text on image and display
TMP_FILE=/tmp/text.png
convert dog-beagle-portrait.jpg -gravity Center  -fill green -pointsize 100 -annotate 0 'BEAGLE BONE ROCKS' $TMP_FILE
sudo fbi -noverbose -T 1 -a $TMP_FILE

# display video
mplayer -vo fbdev2 -nolirc -framedrop fishies.mp4