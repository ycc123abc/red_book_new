import hashlib
import json

def calculate_md5_hash(input_string):
    """
    使用hashlib库计算MD5哈希值
    """
    # 创建MD5对象
    md5_hash = hashlib.md5()
    
    # 更新哈希对象
    md5_hash.update(input_string.encode('utf-8'))
    
    # 获取十六进制摘要
    hex_digest = md5_hash.hexdigest()
    
    # 转换为4个32位整数
    digest_bytes = md5_hash.digest()
    integers = struct.unpack('<4I', digest_bytes)  # 小端序
    
    return list(integers)

# 测试代码
input_data = '/api/sns/web/v1/homefeed{"cursor_score":"1.7639723078830085E9","num":39,"refresh_type":3,"note_index":145,"unread_begin_note_id":"","unread_end_note_id":"","unread_note_count":0,"category":"homefeed_recommend","search_key":"","need_num":14,"image_formats":["jpg","webp","avif"],"need_filter_image":false}'

import struct
result = calculate_md5_hash(input_data)
print("MD5哈希结果:", result)
print("期望输出: [-850486555, 915399730, -873678503, 411682820]")