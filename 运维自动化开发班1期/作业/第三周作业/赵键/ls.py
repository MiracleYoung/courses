import pwd,os,grp,stat,time,sys

def get_file(args,file_path):
    lst = []
    if args == '-al':
        for file in os.listdir(file_path):
            # print(file)
            stat_info = os.stat(file_path+"/"+file)
            #权限
            mode = stat_info.st_mode
            M = oct(stat.S_IMODE(mode))

            #inode nlink
            ino = stat_info.st_nlink
            #user group
            uid = stat_info.st_uid
            gid = stat_info.st_gid
            user = pwd.getpwuid(uid)[0]
            group = grp.getgrgid(gid)[0]
            #size
            size = stat_info.st_size

            #最后修改时间
            mtime = stat_info.st_mtime
            localtime = time.localtime(mtime)
            strTime = time.strftime("%m-%d %H:%M", localtime)

            # print("oct: ", M)
            # print("ino: ", ino)
            # print("user: ", user)
            # print("group: ", group)
            # print("size: ", size)
            # print("strTime: ", strTime)
            # print("filename:",file)
            result = str(M)+" "+str(ino)+" "+str(user)+" "+str(group)+" "+str(size)+" "+str(strTime)+" "+file
            print(result)


if __name__ == '__main__':
    # 获取参数
    args1 = sys.argv[1]
    args2 = sys.argv[2]
    get_file(args1,args2)
