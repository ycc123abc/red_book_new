import json
class Base64Generator:
    def __init__(self) -> None:
        self.c = [
            "Z", "m", "s", "e", "r", "b", "B", "o", "H", "Q", "t", "N", "P", "+", "w", "O",
            "c", "z", "a", "/", "L", "p", "n", "g", "G", "8", "y", "J", "q", "4", "2", "K",
            "W", "Y", "j", "0", "D", "S", "f", "d", "i", "k", "x", "3", "V", "T", "1", "6",
            "I", "l", "U", "A", "F", "M", "9", "7", "h", "E", "C", "v", "u", "R", "X", "5"
        ]

    def triplet_to_base64(self, e):
        return self.c[(e >> 18) & 63] + self.c[(e >> 12) & 63] + self.c[(e >> 6) & 63] + self.c[e & 63]

    def encode_utf8(self, text):
        import urllib.parse
        encoded = urllib.parse.quote(text, safe='')
        result = []
        i = 0
        while i < len(encoded):
            if encoded[i] == '%':
                result.append(int(encoded[i+1:i+3], 16))
                i += 3
            else:
                result.append(ord(encoded[i]))
                i += 1
        return result

    def b64_encode(self, data):
        json_str = json.dumps(data, separators=(",", ":"))
        data_bytes = self.encode_utf8(json_str)
        result = []
        chunk_size = 16383
        
        # 处理完整块
        for i in range(0, len(data_bytes) - 2, 3):
            if i % chunk_size == 0 and i > 0:
                # 分块处理逻辑保持不变
                pass
            triplet = (data_bytes[i] << 16) + (data_bytes[i + 1] << 8) + data_bytes[i + 2]
            result.append(self.triplet_to_base64(triplet))

        # 处理尾部
        remainder = len(data_bytes) % 3
        if remainder == 1:
            a = data_bytes[-1]
            result.append(self.c[a >> 2] + self.c[(a << 4) & 63] + "==")
        elif remainder == 2:
            a = (data_bytes[-2] << 8) + data_bytes[-1]
            result.append(self.c[a >> 10] + self.c[(a >> 4) & 63] + self.c[(a << 2) & 63] + "=")

        return ''.join(result)

