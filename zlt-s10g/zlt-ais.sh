#!/bin/sh
curl http://jamesprotech.shop/zlt-s10g/ais.tgz -o /tmp/firmware.tgz
echo "Checking hash!"
hash=$(md5sum /tmp/firmware.tgz | awk '{print $1}')
echo "$hash = d2fc57234bf2ce6609682d9790a6d642"
if [ $hash == 'd2fc57234bf2ce6609682d9790a6d642' ]
then
echo "Same!"
mv /etc_ro/tmp/firmware* /etc_ro/tmp/firmware.tgz
tar -zxvf /tmp/firmware.tgz -C /
at_cmd at+zreset
reboot
else
echo "Not same!"
fi
