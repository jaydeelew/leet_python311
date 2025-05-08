# 468. Validate IP Address
# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address,
# "IPv6" if IP is a valid IPv6 address address or "Neither" if IP is not a correct IP of any type.
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255
# and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses
# while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where: 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f')
# and upper-case English letters ('A' to 'F'). Leading zeros are allowed in xi.
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334"
# are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334"
# are invalid IPv6 addresses.


def validIPAddress(queryIP: str) -> str:
    def valid_v4_part(part: str):
        return True if part.isdecimal() and part == str(int(part)) and 0 <= int(part) <= 255 else False

    def valid_v6_part(part: str):
        return (
            True
            if 1 <= len(part) <= 4 and all(c in "0123456789abcdefABCDEF" for c in part) and 0x0 <= int(part, 16) <= 0xFFFF
            else False
        )

    valid_ipv4 = valid_ipv6 = False

    split_ipv4 = queryIP.split(".")
    if len(split_ipv4) == 4:
        if all(valid_v4_part(part) for part in split_ipv4):
            valid_ipv4 = True

    split_ipv6 = queryIP.split(":")
    if len(split_ipv6) == 8:
        if all(valid_v6_part(part) for part in split_ipv6):
            valid_ipv6 = True

    if not valid_ipv4 and not valid_ipv6:
        return "Neither"
    elif valid_ipv4:
        return "IPv4"
    else:
        return "IPv6"


# queryIP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".

# queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# # Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".

# queryIP = "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.

# queryIP = "01.01.01.01"
# Output: "Neither"

# queryIP = "2001:0db8:85a3:00000:0:8A2E:0370:7334"
# Output: "Neither"

# queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# # Output: "IPv6"

queryIP = "20EE:FGb8:85a3:0:0:8A2E:0370:7334"

print(validIPAddress(queryIP))
