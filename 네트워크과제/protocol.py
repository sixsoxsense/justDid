'''
마지막 작성일 2020년 06월 06일
'''
String = ""
serviceTypeDict = {"00": "nomal",
                   "01": "accept",
                   "10": "accept",
                   "11": "confused"}
protocolDict = {"01": "ICMP",
                "06": "TCP",
                "11": "UDP"}
flagsDict = {
    "0": " reversed : 0,\n Don’t Fragment? : 0 / fragment,\n More? : 0 / No more fragments",
    "2": " reversed : 0,\n Don’t Fragment? : 0 / fragment,\n More? : 1 / more fragments",
    "4": " reversed : 0,\n Don’t Fragment? : 1 / Unable to fragment,\n More? : 0 / No more fragments",
    "6": " reversed : 0,\n Don’t Fragment? : 1 / Unable to fragment,\n More? : 1 / more fragments"
}
urgentDict = {"0": "0 / Not urgent",
              "1": "1 / urgent"}
ackDict = {"0": "0 / Unacknowlegment",
           "1": "1 / Acknowlegment"
           }
pushDict = {"0": "0 / Normal",
            "1": "1 / Push"
            }
ResetDict = {"0": "0 / Normal",
             "1": "1 / Reset"
             }
synDict = {"0": "0 / Not Connection Setup",
           "1": "1 / Connection Setup"
           }
finDict = {"0": "0 / Not Connection Release",
           "1": "1 / Connection Release"
           }
tcpPortDict = {"1": "well-known port: TCPMUX",
               "7": "well-known port: ECHO",
               "9": "well-known port: DISCARD",
               "13": "well-known port: DAYTIME",
               "17": "well-known port: QOTD",
               "19": "well-known port: CHARGEN",
               "20": "well-known port: FTP 데이터포트",
               "21": "well-known port: FTP 제어포트",
               "22": "well-known port: SSH",
               "23": "well-known port: 텔넷",
               "24": "well-known port: 개인메일 시스템",
               "25": "well-known port: SMTP",
               "37": "well-known port: TIME",
               "53": "well-known port: DNS",
               "70": "well-known port: 고퍼",
               "79": "well-known port: Finger",
               "80": "well-known port: HTTP",
               "88": "well-known port: 커베로스 -",
               "109": "well-known port: POP2",
               "110": "well-known port: POP3",
               "111": "well-known port: RPC",
               "113": "well-known port: ident",
               "119": "well-known port: NNTP",
               "139": "well-known port: 넷바이오스",
               "143": "well-known port: IMAP4",
               "179": "well-known port: BGP",
               "194": "well-known port: IRC",
               "389": "well-known port: LDAP",
               "443": "well-known port: HTTPS",
               "445": "well-known port: Microsoft-DS",
               "465": "well-known port: SSL 위의 SMTP",
               "515": "well-known port: LPD",
               "540": "well-known port: UUCP",
               "542": "well-known port: Commerce Applications",
               "587": "well-known port: SMTP",
               "591": "well-known port: 파일메이커",
               "631": "well-known port: 인터넷 프린팅 프로토콜",
               "636": "well-known port: SSL 위의 LDAP (암호화된 전송)",
               "666": "well-known port: id 소프트웨어의 둠 멀티플레이어 게임",
               "873": "well-known port: rsync 파일 동기화 프로토콜",
               "981": "well-known port: SofaWare Technologies Checkpoint Firewall-1",
               "990": "well-known port: SSL 위의 FTP",
               "992": "well-known port: SSL 위의 Telnet",
               "993": "well-known port: SSL 위의 IMAP4",
               "995": "well-known port: SSL 위의 POP3"
               }
udpPortDict = {
    "0": "well-known port: 예약",
    "7": "well-known port: ECHO",
    "9": "well-known port: DISCARD",
    "13": "well-known port: DAYTIME ",
    "19": "well-known port: CHARGEN ",
    "37": "well-known port: TIME",
    "49": "well-known port: TACACS",
    "53": "well-known port: DNS",
    "67": "well-known port: BOOTP 서버",
    "68": "well-known port: BOOTP 클라이언트",
    "69": "well-known port: TFTP",
    "80": "well-known port: HTTP",
    "111": "well-known port: RPC",
    "123": "well-known port: NTP",
    "161": "well-known port: SNMP agent",
    "162": "well-known port: SNMP manager",
    "445": "well-known port: Microsoft-DS SMB 파일 공유",
    "514": "well-known port: syslog",
    "542": "well-known port: Commerce Applications"
}
icmpTypeDict = {"03": "03 / Destination Unreachable",  # 목적지 도달불가
                "04": "04 / Source Quench",  # 발신억제
                "05": "05 / Redirect",  # 재지정
                "11": "11 / Time Exceeded",  # 시간초과
                "12": "12 / Parameter Problem",  # 매개변수 문제
                "00": "00 / Echo Reply",  # 에코응당
                "08": "08 / Echo Request",  # 에코 요청
                "09": "09 / Router Advertisement",  # 라우터 광고
                "10": "10 / Router Solicitation"  # 라우터 간청
                }
