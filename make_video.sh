`mkdir input_frames`
for i in $(seq -f "%04g" 1 300)
do
  `convert -font ./OCRA.ttf -size 2400x1200 xc:White -gravity Center -weight 700 -pointsize 200 -annotate 0 "$i" input_frames/$i.png`
done
`ffmpeg -framerate 60 -i pngs/%04d.png -c:v libx264 -r 60 -pix_fmt yuv420p out.mp4`
