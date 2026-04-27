#!/bin/sh

CFG="/www/server.cfg"

SMB_SD="/etc/init.d/S99smb_sd"
SMB_USB="/etc/init.d/S99smb_usb"
UDPBD_SD="/etc/init.d/S99udpbd_sd"
UDPBD_USB="/etc/init.d/S99udpbd_usb"
UDPFS_SD="/etc/init.d/S99udpfs_sd"
UDPFS_USB="/etc/init.d/S99udpfs_usb"

DEVICE="$(echo "$QUERY_STRING" | sed -n 's/.*device=\([^&]*\).*/\1/p')"
SERVER="$(echo "$QUERY_STRING" | sed -n 's/.*server=\([^&]*\).*/\1/p')"

[ -z "$DEVICE" ] && DEVICE="SD"
[ -z "$SERVER" ] && SERVER="SMB"

case "$DEVICE" in
    SD|USB) ;;
    *) DEVICE="SD" ;;
esac

case "$SERVER" in
    SMB|UDPBD|UDPFS) ;;
    *) SERVER="SMB" ;;
esac

TARGET=""

case "${SERVER}_${DEVICE}" in
    SMB_SD)
        TARGET="$SMB_SD"
        ;;
    SMB_USB)
        TARGET="$SMB_USB"
        ;;
    UDPBD_SD)
        TARGET="$UDPBD_SD"
        ;;
    UDPBD_USB)
        TARGET="$UDPBD_USB"
        ;;
    UDPFS_SD)
        TARGET="$UDPFS_SD"
        ;;
    UDPFS_USB)
        TARGET="$UDPFS_USB"
        ;;
esac

cat > "$CFG" <<EOF
device=$DEVICE
server=$SERVER
EOF

chmod -x "$SMB_SD" 2>/dev/null
chmod -x "$SMB_USB" 2>/dev/null
chmod -x "$UDPBD_SD" 2>/dev/null
chmod -x "$UDPBD_USB" 2>/dev/null
chmod -x "$UDPFS_SD" 2>/dev/null
chmod -x "$UDPFS_USB" 2>/dev/null

if [ -n "$TARGET" ]; then
    chmod +x "$TARGET" 2>/dev/null
fi

echo "Content-Type: text/html"
echo ""
cat <<EOF
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="0; url=/cgi-bin/index.cgi">
<title>Applying</title>
</head>
<body></body>
</html>
EOF

(sleep 2; reboot) >/dev/null 2>&1 &
exit 0