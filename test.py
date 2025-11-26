import requests
import json


headers = {
    "sec-ch-ua-platform": "\"Windows\"",
    "xy-direction": "40",
    "Referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "x-xray-traceid": "cd5eedcfbc110d5af29b3aef8c5fce9e",
    "sec-ch-ua-mobile": "?0",
    "X-t": "1764121878431",
    "x-b3-traceid": "0b6b1771cc04306a",
    "X-S-Common": "2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0c1Pjh9HjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHFN0W9N0ZjNsQh+aHCH0rEGnHF+0H7+0YDGfE6q7zM2gSl4nk120bx+n8Eqdch8n4T8dQUq0b1+/ZIPeZF+eZ7+0cjNsQh+jHCHjHVHdW7H0ijHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafp/JDMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpH9LLI3+LSk+d+DJfRSL98lnLYl49IUqgcMc0mrJFShtMmozBD6qM8FyFSh8o+h4g4U+obFyLSi4nbQz/+SPFlnPrDApSzQcA4SPopFJeQmzBMA/o8Szb+NqM+c4ApQzg8Ayp8FaDRl4AYs4g4fLomD8pzBpFRQ2ezLanSM+Skc47Qc4gcMag8VGLlj87PAqgzhagYSqAbn4FYQy7pTanTQ2npx87+8NM4L89L78p+l4BL6ze4AzB+IygmS8Bp8qDzFaLP98Lzn4AQQzLEAL7bFJBEVL7pwyS8Fag868nTl4e+0n04ApfuF8FSbL7SQyrLFaeSl4LShyBEl20YdanTQ8fRl49TQcMkgz9cAq9zV/9pnLoqAag8m8/mf89pDPrMNanDMqA++q0LU4gzmanSNq9SD4fp3nDESpbmF+BEm/9pgLo4bag8//BPI+fpDpd4m/BEwqFzM47QQPMzUagYb+LlM474Yqgq3qfp3ybkm/fLl/LESPbm7wLSe/d+n/BRSL9QQzDS3J7+/q04ApfEByLS387+npdz+anSM8obl4UTFqgzga/PI8/+c4FSQyBRSP7pFPLSk/7+x4gcA47pFJd+c4MYQc9+Va/+Qq0H7JBVUa/pSPgpFcFSbLURQzLkAPbmFJdm8aLbOPrkSnn8rPLSbqSmOLozNJ7b7PFDA/9phqgzgLLIM8nS0cgPAqBY7anY6qAPE/7PA4gzAGMm7GLSead+gLoqManSd8nTSqLlQcFTSyfc6q98c4epQ2e4A2op7zezTzBEQynHFagYw8/P6Po+LGg8A8rSS8nTc4FQQyb+haL+B+aRc4F+QcF4iaLpt8/8//nDhzfzAydp7arSbLLRI4gqlPDlBOaHVHdWEH0iT+0r9PeLE+0WhNsQhP/Zjw0ZVHdWlPaHCHfE6qfMYJsQR",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "X-s": "XYS_2UQhPsHCH0c1Pjh9HjIj2erjwjQhyoPTqBPT49pjHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQTJdPIPAZlg98yGLTlGAD6wLba/9p6/Dk1LjR9p7zi+nTwtFMawepnJaRx2bSxzFDUyfEf+7iF8BQQ/eGILBldPf8rLgSI+bpsyDSoJ/Z9zeplLSkMqrMp/Dz+adpHLnp1+dQp49pNPrTEpeqEydW9JFbQ2Du74pzLNFRmPrkHaMY/4eYPzpL7Pbz+c9EIqMQCLDkcpnbLP9ltarT/Jfznnfl0yLLIaSQQyAmOarGROaHVHdWFH0ijJ9Qx8n+FHdF="
}
url = "https://edith.xiaohongshu.com/api/sns/web/v1/homefeed"
data = {
    "cursor_score": "",
    "num": 39,
    "refresh_type": 1,
    "note_index": 33,
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
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)