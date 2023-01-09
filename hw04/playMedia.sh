#
#   playMedia.sh
#   Sophia Harrison 1/9/23
#   This bash file plays video, displays an image an text
#

export SDL_VIDEODRIVER=fbcon 
export SDL_FBDEV=/dev/fb0

# Display text:
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
     -size $SIZE \
     label:'This is text\nhello\n-sophia' \
     -draw "text 0,200 'Bottom Text'" \
     $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

