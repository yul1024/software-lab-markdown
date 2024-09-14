import time
import os

# md_path = ""
# history_path = ""
# stats_path = ""
# md = []
# bp = []
# start_time = 0
# end_time = 0


class FileOp:
    """文件相关操作"""
    def __init__(self, md_path):
        self.md_path = md_path
        self.md = []
        self.load(self.md_path)

    def load(self, md_path):
        """加载文件，如果没有就新创建"""
        # global md_path, history_path, stats_path
        # md_path = address.replace('\\', '/')
        # history_path = md_path[:md_path.rfind('/')] + r"/history.txt"
        # stats_path = md_path[:md_path.rfind('/')] + r"/stats.txt"
        try:
            with open(md_path, 'r+', encoding='utf-8') as f:
                # global md
                self.md = f.readlines()
        except FileNotFoundError:
            with open(md_path, 'w') as f:
                pass

    def save(self):
        """保存文件，会覆盖原有的文件，但已经保存了原本的md，所以无影响"""
        with open(self.md_path, 'w', encoding='utf-8') as f:
            for line in self.md:
                f.write(line)

    def get_md(self):
        return self.md

    def set_md(self, md):
        self.md = md


class Edit:
    """编辑文件"""
    def __init__(self, md):
        self.md = md

    def insert(self, *args):
        """由于python不支持函数重载，这里用可变参数实现"""
        # self.rcd()  # 执行前会进行备份
        # print("editing")
        # global md
        if len(args) == 1:
            self.md.insert(len(self.md), str(args[0]) + "\n")
        elif len(args) == 2:
            self.md.insert(int(args[0]) - 1, str(args[1]) + "\n")

    def append_head(self, content):
        """用insert实现"""
        self.insert(1, content)

    def append_tail(self, content):
        """用insert实现"""
        self.insert(content)

    def delete(self, content):
        # self.rcd()  # 执行前会进行备份
        if isinstance(content, int):
            self.md.pop(content - 1)
        elif isinstance(content, str):
            self.md.remove(content + '\n')

    def get_md(self):
        return self.md

    # def rcd(self):
    #     """备份实现的方式是复制"""
    #     # global md, bp
    #     self.bp = self.md[:]

    # def undo(self):
    #     # global md, bp
    #     self.md, self.bp = self.bp, self.md
    #
    # def redo(self):
    #     # global md, bp
    #     # md, bp = bp, md
    #     self.undo()


# class FileOp1(FileOp):
#     """会有撤销功能的文件操作"""
#     def __init__(self, md_path):
#         super().__init__(md_path)
#
#     def load(self, address):
#         super().load(address)
#         Record.rcd()
#
#     def save(self):
#         super().save()
#         Record.rcd()


class Edit1(Edit):
    def __init__(self, md):
        super().__init__(md)
        self.bp = self.md
        # self.record = Record(self.md)

    def rcd(self):
        """备份实现的方式是复制"""
        # global md, bp
        self.bp = self.md[:]

    def undo(self):
        # global md, bp
        self.md, self.bp = self.bp, self.md

    def redo(self):
        # global md, bp
        # md, bp = bp, md
        self.undo()

    def insert(self, *args):
        self.rcd()
        super().insert(*args)

    def delete(self, content):
        self.rcd()
        super().delete(content)


class Edit2(Edit1):
    def __init__(self, md):
        super().__init__(md)
        self.ob_list = []

    def add_ob(self, ob):
        self.ob_list.append(ob)

    def notify(self):
        for ob in self.ob_list:
            ob.set_md(self.md)

    def insert(self, *args):
        super().insert(*args)
        self.notify()

    def delete(self, content):
        super().delete(content)
        self.notify()

    def undo(self):
        super().undo()
        self.notify()


