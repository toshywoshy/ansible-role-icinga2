#!/usr/bin/env bash
### --------------------------------------------------
### VanTosh Host Notification Mail Commands File
### (c) copyleft 2014 VanTosh
### Author: Toshaan Bharvani <toshaan@vantosh.com>
### --------------------------------------------------
### {{ ansible_managed }}

template=$(cat <<TEMPLATE
***** VanTosh System Monitoring Tool *****

Notification Type: $NOTIFICATIONTYPE

Host: $HOSTALIAS
Address: $HOSTADDRESS
State: $HOSTSTATE

Date/Time: $LONGDATETIME

Additional Info: $HOSTOUTPUT

Comment: [$NOTIFICATIONAUTHORNAME] $NOTIFICATIONCOMMENT
TEMPLATE
)

/usr/bin/printf "%b" "$template" | mail -s "$NOTIFICATIONTYPE - $HOSTDISPLAYNAME is $HOSTSTATE" $USEREMAIL
