#!/bin/sh

echo "UNLOCKING..."

ubus call version set_atcmd_info '{"atcmd":"AT*PROD=2"}' >/dev/null 2>&1
ubus call version set_atcmd_info '{"atcmd":"AT*MRD_MEP=D"}' >/dev/null 2>&1
ubus call version set_atcmd_info '{"atcmd":"AT*PROD=0"}' >/dev/null 2>&1

echo "FLASHING BOOTLOADER" 
echo "Checking hash!"
hash=$(md5sum /tmp/uboot.bin | awk '{print $1}')
echo "$hash = 707b4f4c5f2cee77affcbd7d0cc712ec"
if [ $hash == '707b4f4c5f2cee77affcbd7d0cc712ec' ]
then
mtd write /tmp/uboot.bin /dev/mtd1 >/dev/null 2>&1
echo "Enabling TFTP Flashing... Done."
else
echo "Not same!"
fi

echo "FLASHING PLDT ARS V6 FIRMWARE" 
firmware2=$(cat /proc/mtd | grep firmware2 | awk '{print $1}')
echo "CHECKING HASH"
hash=$(md5sum /tmp/a.bin | awk '{print $1}')
echo "$hash = 283e12666fdc537fe57795a17ac5b96a"
if [ $hash == '283e12666fdc537fe57795a17ac5b96a' ]
then
echo "SAME!"
echo "FLASHING SMARTBRO ARS VERSION 8 LITE FIRMWARE"
jffs2reset -y 2> /dev/null && firstboot -y 2> /dev/null
if [ $firmware2 == 'mtd7:' ];
then
echo "WAIT FOR THE MODEM TO REBOOT"
mtd -r write /tmp/a.bin /dev/mtd4 2> /dev/null
exit
fi
echo "WAIT FOR THE MODEM TO REBOOT"
mtd -r write /tmp/a.bin /dev/mtd5 2> /dev/null
exit
else
echo "NOT SAME!"
fi