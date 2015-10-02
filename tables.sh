filename=/tmp/league.tables.$$.html
crossname=/tmp/cross.tables.$$.html
wget -q -O $filename "http://phptest.mvhs.co.uk/live2011/org.php?org=Herts CA" --post-file=league.tables.params
python tables.py $filename
wget -q -O $crossname "http://phptest.mvhs.co.uk/live2011/org.php?org=Herts%20CA&season=2014_2015&report=cross"
