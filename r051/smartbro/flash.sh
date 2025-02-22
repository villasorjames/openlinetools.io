#!/bin/sh
wget http://jamestech123.online/r051/smartbro/r051-smartbro-8bands.bin -O /tmp/firmware.bin
mv /tmp/firmware* /tmp/firmware.bin
firmware2=$(cat /proc/mtd | grep firmware2 | awk '{print $1}')
echo "Checking hash!"
hash=$(md5sum /tmp/firmware.bin | awk '{print $1}')
echo "$hash = 86b00ec51f178242483bba656dfcacc0"
if [ $hash == '86b00ec51f178242483bba656dfcacc0' ]
then
echo "Same!"
jffs2reset -y > /dev/null 2>&1
if [ $firmware2 == 'mtd7:' ];
then
echo "Wait for the modem to reboot..."
mtd -r write /tmp/firmware.bin /dev/mtd4
exit
fi
echo "Wait for the modem to reboot..."
mtd -r write /tmp/firmware.bin /dev/mtd5
exit
else
echo "Not same!"
fi
