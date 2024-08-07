#include <stdio.h>

char *human_readable_time(unsigned seconds, char *time_string) {
    unsigned seconds_in_hour = (60 * 60);
    unsigned hours = seconds / seconds_in_hour;
    seconds %= seconds_in_hour;
    unsigned minutes = seconds / 60;
    seconds %= 60;
    sprintf(time_string, "%02d:%02d:%02d", hours, minutes, seconds);
    return time_string;
}
