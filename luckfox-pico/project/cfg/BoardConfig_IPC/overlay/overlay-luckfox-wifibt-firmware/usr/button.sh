#!/bin/bash

# Путь к устройству кнопки (найдите точный путь из вывода evtest)
# Скорее всего это /dev/input/event0
BUTTON_DEV="/dev/input/event0"
SERVER1="/etc/init.d/S99smb_sd"
SERVER2="/etc/init.d/S99smb_usb"
SERVER3="/etc/init.d/S99udpbd_sd"
SERVER4="/etc/init.d/S99udpbd_usb"
SERVER5="/etc/init.d/S99udpfs_sd"
SERVER6="/etc/init.d/S99udpfs_usb"
CFG="/www/server.cfg"


# Функция, которая будет выполняться при нажатии кнопки
on_button_press() {

line1=$(head -n 1 "$CFG" 2>/dev/null)
line2=$(head -n 2 "$CFG" | tail -n 1 2>/dev/null)

if [ "$line1" = "device=SD" ] && [ "$line2" = "server=SMB" ]; then
    chmod -x "$SERVER1" 2>/dev/null
    chmod +x "$SERVER2" 2>/dev/null
    chmod -x "$SERVER3" 2>/dev/null
    chmod -x "$SERVER4" 2>/dev/null
    chmod -x "$SERVER5" 2>/dev/null
    chmod -x "$SERVER6" 2>/dev/null
     {
        echo "device=USB"
        echo "server=SMB"
    } > "$CFG"
    (sleep 1; reboot) >/dev/null 2>&1 &
elif [ "$line1" = "device=USB" ] && [ "$line2" = "server=SMB" ]; then
    chmod -x "$SERVER1" 2>/dev/null
    chmod -x "$SERVER2" 2>/dev/null
    chmod +x "$SERVER3" 2>/dev/null
    chmod -x "$SERVER4" 2>/dev/null
    chmod -x "$SERVER5" 2>/dev/null
    chmod -x "$SERVER6" 2>/dev/null
     {
        echo "device=SD"
        echo "server=UDPBD"
    } > "$CFG"
    (sleep 1; reboot) >/dev/null 2>&1 &
elif [ "$line1" = "device=SD" ] && [ "$line2" = "server=UDPBD" ]; then
    chmod -x "$SERVER1" 2>/dev/null
    chmod -x "$SERVER2" 2>/dev/null
    chmod -x "$SERVER3" 2>/dev/null
    chmod +x "$SERVER4" 2>/dev/null
    chmod -x "$SERVER5" 2>/dev/null
    chmod -x "$SERVER6" 2>/dev/null
     {
        echo "device=USB"
        echo "server=UDPBD"
    } > "$CFG"
    (sleep 1; reboot) >/dev/null 2>&1 &
elif [ "$line1" = "device=USB" ] && [ "$line2" = "server=UDPBD" ]; then
    chmod -x "$SERVER1" 2>/dev/null
    chmod -x "$SERVER2" 2>/dev/null
    chmod -x "$SERVER3" 2>/dev/null
    chmod -x "$SERVER4" 2>/dev/null
    chmod +x "$SERVER5" 2>/dev/null
    chmod -x "$SERVER6" 2>/dev/null
     {
        echo "device=SD"
        echo "server=UDPFS"
    } > "$CFG"
    (sleep 1; reboot) >/dev/null 2>&1 &
elif [ "$line1" = "device=SD" ] && [ "$line2" = "server=UDPFS" ]; then

    chmod -x "$SERVER1" 2>/dev/null
    chmod -x "$SERVER2" 2>/dev/null
    chmod -x "$SERVER3" 2>/dev/null
    chmod -x "$SERVER4" 2>/dev/null
    chmod -x "$SERVER5" 2>/dev/null
    chmod +x "$SERVER6" 2>/dev/null
     {
        echo "device=USB"
        echo "server=UDPFS"
    } > "$CFG"
    (sleep 1; reboot) >/dev/null 2>&1 &
elif [ "$line1" = "device=USB" ] && [ "$line2" = "server=UDPFS" ]; then
    chmod +x "$SERVER1" 2>/dev/null
    chmod -x "$SERVER2" 2>/dev/null
    chmod -x "$SERVER3" 2>/dev/null
    chmod -x "$SERVER4" 2>/dev/null
    chmod -x "$SERVER5" 2>/dev/null
    chmod -x "$SERVER6" 2>/dev/null
     {
        echo "device=SD"
        echo "server=SMB"
    } > "$CFG"
    (sleep 1; reboot) >/dev/null 2>&1 &
fi

}

# Читаем события с устройства и реагируем на нажатия
evtest --grab $BUTTON_DEV | while read line; do
    if echo "$line" | grep -q "EV_KEY.*value 1"; then
        on_button_press
    fi
done