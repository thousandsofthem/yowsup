from .env import YowsupEnv
import base64
import hashlib


class AndroidYowsupEnv(YowsupEnv):
    _SIGNATURE = "MIIDMjCCAvCgAwIBAgIETCU2pDALBgcqhkjOOAQDBQAwfDELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFDASBgNV" \
        "BAcTC1NhbnRhIENsYXJhMRYwFAYDVQQKEw1XaGF0c0FwcCBJbmMuMRQwEgYDVQQLEwtFbmdpbmVlcmluZzEUMBIGA1UEAxMLQnJ" \
        "pYW4gQWN0b24wHhcNMTAwNjI1MjMwNzE2WhcNNDQwMjE1MjMwNzE2WjB8MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5" \
        "pYTEUMBIGA1UEBxMLU2FudGEgQ2xhcmExFjAUBgNVBAoTDVdoYXRzQXBwIEluYy4xFDASBgNVBAsTC0VuZ2luZWVyaW5nMRQwEg" \
        "YDVQQDEwtCcmlhbiBBY3RvbjCCAbgwggEsBgcqhkjOOAQBMIIBHwKBgQD9f1OBHXUSKVLfSpwu7OTn9hG3UjzvRADDHj+AtlEm" \
        "aUVdQCJR+1k9jVj6v8X1ujD2y5tVbNeBO4AdNG/yZmC3a5lQpaSfn+gEexAiwk+7qdf+t8Yb+DtX58aophUPBPuD9tPFHsMCN" \
        "VQTWhaRMvZ1864rYdcq7/IiAxmd0UgBxwIVAJdgUI8VIwvMspK5gqLrhAvwWBz1AoGBAPfhoIXWmz3ey7yrXDa4V7l5lK+7+jr" \
        "qgvlXTAs9B4JnUVlXjrrUWU/mcQcQgYC0SRZxI+hMKBYTt88JMozIpuE8FnqLVHyNKOCjrh4rs6Z1kW6jfwv6ITVi8ftiegEkO" \
        "8yk8b6oUZCJqIPf4VrlnwaSi2ZegHtVJWQBTDv+z0kqA4GFAAKBgQDRGYtLgWh7zyRtQainJfCpiaUbzjJuhMgo4fVWZIvXHaS" \
        "HBU1t5w//S0lDK2hiqkj8KpMWGywVov9eZxZy37V26dEqr/c2m5qZ0E+ynSu7sqUD7kGx/zeIcGT0H+KAVgkGNQCo5Uc0koLRW" \
        "YHNtYoIvt5R3X6YZylbPftF/8ayWTALBgcqhkjOOAQDBQADLwAwLAIUAKYCp0d6z4QQdyN74JDfQ2WCyi8CFDUM4CaNB+ceVXd" \
        "KtOrNTQcc0e+t"

    _MD5_CLASSES = "WtoJ21Y6+22aerd95Bq3Ng=="
    _KEY = "eQV5aq/Cg63Gsq1sshN9T3gh+UUp0wIw0xgHYT1bnCjEqOJQKCRrWxdAe2yvsDeCJL+Y4G3PRD2HUF7oUgiGo8vGlNJOaux26k+A2F3hj8A="


    _VERSION = "2.20.108"
    _OS_NAME = "Android"
    _OS_VERSION = "8.0.0"

    # Samsung Galaxy J7 2017 SM-J730F (8.1.0):Samsung:SM-J730F=samsung/j7y17ltexx/j7y17lte:8.1.0/M1AJQ/J730FXXU3BRK2:user/release-keys__2018-11-01
    # Samsung Galaxy S8 Plus SM-G955F (8.0.0):Samsung:SM-G955F=samsung/dream2ltexx/dream2lte:8.0.0/R16NW/G955FXXU1CRC7:user/release-keys
    # Samsung Galaxy S9 Plus SM-G965F (8.0.0):Samsung:SM-G965F=samsung/star2ltexx/star2lte:8.0.0/R16NW/G965FXXU1ARCC:user/release-keys
    # Samsung Galaxy S9 SM-G960F (8.0.0):Samsung:SM-G960F=samsung/starltexx/starlte:8.0.0/R16NW/G960FXXU1ARCC:user/release-keys

    # _DEVICE_NAME = "j7y17lte"
    # _DEVICE_NAME = "dream2lte"
    _DEVICE_NAME = "starlte"
    _MANUFACTURER = "samsung"
    _BUILD_VERSION = "starltexx-user 8.0.0 R16NW G960FXXU1ARCC release-keys"
    # _BUILD_VERSION = "dream2ltexx-user 8.0.0 R16NW G955FXXU1CRC7 release-keys"
    # _BUILD_VERSION = "j7y17ltexx-user 8.0.0 M1AJQ J730FXXU3BRK2 release-keys"
    _AXOLOTL = True

    def getVersion(self):
        return self.__class__._VERSION

    def getOSName(self):
        return self.__class__._OS_NAME

    def getOSVersion(self):
        return self.__class__._OS_VERSION

    def getDeviceName(self):
        return self.__class__._DEVICE_NAME

    def getBuildVersion(self):
        return self.__class__._BUILD_VERSION

    def getManufacturer(self):
        return self.__class__._MANUFACTURER

    def isAxolotlEnabled(self):
        return self.__class__._AXOLOTL

    def getToken(self, phoneNumber):
        keyDecoded = bytearray(base64.b64decode(self.__class__._KEY))
        sigDecoded = base64.b64decode(self.__class__._SIGNATURE)
        clsDecoded = base64.b64decode(self.__class__._MD5_CLASSES)
        data = sigDecoded + clsDecoded + phoneNumber.encode()

        opad = bytearray()
        ipad = bytearray()
        for i in range(0, 64):
            opad.append(0x5C ^ keyDecoded[i])
            ipad.append(0x36 ^ keyDecoded[i])
        hash = hashlib.sha1()
        subHash = hashlib.sha1()
        try:
            subHash.update(ipad + data)
            hash.update(opad + subHash.digest())
        except TypeError:
            subHash.update(bytes(ipad + data))
            hash.update(bytes(opad + subHash.digest()))
        result = base64.b64encode(hash.digest())
        return result
