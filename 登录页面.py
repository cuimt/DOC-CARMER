import tkinter 
from tkinter import messagebox

import pymssql
connect = pymssql.connect('DESKTOP-2MRTG5S', '', '', 'SCT')  #建立连接
if connect:
    print("连接成功!") 

cursor = connect.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行

connect.commit()  #提交
cursor.close()   #关闭游标
connect.close()  #关闭连接

class Login(object): 
 def __init__(self): 
  # 创建主窗口,用于容纳其它组件 
  self.root = tkinter.Tk() 
  # 给主窗口设置标题内容 
  self.root.title("影视资源管理系统(离线版)") 
  self.root.geometry('658x320') 
  #运行代码时记得添加一个gif图片文件，不然是会出错的
  self.canvas = tkinter.Canvas(self.root, height=350, width=658)#创建画布 
  self.image_file = tkinter.PhotoImage(file='welcome_1.gif')#加载图片文件 '
  self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)#将图片置于画布上 
  self.canvas.pack(side='top')#放置画布（为上端） 
  self.label_account = tkinter.Label(self.root, text='选择文件名: ') 
   
  self.label_password = tkinter.Label(self.root, text='选择背包容量: ') 
   
  self.input_account = tkinter.Entry(self.root, width=30) 
 
  self.input_password = tkinter.Entry(self.root,width=30) 
  
  self.login_button = tkinter.Button(self.root, command = self.backstage_interface, text = "继续", width=10) 
   
  self.siginUp_button = tkinter.Button(self.root, command = self.siginUp_interface, text = "退出", width=10) 
 # 完成布局 
 def gui_arrang(self): 
  self.label_account.place(x=40, y= 170) 
  self.label_password.place(x=40, y= 195) 
  self.input_account.place(x=135, y=170) 
  self.input_password.place(x=135, y=195) 
  self.login_button.place(x=180,y=235) 
  self.siginUp_button.place(x=280, y=235) 
 # 进入注册界面 
 def siginUp_interface(self): 
  # self.root.destroy() 
  tkinter.messagebox.showinfo(title='遗传算法求解折扣背包问题', message='进入注册界面')  
 # 进行登录信息验证 
 def backstage_interface(self): 
  account = self.input_account.get().ljust(10," ") 
  password = self.input_password.get().ljust(10," ") 
  #对账户信息进行验证，普通用户返回user，管理员返回master，账户错误返回noAccount，密码错误返回noPassword 
  verifyResult = verifyAccount.verifyAccountData(account,password) 
  if verifyResult=='master': 
   self.root.destroy() 
   tkinter.messagebox.showinfo(title='遗传算法求解折扣背包问题', message='进入文件选择界面') 
  elif verifyResult=='user': 
   self.root.destroy() 
   tkinter.messagebox.showinfo(title='遗传算法求解折扣背包问题', message='进入数据界面') 
  elif verifyResult=='noAccount': 
   tkinter.messagebox.showinfo(title='遗传算法求解折扣背包问题', message='该文件不存在请重新输入!') 
  elif verifyResult=='noPassword': 
   tkinter.messagebox.showinfo(title='遗传算法求解折扣背包问题', message='背包容量错误请重新输入!') 
def main(): 
 # 初始化对象 
 L = Login() 
 # 进行布局 
 L.gui_arrang() 
 # 主程序执行 
 tkinter.mainloop() 
if __name__ == '__main__': 
 main()

