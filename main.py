import os


def rename(path_url):
    # 获取该目录下所有文件，存入列表中
    fileList = os.listdir(path_url)

    old_name = input('请输入要替换的字段：')
    print('ok...')
    new_name = input('请输入替换后的字段：')

    count = 0
    for i in fileList:
        if old_name in i:
            count += 1
            # 设置新文件名
            newname = i.replace(old_name, new_name)
            os.rename(os.sep.join([path_url, i]), os.sep.join([path_url, newname]))  # 用os模块中的rename方法对文件改名
            print(i, '======>', newname)
    print('\nok...  %d个文件修改完成' % count)
    con = input('==========\n输入任意字符退出程序，继续修改请按"1"：')
    return con


if __name__ == '__main__':
    while True:
        try:
            if rename(path_url=input('请复制文件路径粘贴至此处：')) == '1':
                rename(path_url=input('请复制文件路径粘贴至此处：'))
            else:
                break
        except:
            print('文件路径错误，请检查！')
