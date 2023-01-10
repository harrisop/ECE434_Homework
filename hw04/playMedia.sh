#
#   playMedia.sh
#   Sophia Harrison 1/9/23
#   This bash file plays video, displays an image an text
#

export SDL_VIDEODRIVER=fbcon 
export SDL_FBDEV=/dev/fb0

# display image
#sudo fbi -noverbose -T 1 -a dog-beagle-portrait.jpg    

# display video
#mplayer -vo fbdev2 -nolirc -framedrop fishies.mp4

# Display text:
SIZE=80x80
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background blue -fill blue -font Times-Roman -pointsize 24 \
     -size $SIZE \
     label:'This is text\nhello\n-sophia' \
     -draw "text 0,200 'Bottom Text'" \
     $TMP_FILE

#sudo fbi -noverbose -T 1 $TMP_FILE
convert dog-beagle-portrait.jpg -gravity south \
          -stroke '#000C' -strokewidth 2 -annotate 0 'Faerie Dragon' \
          -stroke  none   -fill white    -annotate 0 'Faerie Dragon' \
          $TMP_FILE
sudo fbi -noverbose -T 1 $TMP_FILE