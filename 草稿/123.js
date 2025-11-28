function anonymous(t, r) {
    // 如果 t 是字符串，则通过 window._765b4a22808933082686525e8ad1892e 转换为其他形式
    if (typeof t === "string") {
        t = window._765b4a22808933082686525e8ad1892e(t);
    }

    // 如果 r 是字符串，则通过 window._765b4a22808933082686525e8ad1892e 转换为其他形式
    if (typeof r === "string") {
        r = window._765b4a22808933082686525e8ad1892e(r);
    }

    // 如果 t 为 null 或长度为 0，直接返回 t
    if (t == null || t.length === 0) {
        return t;
    }

    // 执行嵌套调用并返回结果
    return window._07a4982b8029aaf48c4b4d95bc74bdb9(
        window._0d480d3713ddee1557ab2e623700ed7b(
            window._1c9208bcfb2bf7494ca7ffbb22911f9d(t, true),
            window._1c9208bcfb2bf7494ca7ffbb22911f9d(
                r,
                false
            )
        ),
        false
    );
}


const str = 'e6483ca2a1eed5e3';
const uint8Array = new Uint8Array(Array.from(str).map(char => char.charCodeAt(0)));
function convertToUint32Array(n, r) {
    var t, e = n.length, a = e >> 2;
    
    // 如果长度不是4的倍数，增加一个单位
    if ((3 & e) != 0) {
        ++a;
    }
    
    // 根据参数r决定是否添加长度信息
    if (r) {
        t = new Uint32Array(a + 1);
        t[a] = e;  // 在末尾存储原始长度
    } else {
        t = new Uint32Array(a);
    }
    
    // 将输入数组n的每个字节按小端序打包到Uint32Array中
    for (var o = 0; o < e; ++o) {
        t[o >> 2] |= n[o] << ((3 & o) << 3);
    }
    
    return t;
}
unit321=convertToUint32Array(uint8Array,false)
console.log(unit32)
t=[
  119,104,96,
  41,220,
  136,
  242,
  84,
  174,
  16,
  216,
  235,
  179,
  40,
  41,
  41,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  1,
  0,
  0,
  0,
  186,
  0,
  0,
  0,
  27,
  0,
  0,
  0,
  172,
  193,
  161,
  109,
  244,
  43,
  75,
  235,
  52,
  49,
  57,
  57,
  97,
  52,
  50,
  55,
  54,
  101,
  51,
  100,
  122,
  109,
  56,
  104,
  107,
  113,
  118,
  121,
  116,
  117,
  108,
  113,
  109,
  120,
  116,
  104,
  97,
  109,
  106,
  114,
  102,
  103,
  103,
  101,
  121,
  113,
  102,
  49,
  100,
  55,
  51,
  48,
  48,
  48,
  48,
  51,
  49,
  48,
  55,
  55,
  54,
  10,
  120,
  104,
  115,
  45,
  112,
  99,
  45,
  119,
  101,
  98,
  1,
  175,
  248,
  172,
  102,
  103,
  201,
  183,
  129,
  98,
  95,
  7,
  68,
  251,
  132,
  21,
]
unit322=convertToUint32Array(t,true)
console.log(unit32)



