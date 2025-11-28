import requests
import json

from xhs_client import XhsClient

url = "https://edith.xiaohongshu.com/api/sns/web/v1/homefeed"
data = {
    "cursor_score": "",
    "num": 39,
    "refresh_type": 1,
    "note_index": 34,
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
    "need_filter_image": False
}
a1='19ab462768dbnostuyyqujnz1j5fyrt8egmfrrr1n50000440764'
xhsclent=XhsClient()
xhsclent.request_get(url,data,a1)