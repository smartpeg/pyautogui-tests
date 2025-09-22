# PyAutoGUI
Permette di simulare click di mouse e tastiera. La cosa utile e' che permette di cercare su una GUI usando degli screenshot di riferimento. Come faremo a farlo funzionare senza una GUI dentro una VM? Siamo qui per questo 🔥🔥🔥
## Dipendenze
```bash
sudo apt install -y python3 python3-venv python3-dev python3-tk scrot xvfb gnome-screenshot
Xvfb :99 -ac -screen 0 1024x768x24 &
export DISPLAY=:99

```
## Installazione
```bash
python3 -m venv .
source bin/activate
pip3 install pyautogui xlib tk pillow pyscreeze
```