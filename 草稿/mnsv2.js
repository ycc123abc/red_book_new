
const crypto = require('crypto');
function stringToMD5(input) {
    return crypto.createHash('md5').update(input, 'utf8').digest('hex');
}
function mnsv2(c, d){

    t=4294967295 
    // ranodm_int=int(Math.random()*t)
    ranodm_int=parseInt(t*0.6146058558034981);
    let arr=new Uint8Array([ranodm_int&255,ranodm_int>>8&255,ranodm_int>>16&255,ranodm_int>>24&255])
    console.log(arr);
    textdecoder=new TextEncoder()
    console.log(c)
    c_text=textdecoder.encode(c)
    console.log(c_text)
    return 
}
function seccore_signv2(e, a) {
    var c=e+JSON.stringify(a);
    var d = stringToMD5(c)
    var s = mnsv2(c, d)
    // var f = {
    //     x0: '4.2.6',
    //     x1: "xhs-pc-web",
    //     x2: "window",
    //     x3: s,
    //     x4: "object"
    // };
    // return "XYS_" + b64Encode(encodeUtf8(JSON.stringify(f)))
    //     }
}

e='/api/sns/web/v1/homefeed'
s={
    "cursor_score": "1.7639723078830085E9",
    "num": 39,
    "refresh_type": 3,
    "note_index": 145,
    "unread_begin_note_id": "",
    "unread_end_note_id": "",
    "unread_note_count": 0,
    "category": "homefeed_recommend",
    "search_key": "",
    "need_num": 14,
    "image_formats": [
        "jpg",
        "webp",
        "avif"
    ],
    "need_filter_image": false
}

seccore_signv2(e,s)