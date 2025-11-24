const crypto = require('crypto');
function encodeUtf8(e) {
    for (var a = encodeURIComponent(e), r = [], c = 0; c < a.length; c++) {
        var d = a.charAt(c);
        if ("%" === d) {
            var s = parseInt(a.charAt(c + 1) + a.charAt(c + 2), 16);
            r.push(s),
            c += 2
        } else
            r.push(d.charCodeAt(0))
    }
    return r
}

function b64Encode(e) {
    for (var a, r = e.length, d = r % 3, s = [], f = 16383, u = 0, l = r - d; u < l; u += f)
        s.push(encodeChunk(e, u, u + f > l ? l : u + f));
    return 1 === d ? (a = e[r - 1],
    s.push(c[a >> 2] + c[a << 4 & 63] + "==")) : 2 === d && (a = (e[r - 2] << 8) + e[r - 1],
    s.push(c[a >> 10] + c[a >> 4 & 63] + c[a << 2 & 63] + "=")),
    s.join("")
}


function stringToMD5(input) {
    return crypto.createHash('md5').update(input, 'utf8').digest('hex');
}

function seccore_signv2(e, a) {
    var c=e+JSON.stringify(a);
    var d = stringToMD5(c)
    var s = window.mnsv2(c, d)
    var f = {
        x0: '4.2.6',
        x1: "xhs-pc-web",
        x2: "window",
        x3: s,
        x4: "obhject"
    };
    return "XYS_" + b64Encode(encodeUtf8(JSON.stringify(f)))
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

x_s=seccore_signv2(e,s)