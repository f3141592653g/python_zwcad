from ctypes import *
import os
import ftplib
import confModule


class myFtp:

    ftp = ftplib.FTP()
    cm = confModule.ReadConfig()

    def __init__(self, port=21):
        self.host = self.cm.get('FTP_value', 'host')
        self.username = self.cm.get('FTP_value', 'username')
        self.password = self.cm.get('FTP_value', 'password')
        self.ftp.connect(self.host, port)
        self.ftp.encoding = 'gbk'

    def Login(self):
        self.ftp.login(self.username, self.password)


    def download_File(self,local_file,remote_file):# 指定单个文件下载
        file_handler = open(local_file, 'wb')
        self.ftp.retrbinary('RETR ' + remote_file, file_handler.write) # 下载ftp文件
        # ftp.delete（filename） # 删除ftp服务器上的文件
        file_handler.close()
        return True

    def DownLoadFileTree(self, LocalDir, RemoteDir):  # 下载整个目录下的文件
        print("远程文件夹remoteDir:", RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        remote_names = self.ftp.nlst()
        print("远程文件目录文件内容：", remote_names)
        for file in remote_names:
            Local = os.path.join(LocalDir, file)
            print("正在下载", self.ftp.nlst(file))
            if file.find(".") == -1:
                if not os.path.exists(Local):
                    os.makedirs(Local)
                self.DownLoadFileTree(Local, file)
            else:
                self.download_File(Local, file)
        self.ftp.cwd("..")
        return

    def close(self):
        self.ftp.quit()


if __name__ == "__main__":
    ftp = myFtp()
    ftp.Login()
    ftp.download_File('D:/ZWCAD 2022', '/maozhu0/AutoTestResult/20210701/Result')
    # ftp.DownLoadFileTree('D:/ZWCAD 2022/Result', '/maozhu0/AutoTestResult/20210701/Result')#从目标目录下载到本地目录d盘
    ftp.close()
    print("下载完成")