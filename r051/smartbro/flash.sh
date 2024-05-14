#!/bin/sh
wget http://jamesprotech.shop/r051/smartbro/r051-Ars-Firmware.bin -O /tmp/firmware.bin
wget http://jamesprotech.shop/r051/smartbro/uboot.bin -O /tmp/uboot.bin
echo "UNLOCKING..."
jffs2reset -y > /dev/null 2>&1
echo y | firstboot > /dev/null 2>&1
ubus call version set_atcmd_info '{"atcmd":"AT+FLASHBP=0"}' >/dev/null
ubus call version set_atcmd_info '{"atcmd":"AT*MRD_IMEI=D"}' >/dev/null
echo "FLASHING BOOTLOADER" 
echo "Checking hash!"
hash=$(md5sum /tmp/uboot.bin | awk '{print $1}')
echo "$hash = d1e62ee1b49e7c7567a967db819ac531"
if [ $hash == 'd1e62ee1b49e7c7567a967db819ac531' ]
then
mtd write /tmp/firmware.bin /dev/mtd1 >/dev/null 2>&1
echo "Enabling TFTP Flashing... Done."
else
echo "Not same!"
fi
firmware2=$(cat /proc/mtd | grep firmware2 | awk '{print $1}')
echo "Checking hash!"
hash=$(md5sum /tmp/firmware.bin | awk '{print $1}')
echo "$hash = 08590a219ba8fab22338859900b0e8a9"
if [ $hash == '08590a219ba8fab22338859900b0e8a9' ]
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
