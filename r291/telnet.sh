#!/bin/sh
fw_setenv dropbear_mode 1
fw_setenv dropbear_key_type 99
fw_setenv dropbear_password root123
/etc/init.d/dropbear stop
/etc/init.d/dropbear start
