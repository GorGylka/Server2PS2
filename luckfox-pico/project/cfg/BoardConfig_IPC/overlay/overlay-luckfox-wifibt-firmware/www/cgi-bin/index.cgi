#!/bin/sh

CFG="/www/server.cfg"

get_cfg_value() {
    KEY="$1"
    if [ -f "$CFG" ]; then
        grep "^$KEY=" "$CFG" 2>/dev/null | head -n 1 | cut -d= -f2
    fi
}

is_mounted() {
    grep -q "[[:space:]]$1[[:space:]]" /proc/mounts
}

storage_text() {
    MNT="$1"
    NAME="$2"

    if is_mounted "$MNT"; then
        LINE="$(df -h "$MNT" 2>/dev/null | tail -n 1)"
        USED="$(echo "$LINE" | awk '{print $3}')"
        TOTAL="$(echo "$LINE" | awk '{print $2}')"
        echo "$NAME: mounted ($USED / $TOTAL)"
    else
        echo "$NAME: not mounted"
    fi
}

storage_class() {
    MNT="$1"
    if is_mounted "$MNT"; then
        echo "ok"
    else
        echo "bad"
    fi
}

CURRENT_DEVICE="$(get_cfg_value device)"
CURRENT_SERVER="$(get_cfg_value server)"

[ -z "$CURRENT_DEVICE" ] && CURRENT_DEVICE="SD"
[ -z "$CURRENT_SERVER" ] && CURRENT_SERVER="SMB"

SD_TEXT="$(storage_text /mnt/sdcard SD)"
USB_TEXT="$(storage_text /mnt/usb USB)"
SD_CLASS="$(storage_class /mnt/sdcard)"
USB_CLASS="$(storage_class /mnt/usb)"

echo "Content-Type: text/html"
echo ""

cat <<EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>PS2 Network Server</title>
    <style>
        body {
            margin: 0;
            padding: 24px;
            background: #f4f6f8;
            color: #1f2937;
            font-family: Arial, sans-serif;
        }
        .wrap {
            max-width: 760px;
            margin: 0 auto;
        }
        .card {
            background: #ffffff;
            border: 1px solid #d8dee4;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
        }
        h1 {
            margin: 0 0 16px 0;
            font-size: 28px;
        }
        h2 {
            margin: 0 0 12px 0;
            font-size: 18px;
        }
        .muted {
            color: #6b7280;
            font-size: 14px;
            margin-top: -8px;
            margin-bottom: 16px;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }
        @media (max-width: 640px) {
            .grid {
                grid-template-columns: 1fr;
            }
        }
        label {
            display: block;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .status {
            padding: 10px 12px;
            border-radius: 10px;
            margin-bottom: 10px;
            font-size: 15px;
            border: 1px solid transparent;
        }
        .ok {
            background: #ecfdf5;
            border-color: #a7f3d0;
            color: #065f46;
        }
        .bad {
            background: #fef2f2;
            border-color: #fecaca;
            color: #991b1b;
        }
        .info {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            color: #1e3a8a;
            padding: 10px 12px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .btn {
            display: inline-block;
            border: 0;
            border-radius: 10px;
            background: #2563eb;
            color: #ffffff;
            padding: 12px 18px;
            font-size: 15px;
            cursor: pointer;
        }
        .btn:hover {
            background: #1d4ed8;
        }
    </style>
</head>
<body>
    <div class="wrap">
        <div class="card">
            <h1>PS2 Network Server</h1>
            <div class="muted">Select server type and storage device</div>

            <form action="/cgi-bin/apply.cgi" method="get">
                <div class="grid">
                    <div>
                        <h2>Storage Device</h2>
EOF

if [ "$CURRENT_DEVICE" = "SD" ]; then
    echo '<label><input type="radio" name="device" value="SD" checked> SD</label>'
else
    echo '<label><input type="radio" name="device" value="SD"> SD</label>'
fi

if [ "$CURRENT_DEVICE" = "USB" ]; then
    echo '<label><input type="radio" name="device" value="USB" checked> USB</label>'
else
    echo '<label><input type="radio" name="device" value="USB"> USB</label>'
fi

cat <<EOF
                    </div>

                    <div>
                        <h2>Server Type</h2>
EOF

if [ "$CURRENT_SERVER" = "SMB" ]; then
    echo '<label><input type="radio" name="server" value="SMB" checked> SMB</label>'
else
    echo '<label><input type="radio" name="server" value="SMB"> SMB</label>'
fi

if [ "$CURRENT_SERVER" = "UDPBD" ]; then
    echo '<label><input type="radio" name="server" value="UDPBD" checked> UDPBD</label>'
else
    echo '<label><input type="radio" name="server" value="UDPBD"> UDPBD</label>'
fi

if [ "$CURRENT_SERVER" = "UDPFS" ]; then
    echo '<label><input type="radio" name="server" value="UDPFS" checked> UDPFS</label>'
else
    echo '<label><input type="radio" name="server" value="UDPFS"> UDPFS</label>'
fi

cat <<EOF
                    </div>
                </div>

                <div style="margin-top: 16px;">
                    <button class="btn" type="submit">Apply and reboot</button>
                </div>
            </form>
        </div>

        <div class="card">
            <h2>Current Configuration</h2>
            <div class="info">Selected device: $CURRENT_DEVICE</div>
            <div class="info">Selected server: $CURRENT_SERVER</div>
            <div class="status $SD_CLASS">$SD_TEXT</div>
            <div class="status $USB_CLASS">$USB_TEXT</div>
        </div>
    </div>
</body>
</html>
EOF