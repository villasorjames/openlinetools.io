#!/bin/sh
curl http://jamesprotech.shop/zlt-s10g/ais.tgz -o /tmp/firmware.tgz
echo "Checking hash!"
hash=$(md5sum /tmp/firmware.tgz | awk '{print $1}')
echo "$hash = 7f27169e1014599f57eabe31a5b946e3"
if [ $hash == '7f27169e1014599f57eabe31a5b946e3' ]
then
echo "Same!"
mv /etc_ro/tmp/firmware* /etc_ro/tmp/firmware.tgz
tar -zxvf /tmp/firmware.tgz -C /
at_cmd at+zreset
reboot
else
echo "Not same!"
fi
