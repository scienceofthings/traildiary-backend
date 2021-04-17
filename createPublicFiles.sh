sourceDirectory="$1"
if ! [ -d "$sourceDirectory" ]; then
    echo "Bitte ein valides Quellverzeichnis angeben."
    exit 1
fi

baseTargetDirectory="$2"
if ! [ -d "$baseTargetDirectory" ]; then
    echo "Bitte ein valides Zielverzeichnis angeben."
    exit 1
fi

# parameters:
#   sourceFileName
#   targetFileName
#   size
generateResponsiveImage() {
	mogrify -write "$2"  -filter Triangle -define filter:support=2 -thumbnail "$3" -unsharp 0.25x0.25+8+0.065 -dither None -posterize 136 -quality 82 -define jpeg:fancy-upsampling=off -define png:compression-filter=5 -define png:compression-level=9 -define png:compression-strategy=1 -define png:exclude-chunk=all -interlace none -colorspace sRGB -strip "$1"
}

# Generates responsive images with various sizes for one given image
# parameters
#   sourceFileName
#   baseForTargetFileName
#   targetDirectory
generateResponsiveImages() {
  if ! [ -f "$1" ]; then
    echo "Keine valide Quelldatei angegeben: $1"
    exit 1
  fi
	fileSizes=( 0210 0715 1020 )
	sourceFileName=$1
	for fileSize in "${fileSizes[@]}"
	do
		destinationFileName="${3}/${2}_w${fileSize}.jpg"
		generateResponsiveImage "$sourceFileName" "$destinationFileName" "$fileSize"
	done;
}

# Initializes the target directory
# parameters
#  targetDirectory
initializeTargetDirectory() {
  targetDirectory=$1
  if [ -d "targetDirectory" ]
  then
	  rm -rf "$targetDirectory"
  fi
  mkdir -p "$targetDirectory"
}

fullTargetDirectory="${baseTargetDirectory}/$(basename "$sourceDirectory")"
initializeTargetDirectory "$fullTargetDirectory"

baseFileName=1
shopt -s nullglob
for FILE in "$sourceDirectory"/{*.jpg,*.JPG,*.jpeg,*.JPEG}
do
	generateResponsiveImages "$FILE" "$baseFileName" "$fullTargetDirectory"
	baseFileName=$((baseFileName +1))
done;

cp "$sourceDirectory"/*.gpx "$fullTargetDirectory"