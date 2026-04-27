#!/bin/sh
# Configuration CGI script for selecting device and server

echo "Content-type: text/html"
echo ""

# --- Function to display the form ---
show_form() {
    device_val="$1"
    server_val="$2"
    mount_status="$3"
    disk_usage="$4"

    cat <<EOF
<!DOCTYPE html>
<html>
<head>
    <title>Server Configuration</title>
    <meta charset="utf-8">
    <style>
        body { font-family: sans-serif; margin: 2em; }
        fieldset { margin: 1em 0; padding: 1em; }
        legend { font-weight: bold; }
        input[type="submit"] { font-size: 1.2em; padding: 0.5em 1em; }
        .status { background: #eee; padding: 1em; border-radius: 5px; }
    </style>
</head>
<body>
<h1>Select Device and Server</h1>
<form method="post" action="/cgi-bin/config.cgi">
    <fieldset>
        <legend>Storage Device</legend>
        <label><input type="radio" name="device" value="SD" ${device_val}="SD" ? "checked" : ""}> SD Card</label><br>
        <label><input type="radio" name="device" value="USB" ${device_val}="USB" ? "checked" : ""}> USB Drive</label>
    </fieldset>
    <fieldset>
        <legend>Server Type</legend>
        <label><input type="radio" name="server" value="SMB" ${server_val}="SMB" ? "checked" : ""}> SMB</label><br>
        <label><input type="radio" name="server" value="UDPBD" ${server_val}="UDPBD" ? "checked" : ""}> UDPBD</label><br>
        <label><input type="radio" name="server" value="UDPFS" ${server_val}="UDPFS" ? "checked" : ""}> UDPFS</label>
    </fieldset>
    <p><input type="submit" name="apply" value="Apply and Reboot"></p>
</form>

<div class="status">
    <h2>Device Status</h2>
    <p><strong>Mount status:</strong> $mount_status</p>
    <p><strong>Disk usage:</strong> $disk_usage</p>
</div>
</body>
</html>
EOF
}

# --- Read current configuration ---
CONFIG_FILE="/www/server.cfg"
device=""
server=""
if [ -f "$CONFIG_FILE" ]; then
    while IFS='=' read -r key value; do
        case "$key" in
            device) device="$value" ;;
            server) server="$value" ;;
        esac
    done < "$CONFIG_FILE"
fi

# --- Function to check mount status and disk usage ---
check_mount() {
    dev_type="$1"
    mount_point=""
    case "$dev_type" in
        SD) mount_point="/mnt/sdcard" ;;
        USB) mount_point="/mnt/usb" ;;
        *) return ;;
    esac

    if mount | grep -q "on $mount_point "; then
        mount_status="Mounted"
        usage=$(df -h "$mount_point" 2>/dev/null | awk 'NR==2 {print $3 " / " $2 " (" $5 " used)"}')
        if [ -n "$usage" ]; then
            disk_usage="$usage"
        else
            disk_usage="Error retrieving data"
        fi
    else
        mount_status="Not mounted"
        disk_usage="N/A"
    fi
}

# If device is known, get status
mount_status="Not mounted"
disk_usage="N/A"
if [ -n "$device" ]; then
    check_mount "$device"
fi

# --- Handle POST (form submission) ---
if [ "$REQUEST_METHOD" = "POST" ]; then
    # Read POST data (simple, no multipart handling)
    read -r POST_DATA

    # Extract parameters
    new_device=$(echo "$POST_DATA" | sed -n 's/.*device=\([^&]*\).*/\1/p')
    new_server=$(echo "$POST_DATA" | sed -n 's/.*server=\([^&]*\).*/\1/p')

    if [ -n "$new_device" ] && [ -n "$new_server" ]; then
        # Save configuration
        cat > "$CONFIG_FILE" <<EOF
device=$new_device
server=$new_server
EOF

        # Convert to lowercase for script names
        server_lower=$(echo "$new_server" | tr '[:upper:]' '[:lower:]')
        device_lower=$(echo "$new_device" | tr '[:upper:]' '[:lower:]')
        keep_script="S99${server_lower}_${device_lower}"

        # Disable execution for all scripts except the selected one
        for script in /etc/init.d/S99*_*; do
            if [ -f "$script" ]; then
                base=$(basename "$script")
                if [ "$base" = "$keep_script" ]; then
                    chmod +x "$script"
                else
                    chmod -x "$script"
                fi
            fi
        done

        # Output message and reboot with delay
        echo "Content-type: text/html"
        echo ""
        echo "<html><body><h1>Configuration saved. Rebooting...</h1></body></html>"
        (sleep 2; reboot) &
        exit 0
    fi
fi

# --- If not POST or POST without data, display the form ---
show_form "$device" "$server" "$mount_status" "$disk_usage"