icmpType03Dict = {"00": "00 / Network Unreachable",
                  "01": "01 / Host Unreachable",
                  "10": "10 / Protocol Unreachable",
                  "11": "11 / Port Unreachable"
                  }
operationDict = {"0001": "Request",
                 "0010": "Reply"}


def strToIP(String):  # dc 5f e9 ab -> 220.95.233.171
    bytes = ["".join(x) for x in zip(*[iter(String)] * 2)]
    bytes = [int(x, 16) for x in bytes]
    IP = ".".join(str(x) for x in bytes)
    return IP


def strToMAC(String):
    bytes = ["".join(x) for x in zip(*[iter(String)] * 2)]
    MAC = ":".join(str(x) for x in bytes)
    return MAC


def checkCast(String, flag):
    if flag == "des":
        print("ETHERNET:")
        print(" Destination Address: " + strToMAC(String), end="")

    elif flag == "source":
        print("ETHERNET:")
        print(" Source Address: " + strToMAC(String), end="")

    if String == "ffffffffffff":
        return print(" / broadcast")
    elif sliceBin(String)[3] == "0":
        return print(" / unicast")
    elif sliceBin(String)[3] == "1":
        return print(" / multicast")
    else:
        print("프레임오류")
        exit(-1)


def sliceBin(String):
    slicing = ["".join(x) for x in zip(*[iter(String)] * 1)]
    return format(int(slicing[1]), '04b')


def ETHERNET(String):
    destiAddress = String[0:12]
    sourceAddress = String[12:24]
    ethernetType = String[24:28]
    checkCast(destiAddress, "des")
    checkCast(sourceAddress, "source")
    return ethernetType


def IP(String):
    VER = String[0]
    HLEN = String[1]
    serviceType = String[2:4]
    TotalLength = String[4:8]
    Identy = String[8:12]
    flag = String[12]
    offset = String[13:16]
    TTL = String[16:18]
    Protocol = String[18:20]
    checksum = String[20:24]
    sourceAddress = String[24:32]
    destiAddress = String[32:40]
    print("IP:")
    print(" Version: " + VER)
    print(" Header Length: " + HLEN + " / ", int(HLEN, 16) * 4, "bytes")
    print(" Service Type: ", serviceType, " / ", serviceTypeDict[serviceType])
    print(" Total Length: " + TotalLength + " / ", int(TotalLength, 16), "bytes : ",
          (int(TotalLength, 16) - (int(HLEN, 16) * 4)), "payloadByte")
    print(" Identification: " + Identy + " / ", int(HLEN, 16) * 4, "bytes")
    print(" Flags: " + flag + " / ", format(int(flag, 16), '04b'))
    print(flagsDict[flag])
    print(" Offset: " + offset + " / ", 1 + int(offset, 2) * 8, "번째 프레임")
    print(" TTL: " + TTL + " / ", int(TTL, 16), "hops")
    print(" Protocol: " + Protocol + " / " + protocolDict[Protocol])
    print(" Checksum: " + checksum)
    print(" Source Address: " + sourceAddress + " / ", strToIP(sourceAddress))
    print(" Destination Address: " + destiAddress + " / ", strToIP(destiAddress))
    return Protocol


def TCP(String):
    sourcePort = String[0:4]
    destiPort = String[4:8]
    sequenceN = String[8:16]
    ackN = String[16:24]
    headerLength = String[24:25]
    controlBits = String[26:28]
    windowSize = String[28:32]
    checksum = String[32:36]
    urgentPoint = String[36:40]
    option = String[40:]
    print("TCP:")
    print(" Source Port: ", end='')
    printTcpPort(sourcePort)
    print(" Destination Port: ", end='')
    printTcpPort(destiPort)
    print(" Sequence number: ", sequenceN)
    print(" Ack number: ", ackN)
    print(" Header Length: ", headerLength, " / ", int(headerLength, 16) * 4, "bytes : option",
          int(headerLength, 16) * 4 - int(len(option) / 2), "bytes")
    print(" Control Bits: ", controlBits, " / ", controlbitFunc(format(int(controlBits, 16), "08b")))
    print(" Window Size: ", windowSize, " / ", int(windowSize, 16), "bytes")
    print(" Checksum: ", checksum)
    print(" Urgent Point: ", urgentPoint, " / ")
    print(" Option:", option, " / ", len(option) / 2, "bytes")


