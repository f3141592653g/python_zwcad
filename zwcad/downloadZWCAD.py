
import downloadFile


def get_path():
    # coding=utf8
    ftp = downloadFile.myFtp()
    ftp.Login()
    ftp.downloadFile('D:/ZWCAD 2022', '/maozhu0/AutoTestResult/20210701/Result', 'VersionList.csv')  # 从目标目录下载到本地目录d盘
    ftp.close()
    with open("D:/ZWCAD 2022/VersionList.csv") as csvfile:
        mLines = csvfile.readlines()
    targetLine = mLines[-1]
    path_1 = targetLine.split(',')[0]
    path_2 = targetLine.split(',')[1]
    print(path_1,path_2)

    if 'win32'.upper() in path_2.upper():
        total_path = path_1 + '/' + path_2 + '/' + 'win32' + '/' + 'bin'
        print(total_path)
        ftp = downloadFile.myFtp()
        ftp.Login()
        ftp.DownLoadFileTree('D:/ZWCAD', total_path)#从目标目录下载到本地目录d盘
        ftp.close()

    elif 'x64'.upper() in path_2.upper():
        total_path = path_1 + '/' + path_2 + '/' + 'x64' + '/' + 'bin'
        print(total_path)
        ftp = downloadFile.myFtp()
        ftp.Login()
        ftp.DownLoadFileTree('D:/ZWCAD', total_path)  # 从目标目录下载到本地目录d盘
        ftp.close()
    else:
        print("不存在win32或x64文件")


if __name__ == '__main__':
    get_path()