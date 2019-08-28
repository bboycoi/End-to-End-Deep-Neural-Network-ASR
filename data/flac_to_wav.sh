# Convert all .flac files within this folder to .wav files

find . -iname "*.wav" | wc

for flacfile in `find . -iname "*.wav"`
do
    avconv -y -f wav -i $flacfile -ab 64k -ac 1 -ar 16000 -f wav "${flacfile%.*}.wav"
done
