if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Mr-BKM/Lucifer-RoBoT.git /Lucifer-RoBoT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /EvaMaria
fi
cd /Lucifer-RoBoT
pip3 install -U -r requirements.txt
echo "Starting Lucifer RoBoT...."
python3 bot.py
