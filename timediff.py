# Stopwatch program, using time difference

def splitIt(timeStr: str) -> int:
    # Splits elapsed time notation into hours and minutes as integer,
    # then returns the time expressed in minutes.
    #
    # Required input:
    #  timeStr - a time string in the format of hh:mm, symbolizing elapsed time
    # Output:
    #  total - the time string in minutes (integer)
    # Other variables:
    #  h, m: hours and minutes
    [h, m] = timeStr.split(":")
    h = int(h)
    m = int(m)
    total = h * 60 + m
    
    return total

def zFill(myStr: str, len0: int) -> str:
    # Fills an hour or minute field with leading zeros if needed.
    # Input:
    #   myStr: The hour or minute field
    #   len0: The expected length of the field (2 for time fields).
    while (len(myStr) < len0):
        myStr = "0" + myStr
    # do nothing if mStr is equal to or longer than len0
    return myStr

def tStr(tMin: int) -> str:
    # Converts time in minutes (integer) to string.
    # Input: tMin
    #     Elapsed time expressed in minutes
    # Output: timeStr
    #     Elapsed time in hh:mm format
    hrs = tMin // 60
    mins = tMin - (hrs * 60)
    
    hStr = str(hrs)
    mStr = str(mins)
    
    # place leading zeros in hours and minutes if needed
    hStr = zFill(hStr, 2)
    mStr = zFill(mStr, 2)
    
    # put the string together
    timeStr = hStr + ":" + mStr
    
    return timeStr

# Main code
time1="09:38"
time2="204:15"

tmin1 = splitIt(time1)
tmin2 = splitIt(time2)

tdiff = tmin2 - tmin1

print("Elapsed time is: ", tStr(tdiff))