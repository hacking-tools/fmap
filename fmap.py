#!/usr/bin/python3
import sys
import os

if __name__ == "__main__":
    noIP = False

    # Preform arg checks
    try:
        temp = sys.argv[1]
    except:
        print("You didn't provide an IP address")
        print("USAGE: {} <IP Address to Scan>".format(sys.argv[0]))
        noIP = True


    nmapDefaultArgs = "-sV -sC -T5"
    nmapArgsList = []


    ProgArguments = sys.argv
    programName = ProgArguments[0]
    ProgArguments.remove(programName)
    IP = ProgArguments[0]




    if noIP == False:
        os.system("nmap {} > /root/temp/nmapscan".format(IP))
        scan = open("/root/temp/nmapscan", "r")
        ports = []
        scrapPorts = 0
        for line in scan:
            currentLine = line.strip()
            if scrapPorts == 1:
                if "MAC" in currentLine:
                    placeholder = 0
                    break
                else:
                    split = currentLine.split("/")
                    ports.append(split[0])
            if "PORT" in currentLine:
                scrapPorts = 1
        printPorts = ""
        for port in ports:
            printPorts = printPorts + port + " "
        print("Scanning ports: {}".format(printPorts))

        os.system("rm /root/temp/nmapscan")
        portsWComma = ""
        for port in ports:
            portsWComma = portsWComma + port + ","
        portsWComma = portsWComma[:-1]
        os.system("nmap {} -p {} {}".format(nmapDefaultArgs, portsWComma, IP))