def UDP(String):
    sourcePort = String[0:4]
    destiPort = String[4:8]
    totalLength = String[8:12]
    checksum = String[12:16]
    print("UDP:")
    print(" Source Port: ", end='')
    printUdpPort(sourcePort)
    print(" Destination Port: ", end='')
    printUdpPort(destiPort)
    print(" Total Length: " + totalLength + " / ", int(totalLength, 16), "bytes")
    print(" Checksum: ", checksum)


def ICMP(String):
    Type = String[0:2]
    Code = String[2:4]
    checksum = String[4:8]
    id = String[8:12]
    sequence = String[12:16]
    data = String[16:]
    print("ICMP:")
    print(" Type: ", Type)
    if Type == "03":
        print(" Code: ", icmpType03Dict[Code])
    else:
        print(" Code: ", Code)
    print(" Checksum: ", checksum)
    print(" Id: ", id)
    print(" Sequence N: ", sequence)
    print(" Data: ", data)


def ARP(String):
    HWType = String[0:4]
    protocolType = String[4:8]
    HWSize = String[8:10]
    protocolSize = String[10:12]
    operation = String[12:16]
    sourceMacAddress = String[16:28]
    sourceIPAddress = String[28:36]
    targetMacAddress = String[36:48]
    targetIPAddress = String[48:56]
    print("ARP:")
    print(" H/WType: ", HWType, " / Ethernet")
    print(" ProtocolType: ", protocolType, " / IP")
    print(" H/W Length: ", HWSize, " / ", int(HWSize, 16) * 8, "bits")
    print(" Protocol Length: ", protocolSize, " / ", int(protocolSize, 16) * 8, "bits")
    print(" Operation: ", operation, " / ", operationDict[operation])
    if bin(int(sourceMacAddress, 16))[8] == "0":
        print(" Sender MAC Address: ", strToMAC(sourceMacAddress), " / Unicast")
    elif sourceMacAddress == "ffffffffffff":
        print(" Sender MAC Address: ", strToMAC(sourceMacAddress), " / Broadcast")
    print(" Sender IP Address: ", sourceIPAddress, " / ", strToIP(sourceIPAddress))
    if operation == "01":
        print(" Target MAC Address: ", strToMAC(targetMacAddress), " / Unknown MAC")
    elif operation == "10":
        print(" Target MAC Address: ", strToMAC(targetMacAddress), " / Request MAC")
    print(" Target IP Address: ", targetIPAddress, " / ", strToIP(targetIPAddress))


def Frame(String):
    eType = ETHERNET(String[:28])
    if eType == "0800":  # IP인경우
        print(" Type: " + eType + "/ IP")
        protocol = IP(String[28:])
        if protocol == "06":
            TCP(String[68:])
        elif protocol == "01":
            ICMP(String[68:])
        elif protocol == "11":
            UDP(String[68:])
        else:
            print("IP 프로토콜오류 및 미구현한 부분")
    elif eType == "0806":  # arp인경우
        print(" Type: " + eType + "/ ARP")
        ARP(String[28:])
    else:
        print("입력프레임오류")


def controlbitFunc(String):
    Urgent = String[-1]
    AcK = String[-2]
    Push = String[-3]
    Reset = String[-4]
    Syn = String[-5]
    Fin = String[-6]
    print("  -Urgent: ", urgentDict[Urgent])
    print("  -AcK: ", ackDict[AcK])
    print("  -Push: ", pushDict[Push])
    print("  -Reset: ", ResetDict[Reset])
    print("  -Syn: ", synDict[Syn])
    print("  -Fin: ", finDict[Fin])


def printTcpPort(String):
    portN = int(String, 16)
    if str(portN) in tcpPortDict.keys():
        print(String, " / ", portN, tcpPortDict[str(portN)])
    elif 1024 <= portN and portN <= 49151:
        print(String, " / ", portN, "registered port")
    elif 49152 <= portN and portN <= 65535:
        print(String, " / ", portN, "dynamic port")
    else:
        print(String, " / ", portN, "well-known port")


def printUdpPort(String):
    portN = int(String, 16)
    if str(portN) in udpPortDict.keys():
        print(String, " / ", portN, udpPortDict[str(portN)])
    elif 1024 <= portN and portN <= 49151:
        print(String, " / ", portN, "registered port")
    elif 49152 <= portN and portN <= 65535:
        print(String, " / ", portN, "dynamic port")
    else:
        print(String, " / ", portN, "well-known port")


def main():
    String = str(input("프레임을입력하시오\n"))
    Frame(String)


if __name__ == '__main__':
    main()
