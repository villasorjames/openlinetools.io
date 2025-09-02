#!/bin/sh
opkg update && opkg install kmod-mtd-rw
sleep 3
insmod mtd-rw i_want_a_brick=1
sleep 3
wget -O /tmp/uboot.bin http://jamestech123.online/breed-mt7621-gehua-ghl-r-001.bin
sleep 3
mv /tmp/uboot* /tmp/uboot.bin
echo "Checking file hash!"
hash=$(md5sum /tmp/uboot.bin | awk '{print $1}')
echo "$hash = 2fd662527c2d39cd6ffd49a41bcb8049"
if [ $hash == '2fd662527c2d39cd6ffd49a41bcb8049' ]
then
    echo "File downloaded successfully!"
    mtd -r write /tmp/uboot.bin u-boot
else
    echo "File is corrupt or incomplete download!"
fi