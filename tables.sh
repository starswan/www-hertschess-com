filename=/tmp/league.tables.$$.html
wget -q -O $filename "http://phptest.mvhs.co.uk/live2011/org.php?org=Herts%20CA&season=2014_2015&x4_report=division"
python tables.py $filename
rm $filename
#crossname=/tmp/cross.tables.$$.html
#wget -q -O $crossname "http://phptest.mvhs.co.uk/live2011/org.php?org=Herts%20CA&season=2014_2015&report=cross"
