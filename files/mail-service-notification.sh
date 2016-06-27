#!/usr/bin/env bash
### --------------------------------------------------                                                                                                                                                                                         
### VanTosh Host Notification Mail Commands File
### (c) copyleft 2014 VanTosh
### Author: Toshaan Bharvani <toshaan@vantosh.com>
### --------------------------------------------------
### {{ ansible_managed }}

template=$(cat <<TEMPLATE
***** VanTosh System Monitoring Tool  *****

Notification Type: $NOTIFICATIONTYPE

Service: $SERVICEDESC
Host: $HOSTALIAS
Address: $HOSTADDRESS
State: $SERVICESTATE

Date/Time: $LONGDATETIME

Additional Info: $SERVICEOUTPUT

Comment: [$NOTIFICATIONAUTHORNAME] $NOTIFICATIONCOMMENT
TEMPLATE
)

/usr/bin/printf "%b" "$template" | mail -s "$NOTIFICATIONTYPE - $HOSTDISPLAYNAME - $SERVICEDISPLAYNAME is $SERVICESTATE" $USEREMAIL
