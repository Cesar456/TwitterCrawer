# encoding=utf-8

err_log = open('C:\Users\Cesar\Desktop\err.txt', "r+")

err_log.writelines('错误\n')
err_log.writelines('正确'+'\n')
err_log.writelines(str(123)+'\n')

x = err_log.readlines(1)[0]
print x
