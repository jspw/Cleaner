#! /usr/bin/env python3

#program:cleaner
#@Author : 5hifaT
#github:https://github.com/jspw
#Date:12 June, 2020
#distro : Debian

import os
import sys
import subprocess as sp 


def check_cache():

    print("\nSHOWING CACHES .................\n\n")

    # commands as variables
    check_apt_cache = ["sudo" ,"du" ,"-sh", "/var/cache/apt"]
    check_journal_logs =["sudo" ,"journalctl","--disk-usage"]
    check_thumbnail_cache = ["sudo","du", "-sh", "~/.cache/thumbnails"]

    # Executing
    try :
        sp.call(check_apt_cache)

    except :
        sp.call(["sudo","apt","install","du"])
        sp.call(check_apt_cache)

    try:
        sp.call(check_journal_logs)

    except:
        sp.call(["sudo","apt","install","journalctl"])
        sp.call(check_journal_logs)

    try:
        sp.call(check_thumbnail_cache)

    except Exception as e :
        print(e)


    print("\n\n\n[-] please use -c to clean caches\n")




def clean():

    # Variables
    su = "sudo"
    apt ="apt"

    # Commands 
    autoremove = [su, apt, "autoremove"]
    apt_cache1 = [su, apt, "autoclean"]
    apt_cache2 = [su,apt ,"clean"]
    journal_logs_clean = [su, "journalctl", "--vacuum-time=7d"]
    thumbnail_cache = [su, "rm", "-rf", "~/.cache/thumbnails/*"]



    # Execute
    print("\n\n\nGeting rid of packages that are no longer required........\n\n\n")
    sp.call(autoremove)
    print("\n\n\nCleaning up APT cache..........\n\n\n")
    sp.call(apt_cache1)
    sp.call(apt_cache2)
    print("\n\n\nClearing systemd journal logs 7 days out-dated......\n\n\n")

    try:
        sp.call(journal_logs_clean)

    except:
        sp.call(["sudo","apt","install","journalctl"])
        sp.call(journal_logs_clean)

    print("\n\n\nCleaning the thumbnail cache.......\n\n\n")

    try:
        sp.call(thumbnail_cache)

    except :
        print("Already Cleaned")


    print("All Cleaned!")


def error_msg():
    print("Help:")
    print("\t[-] Please use -s to show caches")
    print("\t[-] Please use -c to clean caches")
    print("\t[-] Please use sudo command to execute properly!")



def main():
    option = sys.argv
    l = len(option)
    if l == 2:
        if option[1] == "-s":
            try:
                check_cache()
            except:
                print("Use sudo command to execute properly!")
        elif option[1] == "-c":
            try:
                clean()
            except:
                print("Use sudo command to execute properly!")
        else :
            error_msg()
    else :
        error_msg()







if __name__ == "__main__":
        main()