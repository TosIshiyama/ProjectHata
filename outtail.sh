#!/bin/sh

# output.datがたまりすぎるので、末尾500件のみにリサイズする。適当なタイミングでcronで呼び出して運用すること
tail -500 /home/pi/ProjectHata/web/output.dat > /home/pi/ProjectHata/web/o_tmp.dat
mv -f /home/pi/ProjectHata/web/o_tmp.dat /home/pi/ProjectHata/web/output.dat
