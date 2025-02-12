for file in /data/Twitter\ dataset/geoTwitter20-*.zip; do
    echo "Starting map.py on file: $file"
    nohup python3 ~/twitter_coronavirus/src/map.py --input_path "$file" --output_folder ~/twitter_coronavirus/src > "${file##*/}.log" 2>&1 & 
done
echo "Started everything"
