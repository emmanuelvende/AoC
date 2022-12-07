import re

# s = "16232 fvhn.fqm"


# def is_command(s):
#     return re.match(r"^$", s)


class Dir:
    def __init__(self, depth, name):
        self.depth = depth
        self.name = name
        self.dirs = []
        self.files = []

    def __str__(self):
        return (
            f"Dir<{self.name}, {self.depth}>{{DIRS={self.dirs}, FILES={self.files}}}"
        )

    def __repr__(self):
        return self.__str__()


# class FS:
#     def __init__(self, name, parent):
#         self.name = name
#         self.parent = parent  # str
#         self.folders = []  # list of str
#         self.files = []  # list of (str, int)


class FSMgr:
    def __init__(self):
        # self.fs = FS()
        self.fs = []
        self.mode = None
        self.deepness = 0
        self.curdirname = ""

    def parse_for_file_info(self, s):
        m = re.search(r"^(?P<filesize>\d+) (?P<filename>[\w\.]+)", s)
        if m:
            filesize = int(m.group("filesize"))
            filename = m.group("filename")
            self.add_file(filename, filesize)
        return bool(m)

    def parse_for_dir_info(self, s):
        m = re.search(r"^dir (?P<dirname>\w+)", s)
        if m:
            dirname = m.group("dirname")
            self.add_dir(dirname)

    def enter_dir(self, dirname):
        self.deepness += 1
        self.curdirname = dirname

    def up(self):
        self.deepness -= 1

    def add_file(self, filename, filesize):
        self.fs[self.deepness].files.append((filename, filesize))

    def add_dir(self, dirname):
        newdir = Dir(self.deepness, dirname)
        self.fs.append(newdir)

    def parse_for_command(self, s):
        m = re.match(r"^$", s)
        if m:
            if s == "$ ls":
                self.mode = "listing"
            elif s == "$ cd ..":
                self.up()
            else:
                n = re.match(r"\$ cd (?P<dirname>\w+)", s)
                dirname = n.group("dirname")
                self.enter_dir(dirname)

        return bool(m)


with open("test.txt", "r") as f:
    lines = f.readlines()

fsmgr = FSMgr()

for line in lines:
    for action in (
        fsmgr.parse_for_command,
        fsmgr.parse_for_dir_info,
        fsmgr.parse_for_file_info,
    ):
        success = action(line)
        if success:
            break

print(fsmgr.fs)


# directory : ("name", []) with [] containing subdirs
# class FS:
#     def __init_(self):
#         self.dirs = []
#         self.stack_dirnames = []
#         self.curdir_index = 0

#     def new_dir(self, dirname):
#         self.dirs.append((dirname, []))

#     def cd(self, dirname):
#         pass

#     def new_file_in_curdir(self, filename, filesize):
#         self.dirs

#     def up(self):
#         pass


# m = re.search(r"move (?P<n>\d+) from (?P<a>\d+) to (?P<b>\d+)", s)
# int(m.group("n")), int(m.group("a")), int(m.group("b"))
