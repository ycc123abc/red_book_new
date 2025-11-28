import random
import time
from typing import List
from .base64_generator import Base64Generator
import hashlib
class XHSSignatureGenerator:
    """小红书签名生成器"""
    def __init__(self):
        self.t = 4294967295
        self.initial_list = [119, 104, 96, 41]
        self.fixed_suffix = [179, 40, 41, 41]
        self.fixed_web = [10, 120, 104, 115, 45, 112, 99, 45, 119, 101, 98]
        self.fixed_bytes = [248, 172, 102, 103, 201, 182, 129, 98, 95, 7, 68, 251, 132, 21]
        self.base64_charset = 'MfgqrsbcyzPQRStuvC7mn501HIJBo2DE'
        self.encryption_key = 'e6483ca2a1eed5e3'
        self.timestamp = int(time.time() * 1000)
        self.random_int = int(self.t * random.random())
    
    def _convert_to_uint32_array(self, n: List[int], r: bool) -> List[int]:
        """将字节数组转换为32位无符号整数数组"""
        e = len(n)
        a = e >> 2
        
        if (3 & e) != 0:
            a += 1
        
        if r:
            t = [0] * (a + 1)
            t[a] = e
        else:
            t = [0] * a
        
        for o in range(e):
            t[o >> 2] |= n[o] << ((3 & o) << 3)
        
        return t
    
    def _uint32_array_to_uint8_array(self, uint32_arr: List[int]) -> List[int]:
        """将32位无符号整数列表转换为8位无符号整数列表"""
        byte_length = len(uint32_arr) * 4
        uint8_arr = [0] * byte_length
        
        for i in range(len(uint32_arr)):
            value = uint32_arr[i]
            offset = i * 4
            uint8_arr[offset] = (value >> 0) & 0xFF
            uint8_arr[offset + 1] = (value >> 8) & 0xFF
            uint8_arr[offset + 2] = (value >> 16) & 0xFF
            uint8_arr[offset + 3] = (value >> 24) & 0xFF
        
        return uint8_arr
    
    def _base64_encode(self, data: List[int], charset: str) -> str:
        """自定义Base64编码"""
        full_charset = charset + "FTKdeNOwxWXYZap89+/A4UVLhijkl63G"
        result = []
        
        for e in range(0, len(data), 3):
            o = data[e]
            l = data[e + 1] if e + 1 < len(data) else 0
            n = data[e + 2] if e + 2 < len(data) else 0
            
            u = o << 16 | l << 8 | n
            F = [
                (u >> 18) & 63,
                (u >> 12) & 63,
                (u >> 6) & 63,
                u & 63
            ]
            
            padding = 0 if len(data) - e >= 3 else 3 - (len(data) - e)
            
            for f in range(4 - padding):
                result.append(full_charset[F[f]])
            
            for _ in range(padding):
                result.append("=")
        
        return "".join(result)
    
    def _decrypt_data(self, data: List[int], key_str: str) -> List[int]:
        """数据解密"""
        class OptimizedDecryptor:
            def __init__(self):
                self.const = 1013904243
                self.n_mapping = {4: 3, 5: 0, 6: 1}
            
            def single_decrypt(self, m, x, a, idx, n, key, sign=1):
                n_val = self.n_mapping.get(n, n)
                k = (n_val ^ idx) % 4
                number_7 = ((a >> 5) ^ (x << 2)) + ((x >> 3) ^ (a << 4))
                number_12 = (m ^ x) + (a ^ key[k])
                result = number_7 ^ number_12
                return result
            
            def get_iv(self, e):
                return e / self.const, e + self.const
            
            def decrypt(self, r, key):
                length = len(r)
                last_idx = length - 1
                a = r[last_idx]
                e = 0
                iterations = 6 + 52 // length
                
                for _ in range(iterations):
                    n, e = self.get_iv(e)
                    n_int = int(n)
                    
                    for idx in range(last_idx):
                        x = r[idx + 1]
                        r[idx] = (r[idx] + self.single_decrypt(e, x, a, idx, n_int, key)) & 0xFFFFFFFF
                        a = r[idx]
                    
                    x = r[0]
                    r[last_idx] = (r[last_idx] + self.single_decrypt(e, x, a, last_idx, n_int, key)) & 0xFFFFFFFF
                    a = r[last_idx]
                
                return r
        
        # 准备解密密钥
        key_uint8 = [ord(char) for char in key_str]
        key = self._convert_to_uint32_array(key_uint8, False)
        
        # 准备数据
        data_uint32 = self._convert_to_uint32_array(data, True)
        
        # 解密
        decryptor = OptimizedDecryptor()
        decrypted_data = decryptor.decrypt(data_uint32.copy(), key)
        
        return self._uint32_array_to_uint8_array(decrypted_data)
    

    def generate_signature(self, qarams: str, md5_str: str, a1: str) -> str:
        """
        生成签名
        
        Args:
            qarams: 请求参数
            md5_str: MD5字符串
            a1: 设备标识
            
        Returns:
            生成的签名
        """
        result_list = self.initial_list.copy()
        
        # 步骤1: 生成随机字节
        arr = [self.random_int & 255, self.random_int >> 8 & 255, 
               self.random_int >> 16 & 255, self.random_int >> 24 & 255]
        result_list.extend(arr)

        # 步骤2: 时间戳相关计算
        self.t+=1
        integer_part = int(self.timestamp / self.t)
        fractional_part = (self.timestamp / self.t) - integer_part
        init_num = int(fractional_part * self.t)
        
        # 计算第二个数字列表
        num_list_second = []
        right_move = 0
        result = 0

        for i in range(4):
            a = init_num >> right_move
            b = a & 255
            num_list_second.append(b)
            if i == 0:
                c = 0
                d = b
            else:
                c += b
                d = c & 255
            right_move += 8
            result = d


        # 计算第四个数字
        fourth_num = 0
        for i in range(4):
            init_num = integer_part
            first_num = init_num & 255
            second_num = init_num + result
            third_num = second_num & 255
            fourth_num = third_num + 1

        # 添加计算结果
        result_list.append(fourth_num ^ 41)
        for index, value in enumerate(num_list_second):
            if index == 0:
                continue
            result_list.append(value ^ 41)
        
        # 步骤3: 添加固定后缀
        result_list.extend(self.fixed_suffix)
        
        # 步骤4: 添加时间相关字节
        init_part = int((0.18809002079069614) * (self.t + 1))
        for i in range(8):
            result_num = init_part & 255
            init_part = init_part >> 8
            result_list.append(result_num)

        # 步骤5: 添加固定值1
        init_part = 1
        for i in range(4):
            result_num = init_part & 255
            init_part = init_part >> 8
            result_list.append(result_num)

        # 步骤6: 添加随机数
        init_part = random.randint(150, 200)
        for i in range(4):
            result_num = init_part & 255
            init_part = init_part >> 8
            result_list.append(result_num)

        # 步骤7: 添加参数长度
        init_part = len(qarams)
        for i in range(4):
            result_num = init_part & 255
            init_part = init_part >> 8
            result_list.append(result_num)

        # 步骤8: 添加MD5相关字节
        for i in range(0, len(md5_str), 2):
            pair = md5_str[i:i+2]
            result_list.append(int(pair, 16) ^ result_list[4])
            if i == 14:
                break

        # 步骤9: 添加设备标识和固定web标识
        a1_byte_array = list(a1.encode('utf-8'))
        result_list = result_list + [52] + a1_byte_array + self.fixed_web

        # 步骤10: 添加固定字节
        result_list.extend([1, result_list[4] ^ 115] + self.fixed_bytes)

        # 步骤11: 数据解密
        
        decrypted_data = self._decrypt_data(result_list, self.encryption_key)
        
        # 步骤12: Base64编码
        base64_result = self._base64_encode(decrypted_data, self.base64_charset)
        
        return f"mns0201_{base64_result}"


