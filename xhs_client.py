import json
import requests
import re 
from urllib.parse import urlparse
from encrypt import x_b3_traceid_generator,x_s_generator,x_xray_traceid_generator,xsc_generator,x_t_generator
class XhsClient:
    def __init__(self):
        self.session = requests.Session()

    def get_uri(self, url,query_params):
        """
        从URL中提取API路径部分
        
        Args:
            url (str): 完整的API URL
            
        Returns:
            str: 提取的API路径
        """
        # 解析URL
        parsed_url = urlparse(url)
        
        # 提取路径部分
        path = parsed_url.path
        
        # 如果路径以/api开头，则返回完整路径
        if path.startswith('/api/'):
            pass
        else:
            # 否则尝试匹配/api/xxxxxx模式
            match = re.search(r'(/api/[^?\s]*)', path)
            if match:
                path= match.group(1)
        uri=path+json.dumps(query_params, separators=(',', ':'))
        print("uri:",uri)
        return uri

    def request_get(self, url, query_params,a1):
        uri=self.get_uri(url,query_params)

        b3_trace_id=x_b3_traceid_generator.get_b3_trace_id()
        x_s=x_s_generator.get_xs(uri,a1)
        e = 'I38rHdgsjopgIvesdVwgIC+oIELmBZ5e3VwXLgFTIxS3bqwErFeexd0ekncAzMFYnqthIhJeSnMDKutRI3KsYorWHPtGrbV0P9WfIi/eWc6eYqtyQApPI37ekmR6QL+5Ii6sdneeSfqYHqwl2qt5B0DBIx+PGDi/sVtkIxdsxuwr4qtiIhuaIE3e3LV0I3VTIC7e0utl2ADmsLveDSKsSPw5IEvsiVtJOqw8BuwfPpdeTFWOIx4TIiu6ZPwrPut5IvlaLbgs3qtxIxes1VwHIkumIkIyejgsY/WTge7eSqte/D7sDcpipedeYrDtIC6eDVw2IENsSqtlnlSuNjVtIvoekqt3cZ7sVo4gIESyIhEqHnquIxhnqz8gIkIfoqwkICZWG73sdlOeVPw3IvAe0fged0MKIi5s3Mr52utAIiKsidvekZNeTPt4nAOeWPwEIvSLce6eduwAL9KsfPwZI3SrIxE5Luwwaqw+rekhZANe1MNe0Pw9ICNsVLoeSbIFIkosSr7sVnFiIkgsVVtMIiudqqw+tqtWI30e3PwIIhoe3ut1IiOsjut3wutnsPwXICclI3Ir27lk2I5e1utCIES/IEJs0PtnpYIAO0JeYfD1IErPOPtKoqw3I3OexqtWQL5eizKsVbmwIhNs6B7sTuwGpuwOICJeWVwiIkgexjRwIveeSo/efVtSI37skqwuNdQPIhHpICgefYoskjvsfl7ekuwmIEMTIvrOzqweI3ZSIkgei/iEGUNsjVwaIirZyVtuHIgeWSgsSuwpcI=='
        xsc=xsc_generator.get_xsc(a1,e)
        x_xray_trace_id=x_xray_traceid_generator.get_xray_trace_id()
        x_t=x_t_generator.get_x_t()
        print("x_xray_trace_id:",x_xray_trace_id)
        print("x_s:",x_s)
        print("x_xray_trace_id:",x_xray_trace_id)
        print("x_t:",x_t)
        print("x_s_common:",xsc, "length:",len(xsc))
        print("x_b3_trace_id:",b3_trace_id)
        headers = {
            "sec-ch-ua-platform": "\"Windows\"",
            "xy-direction": "40",
            "Referer": "https://www.xiaohongshu.com/",
            "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
            "x-xray-traceid": x_xray_trace_id,
            "sec-ch-ua-mobile": "?0",
            "X-t": x_t,
            "x-b3-traceid": b3_trace_id,
            "X-S-Common": xsc,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "X-s": x_s
        }
        data = json.dumps(query_params, separators=(',', ':'))
        response = self.session.post(url, headers=headers, data=data)

        print(response.text)
        print(response)