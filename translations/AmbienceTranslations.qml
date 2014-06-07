import QtQuick 2.0

Item {
    function qsTrIdString() {
        //% "Ambience Name"
        QT_TRID_NOOP("harbour-ambience-%ProjectName%")
        //% "Ringtone"
        QT_TRID_NOOP("%ProjectName%-ringtone")
        //% "IM tone"
        QT_TRID_NOOP("%ProjectName%-im")
        //% "Email tone"
        QT_TRID_NOOP("%ProjectName%-email")
        //% "Message tone"
        QT_TRID_NOOP("%ProjectName%-message")
        //% "Calendar alarm"
        QT_TRID_NOOP("%ProjectName%-calendar-alarm")
        //% "Clock Alarm"
        QT_TRID_NOOP("%ProjectName%-clock-alarm")
    }
}
