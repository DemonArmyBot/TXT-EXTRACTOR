echo "Cloning Repo..."
git clone https://github.com/DemonArmyBot/TXT-EXTRACTOR.git
cd /TXT-EXTRACTOR
pip install -r requirements.txt
echo "Starting Bot..."
python -m Extractor
