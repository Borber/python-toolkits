from contextlib import closing
from toolkits.ip_proxies import get_proxies
import requests
import os
import time
import filetype

# proxies = {
#     "http": "socks5://127.0.0.1:1080",
#     'https': 'socks5://127.0.0.1:1080'
# }


# 文件下载器
def down_load(file_url, file_full_name, now_count, all_count, headers):
    if os.path.exists(file_full_name):
        return
    # 开始下载图片
    with closing(requests.get(file_url, headers=headers, proxies=get_proxies(), stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers.get('content-length'))  # 文件总大小
        data_count = 0  # 当前已传输的大小
        with open(file_full_name, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                done_block = int((data_count / content_size) * 50)
                data_count = data_count + len(data)
                now_jd = (data_count / content_size) * 100
                print("\r %s：[%s%s] %d%% %d/%d" % ('***'+file_full_name[-10:], done_block * '█', ' ' * (50 - 1 - done_block), now_jd, now_count, all_count), end=" ")

    # 下载完图片后获取图片扩展名，并为其增加扩展名
    # file_type = filetype.guess(file_full_name)
    # os.rename(file_full_name, file_full_name + '.' + file_type.extension)

