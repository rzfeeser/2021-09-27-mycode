#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Analyze a log file with code"""

def main():
    """our run time code"""

    cancel = 0
    invite = 0

    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as of:
        for line in of:
            if "invite" in line.lower():
                invite = invite + 1   # add one value to invite
            elif "cancel" in line.lower():
                cancel = cancel + 1

    print("Recap SIP statistics")
    print("No. of INVITEs -", invite)
    print("No. of CANCELs -", cancel)

main()
