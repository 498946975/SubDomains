import re
import time

time1 = time.time()


######函数功能:能够提取ip地址，并且去重################
def read_file(input_file_name, output_file_name):
    _fLog = open(input_file_name)
    sep = '\n'
    ip_list = []
    for each in _fLog:
        ip = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', str(each), re.S)
        ip_list.append(ip[0])
    # 列表去重:通过set方法进行处理
    ids = list(set(ip_list))
    print("共解析ip个数:%s " % len(ids))
    ##写出数据到本地
    # 设置输出文件路径
    out = open(output_file_name, "a")
    # out.write("ip" + sep)
    for each in ids:
        print(each)
        out.write(each + sep)
    ##关闭连接
    out.close()
    _fLog.close()
    print("ip提取完毕~~")


####主函数################
if __name__ == '__main__':
    input_file_name = "/Users/oliver/Documents/PyCharm/subDomainsBrute/aegis-info.txt"
    output_file_name = "/Users/oliver/Documents/PyCharm/subDomainsBrute/out-aegis.txt"
    read_file(input_file_name, output_file_name)
    time2 = time.time()
    print(u'总共耗时：' + str(time2 - time1) + 's')