class Display:
    """展示md，以打印的方式"""
    def __init__(self, md):
        self.md = md

    def list(self):
        # global md
        for line in self.md:
            print(line, end='')

    def list_tree(self):
        self.dir_tree(self.md[0])

    def dir_tree(self, *args):
        if len(args) == 0:
            self.dir_tree(md[0])
        else:
            index1 = self.md.index(args)
            number = self.md[index1].find('#')
            temp = ""
            for i in range(number):
                temp += '#'
            index2 = 0
            for i in range(index1 + 1, len(self.md)):
                index2 = self.md.index(temp)
            if index2 == -1:
                # print(index1, index2)
                self.print_tree(self.md[index1:])
            else:
                # print(index1, index2)
                self.print_tree(self.md[index1: index2 - 1])

    def print_tree(self, md):
        for line in md:
            index = line.count('#')
            # print(index)
            for j in range(index):
                print('├──', end='')
            print(line[index + 1:])
        # maxrow, maxcol = len(md), 0
        # for line in md:
        #     maxcol = max(maxcol, line.count('#'))
        # res = [["\t" for j in range(maxcol + 1)]for i in range(maxrow)]
        # # for i in range(maxrow):
        # #     for j in range(maxcol):
        # for i in range(maxrow):
        #     res[i][md[i].count('#')] = md[i].split(' ', 1)[1]
        # for i in range(maxrow):
        #     for j in range(md[i].count('#')):
        #         up, right, down = False, False, False
        #         if any(item in md[:i][j] for item in ["", "└── ", "├── "]):
        #             up = True
        #         if any(item in md[i][:] for item in ["", "└── ", "├── "]):
        #             right = True
        #         if any(item in md[:i][j] for item in ["", "└── ", "├── "]):
        #             down = True

    def set_md(self, md):
        self.md = md


class Translate:
    """并不是原本文档里的需求，但是很重要，用以实现在终端输入的命令行转化为执行的函数和其参数，这个类相对独立"""

    @staticmethod
    def trans(content):
        """输入命令，输出函数和其参数。会补全括号和逗号"""
        s = Translate.split_string(content)
        res = Translate.point(s[0]) + s[0] + "("
        if s[0] == "load":
            s[1] = s[1].replace('\\', '/')
        for x in s[1:]:
            if isinstance(x, int):
                res += str(x) + ","
            else:
                res += "'" + x + "'" + ","
        if len(s) == 1:
            res += ")"
        else:
            res = res[:-1] + ")"
        # print(res)
        return res

    @staticmethod
    def split_string(string):
        """将字符简单分割，以list输出函数名和对应的参数，会对应所需参数数量分割"""
        res = string.split()
        if len(res) == 1:
            return res
        temp = ""
        # 以第2个字符串是否含有md语法符号实现
        # for target in ['#', '*', '.']:
        #     index = res[1].find(target)
        #     if index != -1:
        #         for s in res[1:]:
        #             temp += s + ' '
        #         # print(temp)
        #         return [res[0], temp[:-1]]
        # for s in res[2:]:
        #     temp += s + ' '
        # # print(temp)
        # return [res[0], res[1], temp[:-1]]
        # 以第2个字符串是否为数字实现
        if res[1].isdigit():
            if len(res) == 2:
                return [res[0], int(res[1])]
            else:
                for s in res[2:]:
                    temp += s + ' '
                return [res[0], int(res[1]), temp[:-1]]
        else:
            for s in res[1:]:
                temp += s + ' '
            return [res[0], temp[:-1]]

    @staticmethod
    def point(string):
        """指出终端输入命令属于该文件的那个类，以下均为需求文档中的命令，后期可根据需要进行修改"""
        if string in ["load", "save"]:
            return "fileop."
        elif string in ["insert", "append_head", "append_tail", "delete", "undo", "redo"]:
            return "edit."
        # elif string in ["undo", "redo"]:
        #     return "record."
        elif string in ["list", "list_tree", "dir_tree"]:
            return "display."
        elif string in ["history"]:
            return "log."
        elif string in ["stats"]:
            return "statistics."


class Log:
    def __init__(self, history_path):
        self.history_path = history_path

    def track(self, content):
        """将输入的指令记录入history文件中，如果没有，会自动创建"""
        with open(self.history_path, 'a+') as f:
            f.write(time.strftime("%Y%m%d %H:%M:%S", time.localtime()) + " " + content + "\n")

    def history(self, *args):
        with open(self.history_path, 'r+') as f:
            history = f.readlines()
            if len(args) == 1:
                for line in history[-args[0]:]:
                    print(line, end='')
            else:
                for line in history:
                    print(line, end='')


