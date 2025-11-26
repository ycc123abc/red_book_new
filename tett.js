
// const str = '99483c';
// const encoder = new TextEncoder();
// const uint8Array = encoder.encode(str);
// console.log(uint8Array);






function convertToUint32Array(byteArray, includeLength) {
    const byteLength = byteArray.length;
    const arraySize = Math.floor(byteLength / 4) + ((byteLength % 4) !== 0 ? 1 : 0);
    
    let resultArray;
    if (includeLength) {
        resultArray = new Uint32Array(arraySize + 1);
        resultArray[arraySize] = byteLength;
    } else {
        resultArray = new Uint32Array(arraySize);
    }
    
    for (let i = 0; i < byteLength; ++i) {
        const wordIndex = Math.floor(i / 4);
        const bytePosition = i % 4;
        resultArray[wordIndex] |= byteArray[i] << (bytePosition * 8);
    }
    
    return resultArray;
}

function convertFromUint32Array(uint32Array, hasLength) {
    const arrayLength = uint32Array.length;
    let byteLength = arrayLength << 2; // 等同于 arrayLength * 4
    
    if (hasLength) {
        const storedLength = uint32Array[arrayLength - 1];
        // 验证存储的长度是否有效
        if (storedLength < (byteLength -= 4) - 3 || storedLength > byteLength) {
            return null;
        }
        byteLength = storedLength;
    }
    
    // 创建指定长度的 Uint8Array
    const resultArray = new Uint8Array(byteLength);
    
    // 将 Uint32Array 中的数据按字节提取到 Uint8Array 中
    for (let i = 0; i < byteLength; ++i) {
        const wordIndex = i >> 2; // 等同于 Math.floor(i / 4)
        const bytePosition = 3 & i; // 等同于 i % 4
        resultArray[i] = uint32Array[wordIndex] >> (bytePosition << 3); // 等同于 >> (bytePosition * 8)
    }
    
    return resultArray;
}
unit32=convertToUint32Array([119, 104, 96, 41, 186, 177, 85, 93, 236, 87, 199, 151, 179, 40, 41, 41, 232, 170, 38, 48, 0, 0, 0, 0, 1, 0, 0, 0, 160, 0, 0, 0, 39, 1, 0, 0, 15, 114, 252, 167, 33, 171, 73, 247, 52, 49, 57, 97, 98, 52, 54, 50, 55, 54, 56, 100, 98, 110, 111, 115, 116, 117, 121, 121, 113, 117, 106, 110, 122, 49, 106, 53, 102, 121, 114, 116, 56, 101, 103, 109, 102, 114, 114, 114, 49, 110, 53, 48, 48, 48, 48, 52, 52, 48, 55, 54, 52, 10, 120, 104, 115, 45, 112, 99, 45, 119, 101, 98, 1, 201, 248, 172, 102, 103, 201, 182, 129, 98, 95, 7, 68, 251, 132, 21],true)
console.log(unit32)
unit8=convertFromUint32Array(unit32,false)
console.log(unit8)

function customBase64Encode(data, charset) {
    // 扩展字符集
    charset = charset + "FTKdeNOwxWXYZap89+/A4UVLhijkl63G";
    
    const dataLength = data.length;
    const result = [];
    
    // 每3个字节为一组进行处理
    for (let i = 0; i < dataLength; i += 3) {
        // 获取当前组的三个字节，不足的用0补齐
        const byte1 = data[i];
        const byte2 = i + 1 < dataLength ? data[i + 1] : 0;
        const byte3 = i + 2 < dataLength ? data[i + 2] : 0;
        
        // 将三个字节组合成一个24位的数字
        const combined = byte1 << 16 | byte2 << 8 | byte3;
        
        // 将24位数字分割成4个6位的块
        const chunks = [
            combined >>> 18 & 63,
            combined >>> 12 & 63,
            combined >>> 6 & 63,
            combined & 63
        ];
        
        // 计算需要填充的等号数量
        const paddingCount = dataLength - i >= 3 ? 0 : 3 - (dataLength - i);
        
        // 将块转换为对应字符
        for (let j = 0; j < 4 - paddingCount; j++) {
            result.push(charset.charAt(chunks[j]));
        }
        
        // 添加填充等号
        for (let k = 0; k < paddingCount; k++) {
            result.push("=");
        }
    }
    
    return result.join("");
}

console.log(customBase64Encode(unit8,'MfgqrsbcyzPQRStuvC7mn501HIJBo2DE'))