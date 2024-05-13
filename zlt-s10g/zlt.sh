#!/bin/sh
curl http:// jamespro.tech.shop/zlt-s10g/zlt-ais-fw.tgz -o /tmp/firmware.tgz
echo "Checking hash!"
hash=$(md5sum /tmp/firmware.tgz | awk '{print $1}')
echo "$hash = 8ead29179e6a33279e8857a9e90e0efa"
if [ $hash == '8ead29179e6a33279e8857a9e90e0efa' ]
then
echo "Same!"
mv /etc_ro/tmp/firmware* /etc_ro/tmp/firmware.tgz
tar -zxvf /tmp/firmware.tgz -C /
at_cmd at+zreset
reboot
else
echo "Not same!"
fi