class Statistics:
    def __init__(self, stats_path):
        self.stats_path = stats_path
        self.md_path = ""

    def wtime(self, md_path, duration):
        """向文件中写入时间，首先会检测是否有以前写入的记录，有则累加，检测完后没有则新建"""
        self.md_path = md_path
        try:
            timelist = []
            with open(self.stats_path, 'r+') as f:
                timestats = f.readlines()
                # print(timestats)
                flag = True
                for line in timestats:
                    if line.split()[0] == md_path:
                        newtime = int(line.split()[1].replace('\n', '')) + int(duration)
                        timelist.append(md_path + " " + str(newtime) + "\n")
                        flag = False
                    else:
                        timelist.append(line)
                temp = ""
                # print(timelist)
                for line in timelist:
                    temp += line
                if flag:
                    temp += md_path + " " + str(int(duration)) + "\n"
                with open(self.stats_path, 'w') as f:
                    f.write(temp)
        except FileNotFoundError:
            with open(self.stats_path, 'w') as f:
                pass

    def stats(self, option):
        """打印计时记录，秒数部分会转化后再打印"""
        with open(self.stats_path, 'r+') as f:
            rcd = f.readlines()
            # print(rcd)
            if option == "all":
                for line in rcd:
                    print(line.split()[0] + " " + self.fduration(int(line.split()[1])))
            elif option == "current":
                for line in rcd:
                    if line.split()[0] == self.md_path:
                        print(line.split()[0] + " " + self.fduration(int(line.split()[1])))
                        break

    def fduration(self, duration):
        """输入时间间隔的秒数，输出规范化的以时分秒的时间"""
        res = ""
        duration = int(duration)
        if duration >= 60 * 60 * 24:
            res += str(duration // (60 * 60 * 24)) + " 天 "
            duration = duration % (60 * 60 * 24)
        if duration >= 60 * 60:
            res += str(duration // (60 * 60)) + " 小时 "
            duration = duration % (60 * 60)
        if duration >= 60:
            res += str(duration // (60)) + " 分钟 "
            duration = duration % (60)
        res += str(duration) + " 秒 "
        return res

    def tduration(self, strtime):
        """将字符串形式的时间转化为秒数"""
        pass


class FileOp2(FileOp):
    """会在运行计时的文件操作"""
    def __init__(self, md_path):
        super().__init__(md_path)
        self.start_time = 0
        self.end_time = 0

    def load(self, address):
        super().load(address)
        # with open(history_path, 'a+') as f:
        #     f.write("session start at " + time.strftime("%Y%m%d %H:%M:%S", time.localtime()) + "\n")
        # global start_time
        self.start_time = time.time()

    def save(self):
        super().save()
        # global start_time, end_time
        end_time = time.time()
        # self.wtime(end_time - start_time)
        self.start_time = end_time

    def get_duration(self):
        duration = self.end_time - self.start_time
        self.start_time = self.end_time
        return duration


# 实例化已有的类
# fileop = FileOp2()
# edit = Edit1()
# display = Display()
# translate = Translate()
# log = Log()
# statistics = Statistics()


class Md:
    def __init__(self, md_path):
        # 获取路径
        self.md_path = md_path.replace('\\', '/')
        self.history_path = os.path.join(os.getcwd(), "history.txt").replace('\\', '/')
        self.stats_path = os.path.join(os.getcwd(), "stats.txt").replace('\\', '/')
        # 实例化需要的类
        self.fileop = FileOp(self.md_path)
        self.edit = Edit2(self.fileop.get_md())
        self.display = Display(self.fileop.get_md())
        self.log = Log(self.history_path)
        self.statistics = Statistics(self.stats_path)
        # md同步
        self.edit.add_ob(self.fileop)
        self.edit.add_ob(self.display)

    def test(self):
        print("md class test")


# if __name__ == "__main__":
#     while True:
#         content = input()
#         eval(translate.trans(content))
#         log.track(content)
#         print(md)

if __name__ == "__main__":
    # 独立执行history和stats相关操作
    history_path = os.path.join(os.getcwd(), "history.txt").replace('\\', '/')
    stats_path = os.path.join(os.getcwd(), "stats.txt").replace('\\', '/')
    log = Log(history_path)
    statistics = Statistics(stats_path)
    while True:
        content = input()
        if Translate.split_string(content)[0] == "load":
            # print(content[5:].replace('\\', '/'))
            md_path = content[5:].replace('\\', '/')
            start_time = time.time()
            end_time = time.time()
            # 实例化md
            md = Md(md_path)
            while True:
                content = input()
                print(f"md.{Translate.trans(content)}")
                md.log.track(content)
                eval(f"md.{Translate.trans(content)}")
                if content == "save":
                    end_time = time.time()
                    statistics.wtime(md_path, end_time - start_time)
                    start_time = end_time
                print(md.edit.get_md())
        elif Translate.split_string(content)[0] in ["history", "stats"]:
            # 无论是否执行md，都可以执行history和stats相关操作
            eval(f"{Translate.trans(content)}")
        else:
            print("load md first")

