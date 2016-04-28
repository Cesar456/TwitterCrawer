# encoding=utf-8
err_log = open('C:\Users\Cesar\Desktop\err.txt', 'a')

err_log.writelines('错误\n')
err_log.writelines('正确'+'\n')
err_log.writelines(str(123)+'\n')