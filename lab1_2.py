import time

md_path = ""
history_path = ""
stats_path = ""
md = []
bp = []


class FileOp:
    """文件相关操作"""

    def load(self, address):
        """加载文件，如果没有就新创建"""
        global md_path, history_path, stats_path
        md_path = address.replace('\\', '/')
        history_path = md_path[:md_path.rfind('/')] + r"/history.txt"
        stats_path = md_path[:md_path.rfind('/')] + r"/stats.txt"
        # addr = address
        try:
            with open(md_path, 'r+') as f:
                global md
                md = f.readlines()
                # edit.rcd()
        except FileNotFoundError:
            with open(md_path, 'w') as f:
                pass

    def save(self):
        """保存文件，会覆盖原有的文件，但已经保存了原本的md，所以无影响"""
        with open(md_path, 'w') as f:
            for line in md:
                f.write(line)
            # edit.rcd()


class Edit:
    """编辑文件"""

    def insert(self, *args):
        """由于python不支持函数重载，这里用可变参数实现"""
        self.rcd()  # 执行前会进行备份
        print("editing")
        global md
        if len(args) == 1:
            md.insert(len(md), str(args[0]) + "\n")
        elif len(args) == 2:
            md.insert(int(args[0]) - 1, str(args[1]) + "\n")

    def append_head(self, content):
        """用insert实现"""
        self.insert(1, content)

    def append_tail(self, content):
        """用insert实现"""
        self.insert(content)

    def delete(self, content):
        self.rcd()  # 执行前会进行备份
        if isinstance(content, int):
            md.pop(content - 1)
        elif isinstance(content, str):
            md.remove(content + '\n')

    def rcd(self):
        """备份实现的方式是复制"""
        global md, bp
        bp = md[:]

    def undo(self):
        global md, bp
        md, bp = bp, md

    def redo(self):
        global md, bp
        md, bp = bp, md


class Display:
    """展示md，以打印的方式"""

    def list(self):
        global md
        for line in md:
            print(line, end='')

    def list_tree(self):
        pass

    def dir_tree(self):
        pass


class Translate:
    """并不是原本文档里的需求，但是很重要，用以实现在终端输入的命令行转化为执行的函数和其参数，这个类相对独立"""

    def trans(self, content):
        """输入命令，输出函数和其参数。会补全括号和逗号"""
        s = self.split_string(content)
        res = self.point(s[0]) + s[0] + "("
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

    def split_string(self, string):
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

    def point(self, string):
        """指出终端输入命令属于该文件的那个类，以下均为需求文档中的命令，后期可根据需要进行修改"""
        if string in ["load", "save"]:
            return "fileop."
        elif string in ["insert", "append_head", "append_tail", "delete", "undo", "redo"]:
            return "edit."
        elif string in ["list", "list_tree", "dir_tree"]:
            return "display."
        elif string in ["history"]:
            return "log."
        elif string in ["stats"]:
            return "statistics."


class Log:
    def track(self, content):
        """将输入的指令记录入history文件中，如果没有，会自动创建"""
        with open(history_path, 'a+') as f:
            f.write(time.strftime("%Y%m%d %H:%M:%S", time.localtime()) + " " + content + "\n")

    def history(self, *args):
        with open(history_path, 'r+') as f:
            history = f.readlines()
            if len(args) == 1:
                for line in history[-args[0]:]:
                    print(line, end='')
            else:
                for line in history:
                    print(line, end='')


class Statistics:
    def stats(self):
        with open(stats_path, 'r+') as f:
            rcd = f.readlines()
            for line in rcd:
                print(line, end='')

    def fduration(self, duration):
        """输入时间间隔的秒数，输出规范化的以时分秒的时间"""
        res = ""
        duration = int(duration)
        if duration >= 60 * 60 * 24:
            res += str(duration // (60 * 60 * 24)) + "天"
            duration = duration % (60 * 60 * 24)
        if duration >= 60 * 60:
            res += str(duration // (60 * 60)) + "小时"
            duration = duration % (60 * 60)
        if duration >= 60:
            res += str(duration // (60)) + "分钟"
            duration = duration % (60)
        res += str(duration) + "秒"
        return res


class test:
    def ph(self):
        print("hello")


# 实例化已有的类
fileop = FileOp()
edit = Edit()
display = Display()
translate = Translate()
log = Log()
statistics = Statistics()


if __name__ == "__main__":
    while True:
        content = input()
        eval(translate.trans(content))
        log.track(content)
        print(md)
