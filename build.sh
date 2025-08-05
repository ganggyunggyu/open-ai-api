echo 'pyinstaller cli.py --onefile --name cli --hidden-import=openai --hidden-import=dotenv --hidden-import=requests' > build.sh
chmod +x build.sh