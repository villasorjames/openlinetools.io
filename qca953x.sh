
#!/bin/sh
opkg update && opkg install kmod-mtd-rw
sleep 3
insmod mtd-rw i_want_a_brick=1
sleep 3
wget -O /tmp/uboot.bin wget https://cdn.jsdelivr.net/gh/villasorjames/openlinetools.io/qca953x.bin
sleep 3
echo "Checking file hash!"
hash=$(md5sum /tmp/uboot.bin | awk '{print $1}')
echo "$hash = 22ba7987cfd13764ed3b8d1cce5f0018"
if [ $hash == '22ba7987cfd13764ed3b8d1cce5f0018' ]
then
    echo "File downloaded successfully!"
    mtd -r write /tmp/uboot.bin bootloader
else
    echo "File is corrupt or incomplete download!"
fi
