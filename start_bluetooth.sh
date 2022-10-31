#!/usr/bin/bash
bluetoothctl select 00:E0:4C:72:ED:03
bluetoothctl power on
bluetoothctl discoverable on
bluetoothctl pairable on
rfkill unblock all
