import lab1_5
import os

md = lab1_5.Edit1(['1\n', 'b\n', 'c\n', '1\n', '2\n', '3\n', 'abc\n'])
md.insert(2, 'qwer')
print(md.get_md())
# print(lab1_5.Translate.split_string("load D:\dcmt\code\vscode\software_lab\lab1\test.txt"))

# path = r"D:\dcmt\code\vscode\software_lab\lab1\test.txt"
# md = lab1_5.Md(path)
# print(md.md_path, md.history_path, md.stats_path)
# print(path)
# path.replace('\\', '/')
# history_path = os.path.join(os.getcwd(), "history.txt").replace('\\', '/')
# print(history_path)
# history_path = history_path.replace('\\', '/')
# print(history_path)
# print(path)
# print(os.path.abspath(path))
# print(os.path.dirname(path))
# print(os.path.join(os.path.dirname(path), "history.txt"))
# print(os.path.basename(path))
# a = os.path.split(path)[1]
# print(a)
# print(os.path.getatime(path))
# print(os.path.getmtime(path))
# print(os.path.getctime(path))
# print(os.path.normcase(path))

class A:
    def __init__(self):
        self.ob_list = []
        self.data = None

    def add_ob(self, ob):
        self.ob_list.append(ob)

    def notify(self):
        for ob in self.ob_list:
            ob.update(self.data)

    def do_sth(self, data):
        self.data = data
        self.notify()

class B:
    def __init__(self):
        self.data = None

    def update(self, data):
        self.data = data

    def rcv(self):
        print(self.data)


class C:
    def __init__(self):
        self.data = None

    def update(self, data):
        self.data = data

    def rcv(self):
        print(self.data)

# a = A()
# b = B()
# c = C()
# a.add_ob(b)
# a.add_ob(c)
#
# a.do_sth(1)
# b.rcv()
# c.rcv()
# a.do_sth(2)
# b.rcv()
# c.rcv()
# class NewEdit(lab1_2.Edit):
#     def insert(self, *args):
#         print("neweditbegin")
#         super().insert(*args)
#         print("neweditend")
#
# fileop = lab1_4.FileOp2()
# # edit = NewEdit()
# edit = lab1_4.Edit1()
# display = lab1_4.Display()
# translate = lab1_4.Translate()
# log = lab1_4.Log()
# statistics = lab1_4.Statistics()


# lab1_4.md = ["# 新的标题",
# "# 我的书签",
# "## 学习资源",
# "## 新的子标题",
# "### 编程",
# "* 新的文本"]

# display.dir_tree("# 新的标题")
# md = ["# 新的标题",
# "# 我的书签",
# "## 学习资源",
# "## 新的子标题",
# "### 编程"]


# def printtree(md):
#     for line in md:
#         index = line.count('#')
#         # print(index)
#         for j in range(index):
#             print('├──', end='')
#         print(line[index+1:])

# def printtree(md):
#     for i in range(len(md)):
#         index = md[i].count('#')
#         # print(index)
#         if i == 0:
#             print('├──', end='')
#             print(md[0][index+1:])
#         if i >0:
#             if md[i-1].count('#') == md[i].count('#'):
#                 for j in range(md[i].count('#')-1):
#                     print('\t', end='')
#                 print('├──', end='')
#                 print(md[i][index+1:])
#         for j in range(index):
#             print('├──', end='')
#         print(md[i][index+1:])

# def printtree(md):
#     maxrow, maxcol = len(md), 0
#     for line in md:
#         maxcol = max(maxcol, line.count('#'))
#     res = [["\t" for j in range(maxcol + 1)]for i in range(maxrow)]
#     # for i in range(maxrow):
#     #     for j in range(maxcol):
#     for i in range(maxrow):
#         res[i][md[i].count('#')] = md[i].split(' ', 1)[1]
#     for i in range(maxrow):
#         for j in range(md[i].count('#')):
#             up, right, down = False, False, False
#             if any(item in md[:i][j] for item in ["", "└── ", "├── "]):
#                 up = True
#             if any(item in md[i][:] for item in ["", "└── ", "├── "]):
#                 right = True
#             if any(item in md[:i][j] for item in ["", "└── ", "├── "]):
#                 down = True
    # print(res)
    # for i in range(maxrow):
    #     for j in range(maxcol):
    #         print(res[i][j], end='')
    #     print("\n")

# printtree(md)


# a = [["\t" for j in range(3)]for i in range(4)]
# print(a)

# print(statistics.fduration(50000000))

# timestats = ["12 znd", "34 inwe", "67 inqw"]
# timelist = []
# duration = 1
# for line in timestats:
#     if line.split()[0] == "34":
#         newtime = duration
#         timelist.append("ac" + " " + str(newtime))
#     else:
#         timelist.append(line)

# class B:
#     def __init__(self):
#         pass
#
#     def f3(self):
#         print("this is f3")

# a = A()
# a.f2()

# class A:
#     def __init__(self):
#         self.x = 1
#         self.y = self.x * 3 + 5
#
#     def f1(self):
#         print("this id f1")
#
#     def f2(self):
#         print("this is f2")
#         print(self.y)
#
#
# class C:
#     def __init__(self, z):
#         self.z = z
#         self.a = A()
#         self.z += self.a.x
#
#     def f4(self):
#         print("this is c")
#         print(self.z)
#         self.a.f2()
# # a = A()
# # a.f2()
# # b = B()
# # b.f3()
# c = C(45)
# c.f4()


# path = os.getcwd()
# print(path)
# path = path[:path.rfind('\\')] + "\\test.txt"
# print(path)
# a = "D:\dcmt\code\vscode\software_lab\lab1\test.txt"
# D:\dcmt\code\vscode\software_lab\lab1\test.txt.txt
# print(repr(a))
# print(os.path.dirname(a))
# print(os.path.join(os.path.dirname(a), "history.txt"))
# with open(a, 'r+') as f:
#     print(f.read())

# f = open(a, 'r')
# print(f.read())

# a = input()
# print(a)
# f = open(a, "r")
# print(f.read())
# a = 'D:\\dcmt\\code\\vscode\\software_lab\\lab1\\test.txt'.replace('\\', '/')
# with open(a, 'r') as f:
#     print(f.read())

# if __name__ == "__main__":
#     while True:
#         content = input()
#         eval(translate.trans(content))
#         log.track(content)
#         print(lab1_3.md)

# md1 = ['1', '2', '3']
# md = lab1_5.Edit1(md1)
# md.insert(2, 'aaa')
# md.delete(1)
# print(md.md)
#
# md.undo()
# print(md.md)
# md.redo()
# print(md.md)

# if __name__ == "__main__":
#     while True:
#

# class Test:
#     def __init__(self, a=None):
#         self.a = a
#
#     def prt(self):
#         print(self.a)
#
#
# test = Test()
# test.prt()
# print(id(test))
# test = Test(1)
# test.prt()
# print(id(test))
