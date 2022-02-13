if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Sreejithmadmax/Imdb-Updated-Albert.git /Imdb-Updated-Albert
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Imdb-Updated-Albert
fi
cd /Imdb-Updated-Albert
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