def get_xs(uri,a1):
    md5_obj = hashlib.md5()
    md5_obj.update(uri.encode('utf-8'))
    md5_str = md5_obj.hexdigest()
    print("md5_str",md5_str)
    generator = XHSSignatureGenerator()
    signature = generator.generate_signature(uri, md5_str, a1)
    data={
            "x0": "4.2.6",
            "x1": "xhs-pc-web", 
            "x2": "Windows",
            "x3": signature,
            "x4": "object"
        }
    print("signature",signature)
    base64generator=Base64Generator()
    result=base64generator.b64_encode(data)
    return "XYS_"+result



# 使用示例
if __name__ == "__main__":
    print(xsGenerator().b64_encode('{"s0":5,"s1":"","x0":"1","x1":"4.2.6","x2":"Windows","x3":"xhs-pc-web","x4":"4.86.0","x5":"19ab462768dbnostuyyqujnz1j5fyrt8egmfrrr1n50000440764","x6":"","x7":"","x8":"I38rHdgsjopgIvesdVwgIC+oIELmBZ5e3VwXLgFTIxS3bqwErFeexd0ekncAzMFYnqthIhJeSnMDKutRI3KsYorWHPtGrbV0P9WfIi/eWc6eYqtyQApPI37ekmR6QL+5Ii6sdneeSfqYHqwl2qt5B0DBIx+PGDi/sVtkIxdsxuwr4qtiIhuaIE3e3LV0I3VTIC7e0utl2ADmsLveDSKsSPw5IEvsiVtJOqw8BuwfPpdeTFWOIx4TIiu6ZPwrPut5IvlaLbgs3qtxIxes1VwHIkumIkIyejgsY/WTge7eSqte/D7sDcpipedeYrDtIC6eDVw2IENsSqtlnlSuNjVtIvoekqt3cZ7sVo4gIESyIhEqHnquIxhnqz8gIkIfoqwkICZWG73sdlOeVPw3IvAe0fged0MKIi5s3Mr52utAIiKsidvekZNeTPt4nAOeWPwEIvSLce0eSVwCLfosDuwPI3ErIxE5Luwwaqw+rekhZANe1MNe0Pw9ICNsVLoeSbIFIkosSr7sVnFiIkgsVVtMIiudqqw+tqtWI30e3PwIIhoe3ut1IiOsjut3wutnsPwXICclI3Ir27lk2I5e1utCIES/IEJs0PtnpYIAO0JeYfD1IErPOPtKoqw3I3OexqtWQL5eizKsVbmwIhNs6B7sTuwGpuwOICJeWVwiIkgexjRwIveeSo/efVtSI37skqwuNdQPIhHpICgefYoskjvsfl7ekuwmIEMTIvrOzqweI3ZSIkgei/iEGUNsjVwaIirZyVtuHIgeWSgsSuwpcI==","x9":-1843477756,"x10":0,"x11":"normal"}'))    
    # # 创建生成器实例
    # generator = XHSSignatureGenerator()
    # # 准备参数
    # qarams='/api/sns/web/v1/homefeed{"cursor_score": "","num": 39,"refresh_type": 1,"note_index": 33,"unread_begin_note_id": "","unread_end_note_id": "","unread_note_count": 0,"category": "homefeed_recommend","search_key": "","need_num": 14,"image_formats": ["jpg","webp","avif"],"need_filter_image": false}'
    # md5_str='b5c8461d9b11f34d56d087d95db75a6b'
    # a1='19ab462768dbnostuyyqujnz1j5fyrt8egmfrrr1n50000440764'
    # get_xs(qarams,a1)

    