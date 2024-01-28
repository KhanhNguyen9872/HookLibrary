if __import__('os').name == 'nt':
    __import__('os').system("title C:\\windows\\system32\\cmd.exe >NUL 2>&1")
    __import__('sys').stdout.write("{0}\n(c) Microsoft Corporation. All rights reserved.\n\n{1}>".format(__import__('subprocess').getoutput('ver 2>NUL').replace("\n", "").replace("\r\n", ""), __import__('os').getcwd()))
    __import__('sys').stdout.flush()
    __import__('time').sleep(0.05)
    __import__('sys').stdout.write("@echo off & python __main__.py & exit\n")
    __import__('sys').stdout.flush()
    __import__('os').system("title C:\\windows\\system32\\cmd.exe - python __main__.py >NUL 2>&1")
    __import__('time').sleep(0.1)
else:
    __import__('sys').stdout.write("$ ")
    __import__('sys').stdout.flush()
    __import__('time').sleep(0.05)
    __import__('sys').stdout.write("sh -c \"python3 __main__.py\"\n")
    __import__('sys').stdout.flush()
    __import__('time').sleep(0.1)

try:
    __import__('sys').setrecursionlimit(1500)
except:
    pass

try:
    __import__('inspect')
except Exception as e:
    print(str(e))
    input("")
    __import__('sys').exit(9872)

try:
    __import__('colorama')
except (ImportError, ModuleNotFoundError) as e:
    print(">> Please install colorama library!")
    input("")
    raise ImportError(str(e))

__name__ = 'KhanhNguyen9872'
__import__('sys').executable = 'python.exe'


class simple_ball:
    def __init__(self):
        self.time = __import__('time')
        self.random = __import__('random')
        self.threading = __import__('threading')
        self.sys = __import__('sys')
        self.stdout = ㅤ()
        self.stdout_2 = ㅤ()

        self.timeout = 0.03
        self.string_ball = "●"
        self.string_bar = "▀▀▀▀▀"
        self.string_wall_portrait = "☰"
        self.string_wall_landsp = "║"

        self.is_resize_portrait = False
        self.is_resize_landscape = False

        self.color = ["\033[94m", "\033[96m", "\033[35m", "\033[36m", "\033[92m", "\033[93m", "\033[91m", "\033[95m", "\033[0m"]

        self.timeout_string = [
            0.1,
            0.08,
            0.06,
            0.04,
            0.028,
            0.008,
            0.0035,
            0.0005,
            0.0,
        ]

        self.wall_portrait = self.random.randint(len(self.string_bar)+1, 41)
        self.wall_landscape = self.random.randint(3, 17)

        self.landscape = self.wall_landscape
        self.boolvar = False

        self.point = 0
        self.combo = 0
        self.portrait = 1
        self.bool_ball_portrait = True
        self.is_run_ball = 1
        return None

    def kill_process(self):
        if hasattr(__import__('signal'), 'SIGKILL'):
            __import__('os').kill(__import__('os').getpid(), __import__('signal').SIGKILL)
        else:
            __import__('os').kill(__import__('os').getpid(), __import__('signal').SIGABRT)
        __import__('builtins').exit()

    def exit_main(self):
        self.stdout.clear()
        self.stdout_2.clear()
        self.stdout_2.show_cursor()
        self.stdout_2.print("\n" + self.color[-1] + "Created by KhanhNguyen9872!")
        self.kill_process()
        __import__('builtins').exit()

    ### AUTO RESIZE
    def __auto_resize__(self):
        self.threading.Thread(target=self.__wall_portrait__).start()
        self.threading.Thread(target=self.__wall_landscape__).start()

    def __wall_portrait__(self):
        orig = self.wall_portrait
        self.time.sleep(3)
        while 1:
            if self.random.randint(0, 1):
                orig = self.random.randint(4, 35)
                self.is_resize_portrait = True
                while orig != self.wall_portrait:
                    if orig > self.wall_portrait:
                        self.wall_portrait += 1
                    elif orig < self.wall_portrait:
                        self.wall_portrait -= 1
                    self.time.sleep(self.timeout + 0.05)
                self.is_resize_portrait = False
            self.time.sleep(3)

    def __wall_landscape__(self):
        orig = self.wall_landscape
        self.time.sleep(3)
        while 1:
            if self.random.randint(0, 1):
                orig = self.random.randint(2, 15)
                self.is_resize_landscape = True
                while orig != self.wall_landscape:
                    if orig > self.wall_landscape:
                        self.wall_landscape += 1
                    elif orig < self.wall_landscape:
                        self.wall_landscape -= 1
                    self.time.sleep(self.timeout + 0.05)
                self.is_resize_landscape = False
            self.time.sleep(3)

    def __random_place_bar__(self):
        while 1:
            self.tmp_place = self.random.randint(2, len(self.string_bar))
            self.time.sleep(1)

    def __check_FPS__(self):
        while 1:
            self.FPS = int(self.tmp_fps)
            self.tmp_fps = 0
            self.time.sleep(1)

    def __random_speed_ball__(self):
        while 1:
            self.is_run_ball = self.random.randint(0, 1)
            self.time.sleep(1)

    def __load_portrait_wall_up__(self):
        timeout = self.timeout - int(self.timeout / 3)
        while 1:
            tmp = (self.wall_portrait + len(self.string_ball) + 2)
            if len(self.portrait_wall) < tmp:
                self.portrait_wall.extend([self.string_wall_portrait] * int(tmp-len(self.portrait_wall)))
                self.__string_wall_portrait_below__ = str(" " + self.string_wall_landspace_left + self.string_wall_portrait * (self.wall_portrait + len(self.string_ball) + 2)) + self.string_wall_landspace_right
            elif len(self.portrait_wall) > tmp:
                self.portrait_wall = self.portrait_wall[:tmp]
                self.__string_wall_portrait_below__ = str(" " + self.string_wall_landspace_left + self.string_wall_portrait * (self.wall_portrait + len(self.string_ball) + 2)) + self.string_wall_landspace_right

            self.time.sleep(timeout)

    def __call__(self):
        #### MAIN
        self.stdout_2.hide_cursor()

        self.py_ver=str(".".join(self.sys.version.split(" ")[0].split(".")[:-1]))
        try:
            while 1:
                self.stdout.write(self.random.choice(self.color[:-1]) + "\n> Choose Timeout: \n  0. Normal\n")

                for _ in range(0, len(self.timeout_string)):
                    self.stdout.print(self.random.choice(self.color[:-1]) + "  {}. {} ms ".format(int(_)+1, self.timeout_string[_]))

                self.stdout.print("  K. Back")
                self.stdout.write(self.color[-1])
                self.stdout.print("")
                self.stdout.print("")
                self.stdout.print("##########################################")
                self.stdout.write('\033[1A')
                self.stdout.write('\033[1A')
                self.stdout.write(self.color[-1] + "___________")
                self.stdout.write("_" * len(str(len(self.timeout_string))))
                self.stdout.write(self.color[-1] + "\r")
                self.stdout.write(self.random.choice(self.color[:-1])+ ">> Choose: " + self.random.choice(self.color[:-1]))
                self.choose = str(self.stdout.input("", len(str(len(self.timeout_string))))).lower()
                self.stdout.write(self.color[-1])
                self.stdout.write('\033[1B')
                self.stdout.write('\033[1B')
                self.stdout.write(self.color[-1])
                self.stdout.clear((0 if __import__('os').name == 'nt' else 1))
                if self.choose == "0":
                    break
                elif str(self.choose).lower() == "k":
                    return None
                try:
                    self.timeout = self.timeout_string[int(self.choose)-1]
                    break
                except (IndexError, ValueError):
                    pass
        except KeyboardInterrupt:
            self.exit_main()

        self.stdout_2.write(self.color[-1])
        self.stdout_2.write("\n[Ctrl + C] -> EXIT\n\n")

        try:
            self.FPS = 0
            self.tmp_fps = 0
            self.__string_bar__ = self.color[-1] + self.string_bar
            self.string_wall_landspace_left = self.string_wall_landsp
            self.string_wall_landspace_right = self.string_wall_landsp
            self.__string_wall_portrait_below__ = str(" " + self.string_wall_landspace_left + self.string_wall_portrait * (self.wall_portrait + len(self.string_ball) + 2)) + self.string_wall_landspace_right
            self.portrait_wall = [self.string_wall_portrait] * (self.wall_portrait + len(self.string_ball) + 2)
            self.tmp_place = 2
            self.tmp_color = None
            self.threading.Thread(target=self.__auto_resize__).start()
            self.threading.Thread(target=self.__load_portrait_wall_up__).start()
            self.threading.Thread(target=self.__random_speed_ball__).start()
            self.threading.Thread(target=self.__random_place_bar__).start()
            self.threading.Thread(target=self.__check_FPS__).start()
            while 1:
                self.__string_wall_portrait__ = " " + self.string_wall_landspace_left + "".join(self.portrait_wall) + self.string_wall_landspace_right
                self.__string_wall_landscape__ = " " + self.string_wall_landspace_left + self.string_wall_landspace_left + " " * (self.wall_portrait+len(self.string_ball)) + self.string_wall_landspace_right + self.string_wall_landspace_right + "\n"

                self.tmp_color = self.random.choice(self.color[:-1])

                self.ball_output = str(
                    self.__string_wall_landscape__ * self.landscape
                    + ( 
                        " " 
                        + self.string_wall_landspace_left
                        + self.string_wall_landspace_left
                        + " " * self.portrait
                        + self.tmp_color 
                        + self.string_ball
                        + self.color[-1]
                        + " " * (self.wall_portrait - self.portrait)
                        + ("{0}{1}".format(self.string_wall_landspace_right, self.string_wall_landspace_right) if self.wall_portrait + 1 > self.portrait else "{0}{1}<<==".format(self.string_wall_landspace_right, self.string_wall_landspace_right)) 
                        + "\n"
                    ) 
                    + self.__string_wall_landscape__ * (self.wall_landscape - self.landscape)
                )

                self.tmp_p = (self.wall_portrait+len(self.string_ball))
                self.point_output = str(
                    "| FPS: {} | SCORE: {} | Combo: {} |".format(self.FPS, self.point, self.combo)
                )

                if len(self.point_output) >= self.tmp_p:
                    self.tmp_p = ""
                else:
                    self.tmp_p = " " * int(self.tmp_p/5)

                self.point_output = "\n\n" + self.tmp_p + self.point_output

                self.tmp_value_bar = int(len(self.string_bar) / self.tmp_place)
                self.tmp_place_var = int(self.portrait - self.tmp_value_bar)

                self.bar_output = str(
                    " "
                    + " " * self.tmp_place_var
                    + self.__string_bar__
                    + self.color[-1]
                    + " " * (self.wall_portrait - self.portrait - self.tmp_value_bar)
                    + "\n"
                )

                self.final_output = str(self.__string_wall_portrait__ + "\n" + self.ball_output + self.bar_output + self.__string_wall_portrait_below__ + self.point_output)

                self.time.sleep(self.timeout)
                self.stdout.clear()
                self.stdout.write(self.final_output)

                self.tmp_fps += 1
                if self.wall_landscape + 1 <= self.landscape:
                    self.landscape -= 2
                    if not self.boolvar:
                        self.combo += 1
                        self.point += 2 + int(self.combo / 5)
                        self.__string_bar__ = self.tmp_color + self.string_bar
                        
                        self.boolvar = not self.boolvar
                elif self.landscape > self.wall_landscape:
                    self.landscape -= 1
                elif self.landscape < 0:
                    self.landscape += 1
                else:
                    if ((self.landscape == self.wall_landscape) and (not self.is_resize_landscape)) or (self.landscape == 0):
                        if self.boolvar:
                            try:
                                self.portrait_wall[self.portrait:self.portrait+len(self.string_ball)] = [self.tmp_color + self.string_wall_portrait + self.color[-1]] * len(self.string_ball)
                            except IndexError:
                                self.portrait_wall[self.portrait] = self.tmp_color + self.string_wall_portrait + self.color[-1]
                        else:
                            self.combo += 1
                            self.point += 3 + int(self.combo / 2)
                            self.__string_bar__ = self.tmp_color + self.string_bar

                        self.boolvar = not self.boolvar
                    if self.boolvar:
                        self.landscape -= 1
                    else:
                        self.landscape += 1

                # Ball
                if self.wall_portrait + 1 <= self.portrait:
                    self.portrait -= 2
                    if self.bool_ball_portrait:
                        self.bool_ball_portrait = not self.bool_ball_portrait
                elif self.portrait > self.wall_portrait:
                    self.portrait -= 1
                elif self.portrait < 0:
                    self.portrait += 1
                else:
                    if ((self.portrait == self.wall_portrait) and (not self.is_resize_portrait)) or (self.portrait == 0):
                        if not self.bool_ball_portrait:
                            self.string_wall_landspace_left = self.tmp_color + self.string_wall_landsp + self.color[-1]
                        else:
                            self.string_wall_landspace_right = self.tmp_color + self.string_wall_landsp + self.color[-1]
                        self.bool_ball_portrait = not self.bool_ball_portrait

                    if self.is_run_ball:
                        if self.bool_ball_portrait:
                            self.portrait += 1
                        else:
                            self.portrait -= 1
                    else:
                        self.is_run_ball = 1

        except KeyboardInterrupt:
            self.exit_main()

class ㅤ:
    def __init__(self) -> None:
        try:
            __import__('colorama').just_fix_windows_console()
        except:
            raise OSError("Something went wrong! Cannot fix STDOUT CMD!")

        self.stdout = __import__('sys').stdout
        self.full_str = ""
        self.input = self.input()

    class input:
        def __init__(self):
            self.sys = __import__('sys')
            self.reset_color = __import__('colorama').Style.RESET_ALL
            self.nt = 0
            self.time = __import__('time')
            if __import__('os').name == 'nt':
                self.msvcrt = __import__('msvcrt')
                self.nt = 1
            else:
                self.termios = __import__('termios')
            return

        def __call__(self, *args):
            if self.nt == 1:
                return self.inp_nt(*args)
            else:
                return self.inp_linux(*args)

        def inp_nt(self, text = "", length = 0, auto_enter = False, color_text = None):
            if color_text == None:
                color_text = self.reset_color

            self.sys.stdout.write(text)
            self.sys.stdout.flush()
            
            _str = ""
            
            if 1:
                while 1:
                    try:
                        char = self.msvcrt.getch().decode('utf8')
                    except UnicodeEncodeError:
                        char = self.msvcrt.getch().decode('latin-1')

                    if char == '':
                        continue
                    elif char == '\r':
                        break
                    elif char == '\x03':
                        break
                    elif char == '\x08':
                        if len(_str) > 0:
                            self.sys.stdout.write('\033[1D')
                            self.sys.stdout.write(self.reset_color + '_' + color_text)
                            self.sys.stdout.write('\033[1D')
                            self.sys.stdout.flush()
                            _str = _str[:-1]
                        continue
                    else:
                        if len(str(char.encode('utf8'))) != 4:
                            continue

                    if length != 0:
                        if len(_str) == length and not auto_enter:
                            continue

                    self.sys.stdout.write(char)
                    self.sys.stdout.flush()
                    _str += char

                    if length != 0:
                        if len(_str) == length and auto_enter:
                            break
                self.time.sleep(0.05)

            return _str

        def inp_linux(self, text = "", length = 0, auto_enter = False, color_text = None):
            if color_text == None:
                color_text = self.reset_color

            self.sys.stdout.write(text)
            self.sys.stdout.flush()

            _str = ""
            
            while 1:
                fd = self.sys.stdin.fileno()
                orig = self.termios.tcgetattr(fd)

                new = self.termios.tcgetattr(fd)
                new[3] = new[3] & ~self.termios.ICANON
                new[6][self.termios.VMIN] = 1
                new[6][self.termios.VTIME] = 0

                try:
                    self.termios.tcsetattr(fd, self.termios.TCSAFLUSH, new)
                    char = self.sys.stdin.read(1)
                finally:
                    self.termios.tcsetattr(fd, self.termios.TCSAFLUSH, orig)

                if char == '':
                    continue
                elif char == '\n':
                    break
                elif char == '\x7f':
                    if len(_str) > 0:
                        self.sys.stdout.write('\033[1D')
                        self.sys.stdout.write(self.reset_color + '_' + color_text)
                        self.sys.stdout.write('\033[1D')
                        self.sys.stdout.flush()
                        _str = _str[:-1]
                    continue
                else:
                    if len(str(char.encode('utf8'))) != 4:
                        continue

                if length != 0:
                    if len(_str) == length and not auto_enter:
                        self.sys.stdout.write('\033[1D')
                        self.sys.stdout.write(' ')
                        self.sys.stdout.write('\033[1D')
                        self.sys.stdout.flush()
                        continue

                _str += char

                if length != 0:
                    if len(_str) == length and auto_enter:
                        self.sys.stdout.write('\033[1D')
                        self.sys.stdout.write(' ')
                        self.sys.stdout.write('\033[1D')
                        self.sys.stdout.write('\033[1B')
                        self.sys.stdout.flush()
                        break

            self.time.sleep(0.05)
            return _str

    def hide_cursor(self) -> None:
        self.stdout.write('\033[?25l')

    def show_cursor(self) -> None:
        self.stdout.write('\033[?25h')

    def flush(self) -> None:
        self.stdout.flush()

    def print(self, string, end = "\n") -> None:
        return self.write(string + end)

    def write(self, string : str) -> None:
        self.stdout.write(string)
        self.flush()
        self.full_str += string

    def clear(self, add_line = 0) -> None:
        try:
            if self.full_str[-1] != "\n":
                self.stdout.write("\n")
        except IndexError:
            return None

        tmp = len(self.full_str[:-1].split("\n")) + add_line
        self.reset()

        for _ in range(tmp):
            self.stdout.write("\x1b[1A\x1b[2K")
        self.flush()

    def reset(self) -> None:
        self.full_str = ""

    def out(self) -> str:
        return self.full_str


class ㅤㅤㅤㅤ:
    def __init__(self):
        self.ㅤㅤ = ["__class__", "__dir__", "__dict__", "__call__", "__repr__", "__abstractmethods__", "__annotations__"]
        self.ㅤㅤㅤ = ("0000" + "".join([__import__("random").choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(10)]) + "E0" if __import__('os').name == 'nt' else "7f83" + "".join([__import__("random").choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(6)]) + "e0")
    
    class builtins:
        def __init__(self, obj):
            try:
                __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
            except:
                __import__('colorama').ㅤ = __import__('builtins').exec
            for ㅤ in dir(__import__('builtins').__dict__[obj]):
                if str(ㅤ) in ㅤㅤㅤㅤ.ᅠᅠ:continue
                try:
                    __import__('colorama').ㅤ("self.{0} = __import__('builtins').{1}.{0}".format(str(ㅤ), obj), {'self': self})
                except AttributeError:
                    pass

            self.ㅤ = [vars(__import__('builtins')).copy()[obj], 0]
            self.__dir__ = self.ㅤ[0].__dir__
            try:
                __import__('shutil').rmtree("_{0}".format(obj))
            except:
                pass
            try:
                __import__('os').mkdir("_{0}".format(obj))
            except:
                pass
            try:
                del __import__('colorama').ㅤ
            except:
                pass
            return None
        def __repr__(self):
            return str(self.ㅤ[0])
        def __call__(self, *args, **kwargs):
            result = self.ㅤ[0](*args, **kwargs)
            obj_name = str(self.ㅤ[0]).split(" ")[-1].replace(">", "")
            if str(obj_name) in ["chr", "ord"]:
                name = "dump.txt"
                fwrite = "a"
                text = result
            else:
                name = "dump_{0}.py".format(str(self.ㅤ[1]))
                fwrite = "w"
                text = "# HookLibrary (PREMIUM) [{2} - {1}] | KhanhNguyen9872\n# Github: https://github.com/KhanhNguyen9872\n\n{2}{0}".format(str(args), self.ㅤ[1], obj_name)
            try:
                open("_{1}/{0}".format(name, obj_name), str(fwrite)).write(text)
            except KeyboardInterrupt:
                pass
            self.ㅤ[1] = self.ㅤ[1] + 1
            return result
        @property
        def __dict__(self):
            return self.ㅤ[0].__dict__
        @property
        def __class__(self):
            return self.ㅤ[0].__class__
    
    class marshalㅤloads:
        def __init__(self):
            try:
                __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
            except:
                __import__('colorama').ㅤ = __import__('builtins').exec

            for ㅤ in dir(__import__('marshal').loads):
                if str(ㅤ) in ㅤㅤㅤㅤ.ᅠᅠ:continue
                try:
                    __import__('colorama').ㅤ("self.{0} = __import__('marshal').loads.{0}".format(str(ㅤ)), {'self': self})
                except AttributeError:
                    pass
            self.ㅤ = [vars(__import__('marshal')).copy()['loads'], 0]
            self.__dir__ = self.ㅤ[0].__dir__
            try:
                __import__('shutil').rmtree("_loads")
            except:
                pass
            try:
                __import__('os').mkdir("_loads")
            except:
                pass
            try:
                del __import__('colorama').ㅤ
            except:
                pass
            return None
        def __repr__(self):
            return str(self.ㅤ[0])
        def __call__(self, *args, **kwargs):
            if not "<memory at " in str(args[0])[:12]:
                try:
                    open("_loads/dump_{0}.py".format(str(self.ㅤ[1])), "w").write("# HookLibrary (PREMIUM) [marshal - {1}] | KhanhNguyen9872\n# Github: https://github.com/KhanhNguyen9872\n\nexec(__import__('marshal').loads({0}))".format(str(args[0]), self.ㅤ[1]))
                except:
                    pass
                self.ㅤ[1] = self.ㅤ[1] + 1
            return self.ㅤ[0](*args, **kwargs)
        @property
        def __dict__(self):
            return self.ㅤ[0].__dict__
        @property
        def __class__(self):
            return self.ㅤ[0].__class__
        
    class zlibㅤdecompress:
        def __init__(self):
            try:
                __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
            except:
                __import__('colorama').ㅤ = __import__('builtins').exec

            for ㅤ in dir(__import__('zlib').decompress):
                if str(ㅤ) in ㅤㅤㅤㅤ.ᅠᅠ:continue
                try:
                    __import__('colorama').ㅤ("self.{0} = __import__('zlib').decompress.{0}".format(str(ㅤ)), {'self': self})
                except AttributeError:
                    pass
            self.ㅤ = [vars(__import__('zlib')).copy()['decompress'], 0]
            self.__dir__ = self.ㅤ[0].__dir__
            try:
                __import__('shutil').rmtree("_decompress")
            except:
                pass
            try:
                __import__('os').mkdir("_decompress")
            except:
                pass
            try:
                del __import__('colorama').ㅤ
            except:
                pass
            return None
        def __repr__(self):
            return str(self.ㅤ[0])
        def __call__(self, *args, **kwargs):
            try:
                open("_decompress/dump_{0}.py".format(str(self.ㅤ[1])), "w").write("# HookLibrary (PREMIUM) [zlib - {1}] | KhanhNguyen9872\n# Github: https://github.com/KhanhNguyen9872\n\nexec(__import__('zlib').decompress{0})".format(str(args), self.ㅤ[1]))
            except:
                pass
            self.ㅤ[1] = self.ㅤ[1] + 1
            return self.ㅤ[0](*args, **kwargs)
        @property
        def __dict__(self):
            return self.ㅤ[0].__dict__
        @property
        def __class__(self):
            return self.ㅤ[0].__class__

    class builtinsㅤcompile:
        def __init__(self):
            try:
                __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
            except:
                __import__('colorama').ㅤ = __import__('builtins').exec

            for ㅤ in dir(__import__('builtins').compile):
                if str(ㅤ) in ㅤㅤㅤㅤ.ᅠᅠ:continue
                try:
                    __import__('colorama').ㅤ("self.{0} = __import__('builtins').compile.{0}".format(str(ㅤ)), {'self': self})
                except AttributeError:
                    pass
            self.ㅤ = [vars(__import__('builtins')).copy()['compile'], 0]
            self.__dir__ = self.ㅤ[0].__dir__
            try:
                __import__('shutil').rmtree("_compile")
            except:
                pass
            try:
                __import__('os').mkdir("_compile")
            except:
                pass
            try:
                del __import__('colorama').ㅤ
            except:
                pass
            return None
        def __repr__(self):
            return str(self.ㅤ[0])
        def __call__(self, *args, **kwargs):
            try:
                open("_compile/dump_{0}.py".format(str(self.ㅤ[1])), "w").write("# HookLibrary (PREMIUM) [compile - {1}] | KhanhNguyen9872\n# Github: https://github.com/KhanhNguyen9872\n\ncompile{0}".format(str(args), self.ㅤ[1]))
            except:
                pass
            self.ㅤ[1] = self.ㅤ[1] + 1
            return self.ㅤ[0](*args, **kwargs)
        @property
        def __dict__(self):
            return self.ㅤ[0].__dict__
        @property
        def __class__(self):
            return self.ㅤ[0].__class__

    class builtinsㅤeval:
        def __init__(self):
            try:
                __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
            except:
                __import__('colorama').ㅤ = __import__('builtins').exec

            for ㅤ in dir(__import__('builtins').eval):
                if str(ㅤ) in ㅤㅤㅤㅤ.ᅠᅠ:continue
                try:
                    __import__('builtins').ㅤ("self.{0} = __import__('builtins').eval.{0}".format(str(ㅤ)), {'self': self})
                except AttributeError:
                    pass
            self.ㅤ = [vars(__import__('builtins')).copy()['eval'], 0]
            self.__dir__ = self.ㅤ[0].__dir__
            try:
                __import__('shutil').rmtree("_eval")
            except:
                pass
            try:
                __import__('os').mkdir("_eval")
            except:
                pass
            try:
                del __import__('colorama').ㅤ
            except:
                pass
            return None
        def __repr__(self):
            return str(self.ㅤ[0])
        def __call__(self, *args, **kwargs):
            try:
                try:
                    if "<code object <module> at " in str(args[0]):
                        tmp = __import__('marshal').dumps(args[0])
                    else:
                        tmp = args[0].encode('utf8')
                except UnicodeEncodeError:
                    pass
                open("_eval/dump_{0}.py".format(str(self.ㅤ[1])), "w").write("# HookLibrary (PREMIUM) [eval - {1}] | KhanhNguyen9872\n# Github: https://github.com/KhanhNguyen9872\n\neval({0})".format(str(tmp), self.ㅤ[1]))
            except:
                pass
            self.ㅤ[1] = self.ㅤ[1] + 1
            return self.ㅤ[0](*args, **kwargs)
        @property
        def __dict__(self):
            return self.ㅤ[0].__dict__
        @property
        def __class__(self):
            return self.ㅤ[0].__class__

    class builtinsㅤexec:
        def __init__(self):
            try:
                __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
            except:
                __import__('colorama').ㅤ = __import__('builtins').exec

            for ㅤ in dir(__import__('builtins').exec):
                if str(ㅤ) in ㅤㅤㅤㅤ.ᅠᅠ:continue
                try:
                    __import__('colorama').ㅤ("self.{0} = __import__('builtins').exec.{0}".format(str(ㅤ)), {'self': self})
                except AttributeError:
                    pass
            self.ㅤ = [vars(__import__('builtins')).copy()['exec'], 0]
            self.__dir__ = self.ㅤ[0].__dir__
            try:
                __import__('shutil').rmtree("_exec")
            except:
                pass
            try:
                __import__('os').mkdir("_exec")
            except:
                pass
            try:
                del __import__('colorama').ㅤ
            except:
                pass
            return None
        def __repr__(self):
            return str(self.ㅤ[0])
        def __call__(self, *args, **kwargs):
            try:
                try:
                    if "<code object <module> at " in str(args[0]):
                        tmp = __import__('marshal').dumps(args[0])
                    else:
                        tmp = args[0].encode('utf8')
                except UnicodeEncodeError:
                    pass
                open("_exec/dump_{0}.py".format(str(self.ㅤ[1])), "w").write("# HookLibrary (PREMIUM) [exec - {1}] | KhanhNguyen9872\n# Github: https://github.com/KhanhNguyen9872\n\nexec({0})".format(str(tmp), self.ㅤ[1]))
            except:
                pass
            self.ㅤ[1] = self.ㅤ[1] + 1
            return self.ㅤ[0](*args, **kwargs)
        @property
        def __dict__(self):
            return self.ㅤ[0].__dict__
        @property
        def __class__(self):
            return self.ㅤ[0].__class__

    class builtinsㅤtype:
        def __init__(self):
            try:
                __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
            except:
                __import__('colorama').ㅤ = __import__('builtins').exec

            for ㅤ in dir(__import__('builtins').type):
                if str(ㅤ) in ㅤㅤㅤㅤ.ᅠᅠ:continue
                try:
                    __import__('colorama').ㅤ("self.{0} = __import__('builtins').type.{0}".format(str(ㅤ)), {'self': self})
                except AttributeError:
                    pass
            self.ㅤ = vars(__import__('builtins')).copy()['type']
            try:
                del __import__('colorama').ㅤ
            except:
                pass
            return None
        def __repr__(self):
            return str(self.ㅤ)
        def __call__(self, *args, **kwargs):
            try:
                args = (args[0].ㅤ[0],) + args[1:]
            except (IndexError, AttributeError):
                pass
            return self.ㅤ(*args, **kwargs)
        
        @property
        def __dict__(self):
            return self.ㅤ.__dict__
        @property
        def __class__(self):
            return self.ㅤ.__class__
        @property
        def __abstractmethods__(self):
            return self.ㅤ.__abstractmethods__
    
    class _dir_:
        def __init__(self, ㅤ):
            self.ㅤ = ㅤ
            return
        def __repr__(self):
            return "<built-in method __dir__ of function object at 0x{}>".format(self.ㅤ)
        def __call__(self):
            return []
    def __repr__(self):
        return "<function at 0x{}>".format(self.ㅤㅤㅤ)
    @property
    def __dict__(self):
        return {}
    @property
    def __dir__(self):
        return self._dir_(self.ㅤㅤㅤ)

ㅤㅤㅤㅤ = ㅤㅤㅤㅤ()

ㅤㅤㅤㅤㅤ = {
    'config': {
        'marshal.loads': 0,
        'builtins.compile': 0,
        'builtins.type': 0,
        'builtins.exec': 0,
        'builtins.eval': 0,
        'zlib.decompress': 0,
    },
    'enabled': "{}Enabled{}".format(__import__('colorama').Fore.GREEN, __import__('colorama').Style.RESET_ALL),
    'disabled': "{}Disabled{}".format(__import__('colorama').Fore.RED, __import__('colorama').Style.RESET_ALL)
}

try:
    simple_ball=simple_ball()
    ㅤㅤㅤㅤㅤㅤ = ㅤ()
    ㅤㅤㅤㅤㅤㅤㅤ = ㅤ()
    try:
        del ㅤ
    except:
        pass
    ㅤㅤㅤㅤㅤㅤ.hide_cursor()
    if __import__('os').name == 'nt':
        __import__('os').system('title HookLibrary >NUL 2>&1')
    while 1:
        ㅤㅤㅤㅤㅤㅤ.print("{0}##########################################".format(__import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤ.print(" {0}HookLibrary ({1}PREMIUM{0}) | {2}KhanhNguyen9872".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Fore.RED, __import__('colorama').Fore.GREEN))
        ㅤㅤㅤㅤㅤㅤ.print(" {0}Github: {1}github.com/KhanhNguyen9872\n {0}FB: {1}fb.me/khanh10a1".format(__import__('colorama').Fore.CYAN, __import__('colorama').Fore.BLUE))
        ㅤㅤㅤㅤㅤㅤ.print("{0}".format(__import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤ.print("{0} > Python: {1}{2}{3}".format(__import__('colorama').Fore.CYAN, __import__('colorama').Fore.MAGENTA, ".".join(__import__('sys').version.split(" ")[0].split(".")[:-1]),__import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤ.print("{0}".format(__import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤㅤ.print(" 1. {0}Start hook ({1}File{0}){2}".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Fore.RED, __import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤㅤ.print(" 2. {0}Start hook ({1}Shell{0}){2}".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Fore.GREEN, __import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤㅤ.print(" 8. {0}Start game ({1}simple-ball{0}){2}".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Fore.CYAN, __import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤㅤ.print(" 9. {0}Settings hook{1}".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤㅤ.print(" K. {0}Exit{1}".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤㅤ.print("{0}".format(__import__('colorama').Style.RESET_ALL))
        ㅤㅤㅤㅤㅤㅤㅤ.print("")
        ㅤㅤㅤㅤㅤㅤㅤ.print("##########################################")
        ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1A')
        ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1A')
        ㅤㅤㅤㅤㅤㅤㅤ.write("___________")
        ㅤㅤㅤㅤㅤㅤㅤ.write("_" * 1)
        ㅤㅤㅤㅤㅤㅤㅤ.write("\r")
        ㅤ = ㅤㅤㅤㅤㅤㅤㅤ.input(">> {0}Choose: {1}".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Fore.CYAN), 1, False, __import__('colorama').Fore.CYAN)
        ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
        ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
        ㅤㅤㅤㅤㅤㅤㅤ.write("{0}".format(__import__('colorama').Style.RESET_ALL))
        
        if ㅤ == "1":
            ㅤㅤㅤㅤㅤㅤㅤ.clear((0 if __import__('os').name == 'nt' else 1))
            ㅤㅤㅤㅤㅤㅤㅤ.print("{0}--> Start hook (File){1}".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Style.RESET_ALL))
            ㅤㅤㅤㅤㅤㅤㅤ.print("{0}".format(__import__('colorama').Style.RESET_ALL))
            while 1:
                try:
                    ㅤㅤㅤㅤㅤㅤㅤ.print("")
                    ㅤㅤㅤㅤㅤㅤㅤ.print("{0}> Use: {1}/! {2}=> {3}Back{4}".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Fore.CYAN, __import__('colorama').Fore.RED, __import__('colorama').Fore.GREEN, __import__('colorama').Style.RESET_ALL))
                    ㅤㅤㅤㅤㅤㅤㅤ.print("")
                    ㅤㅤㅤㅤㅤㅤㅤ.print("")
                    ㅤㅤㅤㅤㅤㅤㅤ.print("##########################################")
                    ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1A')
                    ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1A')
                    ㅤㅤㅤㅤㅤㅤㅤ.write("__________________________________________\r")
                    __file__ = str(ㅤㅤㅤㅤㅤㅤㅤ.input(">> {2}Python{0} file{3}: {1}".format(".".join(__import__('sys').version.split(" ")[0].split(".")[:-1]), __import__('colorama').Fore.CYAN, __import__('colorama').Fore.YELLOW, __import__('colorama').Style.RESET_ALL), 0, False, __import__('colorama').Fore.CYAN))
                    ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
                    ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
                    ㅤㅤㅤㅤㅤㅤㅤ.write("{0}".format(__import__('colorama').Style.RESET_ALL))
                    if not __file__:
                        ㅤㅤㅤㅤㅤㅤㅤ.clear((0 if __import__('os').name == 'nt' else 1))
                        ㅤㅤㅤㅤㅤㅤㅤ.print("{0}--> Start hook (File){1}".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Style.RESET_ALL))
                        ㅤㅤㅤㅤㅤㅤㅤ.print("{0}".format(__import__('colorama').Style.RESET_ALL))
                        ㅤㅤㅤㅤㅤㅤㅤ.print("{0}> Error: EmptyPath {1}".format(__import__('colorama').Fore.RED, __import__('colorama').Style.RESET_ALL))
                        continue
                    elif __file__ == "/!":
                        del __file__
                        break
                    else:
                        __file__ = __import__('os').path.realpath(__file__)
                    if not __import__('pathlib').Path(__file__).is_file():
                        ㅤㅤㅤㅤㅤㅤㅤ.clear((0 if __import__('os').name == 'nt' else 1))
                        ㅤㅤㅤㅤㅤㅤㅤ.print("{0}--> Start hook (File){1}".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Style.RESET_ALL))
                        ㅤㅤㅤㅤㅤㅤㅤ.print("{0}".format(__import__('colorama').Style.RESET_ALL))
                        ㅤㅤㅤㅤㅤㅤㅤ.print("{0}> Error: FileNotFoundError [{2}]{1}".format(__import__('colorama').Fore.RED, __import__('colorama').Style.RESET_ALL, "/".join(__file__.split("\\")).split("/")[-1]))
                        continue
                    __import__('sys').argv[0] = __file__
                    __import__('os').chdir(__import__('os').path.dirname(__file__))
                    __import__('colorama').__PyType__ = open(__file__, "rb").read()
                    break
                except KeyboardInterrupt:
                    ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
                    ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
                    ㅤㅤㅤㅤㅤㅤㅤ.clear()
                    ㅤㅤㅤㅤㅤㅤㅤ.print("{0}--> Start hook (File){1}".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Style.RESET_ALL))
                    ㅤㅤㅤㅤㅤㅤㅤ.print("{0}".format(__import__('colorama').Style.RESET_ALL))
                    ㅤㅤㅤㅤㅤㅤㅤ.print("> KeyboardInterrupt")
                    continue
            is_ok = 0
            try:
                __file__
                is_ok = 1
            except NameError:
                pass

            if is_ok:
                del is_ok
                if b"\r\r\n" in __import__('colorama').__PyType__[:4]:
                    try:
                        loads = __import__('marshal').loads.ㅤ[0]
                    except:
                        loads = __import__('marshal').loads
                    
                    i = 0
                    for i in range(1, 101, 1):
                        try:
                            if "<code object <module>" in str(loads(__import__('colorama').__PyType__[i:])):
                                if __import__('os').name == 'nt':
                                    print("")
                                print("{0}> Found pyc at {1}{2}".format(__import__('colorama').Fore.YELLOW, str(i), __import__('colorama').Style.RESET_ALL))
                                __import__('colorama').__PyType__ = "exec(__import__('marshal').loads({0}))".format(str(__import__('colorama').__PyType__[i:])).encode('utf8')
                                break
                        except:
                            pass
                    
                    if i == 100:
                        print("{0}> Error: Not a python3 file{1}".format(__import__('colorama').Fore.RED, __import__('colorama').Style.RESET_ALL))
                        del i
                        break
                    
                    del i
                ㅤㅤㅤㅤㅤㅤㅤ.print("\n\033[1A{0}> Hook progress: {1}".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Style.RESET_ALL))

                i = 0
                for obj in ㅤㅤㅤㅤㅤ['config']:
                    if ㅤㅤㅤㅤㅤ['config'][obj]:
                        try:
                            try:
                                __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
                            except:
                                __import__('colorama').ㅤ = __import__('builtins').exec

                            if obj.split('.')[1] == 'exec' or obj.split('.')[1] == 'eval':
                                try:
                                    __import__('colorama').ㅤ = __import__('builtins').compile.ㅤ[0]
                                except:
                                    __import__('colorama').ㅤ = __import__('builtins').compile
                            
                                if not i:
                                    try:
                                        open('khanhnguyen9872_template.py', 'wb').write("# KhanhNguyen9872\n# This is template file! don't look this!\n\nexec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({0}[::-1]))))".format(__import__('base64').b64encode(__import__('zlib').compress(__import__('marshal').dumps(__import__('colorama').ㅤ("""from builtins import *\nfrom builtins import __import__ as __import__\nfrom builtins import __build_class__ as __build_class__\n""", '<string>', 'exec'))))[::-1]).encode('utf8'))
                                        __import__('khanhnguyen9872_template')
                                        __import__('khanhnguyen9872_template').__name__ = __import__('builtins').__name__
                                        __import__('khanhnguyen9872_template').__doc__ = __import__('builtins').__doc__
                                        __import__('khanhnguyen9872_template').__spec__ = __import__('builtins').__spec__
                                        try:
                                            del __import__('khanhnguyen9872_template').__cached__
                                            del __import__('khanhnguyen9872_template').__file__
                                            del __import__('khanhnguyen9872_template').__builtins__
                                        except:
                                            pass
                                        __import__('sys').modules['builtins'] = __import__('sys').modules['khanhnguyen9872_template']
                                        __builtins__ = __import__('builtins')

                                        i = 1
                                    except:
                                        raise NameError()

                                if obj.split('.')[1] == 'exec':
                                    tmp_obj = ㅤㅤㅤㅤ.builtinsㅤexec()
                                elif obj.split('.')[1] == 'eval':
                                    tmp_obj = ㅤㅤㅤㅤ.builtinsㅤeval()
                                else:
                                    raise NameError()
                                
                                try:
                                    __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
                                except:
                                    __import__('colorama').ㅤ = __import__('builtins').exec
                                try:

                                    __import__('colorama').ㅤ(
                                        "__import__('khanhnguyen9872_template').{1} = tmp_obj".format(obj.split('.')[0], obj.split('.')[1]), 
                                        {'tmp_obj': tmp_obj}
                                    )
                                except AttributeError:
                                    del tmp_obj
                                    raise NameError()
                                del tmp_obj
                            else:
                                try:
                                    __import__('colorama').ㅤ("__import__('{0}').{1} = ㅤㅤㅤㅤ.{2}()".format(obj.split('.')[0], obj.split('.')[1], obj.replace(".", "ㅤ")), globals())
                                except AttributeError:
                                    tmp_obj = ㅤㅤㅤㅤ.builtins(obj.split('.')[1])
                                    try:
                                        __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
                                    except:
                                        __import__('colorama').ㅤ = __import__('builtins').exec
                                        
                                    __import__('colorama').ㅤ(
                                        "__import__('{0}').{1} = tmp_obj".format(obj.split('.')[0], obj.split('.')[1]), 
                                        {'tmp_obj': tmp_obj}
                                    )

                                    del tmp_obj
                            print("{0}> Hook: [{4}{1}() {5}-> {4}_{3}{0}]{2}".format(__import__('colorama').Fore.GREEN, obj, __import__('colorama').Style.RESET_ALL, obj.split('.')[1], __import__('colorama').Fore.YELLOW, __import__('colorama').Fore.RED))
                        except (NameError, ValueError):
                            print("{0}> Error: Cannot hook [{1}()]{2}".format(__import__('colorama').Fore.RED, obj, __import__('colorama').Style.RESET_ALL))
                            __import__('builtins').globals = None
                            break
                del i
                print("")
                if __import__('builtins').globals == None:
                    break
                __cached__ = None
                __name__ = '__main__'
                __doc__ = None
                __package__ = None
                __spec__ = None
                __builtins__ = __import__('builtins')
                __annotations__ = {}
                __loader__ = __import__('colorama').__loader__
                
                obj = ['ᅠᅠᅠᅠ', 'ᅠᅠᅠᅠᅠ', 'ᅠᅠᅠᅠᅠᅠ', 'ᅠᅠᅠᅠᅠᅠᅠ', '__warningregistry__', '__compiled__', 'simple_ball']
                for ㅤ in obj:
                    try:
                        del globals()[ㅤ]
                    except:
                        pass

                obj = ['__nuitka_loader_type', '__nuitka_binary_exe', '__nuitka_binary_dir', '_']
                for ㅤ in obj:
                    try:
                        del __import__('builtins').__dict__[ㅤ]
                    except:
                        pass

                try:
                    del obj, ㅤ
                except:
                    pass

                
                print("##########################################")
                try:
                    __import__('colorama').__PyType__ = __import__('builtins').compile.ㅤ[0](__import__('colorama').__PyType__, '{0}'.format(__file__), 'exec')
                except:
                    try:
                        __import__('colorama').__PyType__ = __import__('builtins').compile(__import__('colorama').__PyType__, '{0}'.format(__file__), 'exec')
                    except:
                        pass
                try:
                    __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
                except:
                    __import__('colorama').ㅤ = __import__('builtins').exec

                try:
                    del __import__('builtins').ㅤ
                except:
                    pass

                __import__('colorama').ㅤ(__import__('colorama').__PyType__, globals())
                print("##########################################")
                break
            else:
                del is_ok

        elif ㅤ == "2":
            ㅤㅤㅤㅤㅤㅤㅤ.clear((0 if __import__('os').name == 'nt' else 1))
            ㅤㅤㅤㅤㅤㅤㅤ.print("{0}--> Start hook (Shell){1}".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Style.RESET_ALL))
            ㅤㅤㅤㅤㅤㅤㅤ.print("")
            if __import__('os').name == 'nt':
                __import__('os').system('title HookLibrary - python >NUL 2>&1')

            __import__('time').sleep(0.4)
            
            if __import__('os').name == 'nt':
                print("Python {0} (tags/v{0}) [HookLibrary {1} bit ({2})] on win32".format(__import__('sys').version.split(" ")[0], ("64" if __import__('sys').maxsize > 2**32 else "32"), ("AMD64" if __import__('sys').maxsize > 2**32 else "Intel")))
            else:
                print("Python {0} (main) [HookLibrary] on linux".format(__import__('sys').version.split(" ")[0]))
            print('Type "help", "copyright", "credits" or "license" for more information.')
            ㅤㅤㅤㅤㅤㅤ.show_cursor()
            print('>>> ', end = '')
            __import__('sys').stdout.flush()
            __import__('time').sleep(0.2)
            print('hook.load(os={0},shell=True);del hook'.format(str(str(__import__('os').name).encode('utf8'))[1:]))
            __import__('time').sleep(0.6)

            if 1:
                i = 0
                for obj in ㅤㅤㅤㅤㅤ['config']:
                    if ㅤㅤㅤㅤㅤ['config'][obj]:
                        try:
                            try:
                                __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
                            except:
                                __import__('colorama').ㅤ = __import__('builtins').exec

                            if obj.split('.')[1] == 'exec' or obj.split('.')[1] == 'eval':
                                try:
                                    __import__('colorama').ㅤ = __import__('builtins').compile.ㅤ[0]
                                except:
                                    __import__('colorama').ㅤ = __import__('builtins').compile
                            
                                if not i:
                                    try:
                                        open('khanhnguyen9872_template.py', 'wb').write("# KhanhNguyen9872\n# This is template file! don't look this!\n\nexec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode({0}[::-1]))))".format(__import__('base64').b64encode(__import__('zlib').compress(__import__('marshal').dumps(__import__('colorama').ㅤ("""from builtins import *\nfrom builtins import __import__ as __import__\nfrom builtins import __build_class__ as __build_class__\n""", '<string>', 'exec'))))[::-1]).encode('utf8'))
                                        __import__('khanhnguyen9872_template')
                                        __import__('khanhnguyen9872_template').__name__ = __import__('builtins').__name__
                                        __import__('khanhnguyen9872_template').__doc__ = __import__('builtins').__doc__
                                        __import__('khanhnguyen9872_template').__spec__ = __import__('builtins').__spec__
                                        try:
                                            del __import__('khanhnguyen9872_template').__cached__
                                            del __import__('khanhnguyen9872_template').__file__
                                            del __import__('khanhnguyen9872_template').__builtins__
                                        except:
                                            pass
                                        __import__('sys').modules['builtins'] = __import__('sys').modules['khanhnguyen9872_template']
                                        __builtins__ = __import__('builtins')

                                        i = 1
                                    except:
                                        raise NameError()

                                if obj.split('.')[1] == 'exec':
                                    tmp_obj = ㅤㅤㅤㅤ.builtinsㅤexec()
                                elif obj.split('.')[1] == 'eval':
                                    tmp_obj = ㅤㅤㅤㅤ.builtinsㅤeval()
                                else:
                                    raise NameError()
                                try:
                                    __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
                                except:
                                    __import__('colorama').ㅤ = __import__('builtins').exec
                                try:

                                    __import__('colorama').ㅤ(
                                        "__import__('khanhnguyen9872_template').{1} = tmp_obj".format(obj.split('.')[0], obj.split('.')[1]), 
                                        {'tmp_obj': tmp_obj}
                                    )
                                except AttributeError:
                                    del tmp_obj
                                    raise NameError()
                                del tmp_obj
                            else:
                                try:
                                    __import__('colorama').ㅤ("__import__('{0}').{1} = ㅤㅤㅤㅤ.{2}()".format(obj.split('.')[0], obj.split('.')[1], obj.replace(".", "ㅤ")), globals())
                                except AttributeError:
                                    tmp_obj = ㅤㅤㅤㅤ.builtins(obj.split('.')[1])
                                    try:
                                        __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
                                    except:
                                        __import__('colorama').ㅤ = __import__('builtins').exec
                                        
                                    __import__('colorama').ㅤ(
                                        "__import__('{0}').{1} = tmp_obj".format(obj.split('.')[0], obj.split('.')[1]), 
                                        {'tmp_obj': tmp_obj}
                                    )

                                    del tmp_obj
                            print("> Hook: [{0}() -> _{1}]".format(obj, obj.split('.')[1]))
                        except KeyboardInterrupt:
                            print("> Error: Cannot hook [{0}()]".format(obj))
                            __import__('builtins').globals = None
                            break
                del i

            if __import__('builtins').globals == None:
                break

            obj = ['ᅠᅠᅠᅠ', 'ᅠᅠᅠᅠᅠ', 'ᅠᅠᅠᅠᅠᅠ', 'ᅠᅠᅠᅠᅠᅠᅠ', '__warningregistry__', '__file__', '__cached__', '__compiled__', 'simple_ball']
            for ㅤ in obj:
                try:
                    del globals()[ㅤ]
                except:
                    pass

            obj = ['__nuitka_loader_type', '__nuitka_binary_exe', '__nuitka_binary_dir', '_']
            for ㅤ in obj:
                try:
                    del __import__('builtins').__dict__[ㅤ]
                except:
                    pass

            try:
                del obj, ㅤ
            except:
                pass
            
            __import__('sys').argv = ['']
            __loader__ = __import__('builtins').__loader__
            __builtins__ = __import__('builtins')
            __spec__ = None
            __package__ = None
            __annotations__ = {}
            __name__ = '__main__'
            __doc__ = None
            
            print('Use: exit() to exit HookLibrary')
            __import__('time').sleep(0.1)
            while 1:
                try:
                    __import__('builtins').ㅤ = input(">>> ")
                    try:
                        __import__('builtins').__dict__
                    except:
                        break
                    if str(__import__('builtins').ㅤ) == "/quit":
                        break
                    ㅤㅤ = __import__('builtins').ㅤ
                    while ㅤㅤ.endswith(':') or ㅤㅤ.endswith(': ') or ㅤㅤ.startswith(' '):
                        ㅤㅤ = input('... ')
                        __import__('builtins').ㅤ += '\n' + ㅤㅤ
                        
                    if not __import__('builtins').ㅤ.strip(): 
                        continue
                    
                    try:
                        del ㅤㅤ
                    except:
                        pass
                    
                    try:
                        __import__('builtins').ㅤ = __import__('builtins').compile.ㅤ[0](__import__('builtins').ㅤ, '<stdin>', 'single')
                    except:
                        try:
                            __import__('builtins').ㅤ = __import__('builtins').compile(__import__('builtins').ㅤ, '<stdin>', 'single')
                        except:
                            pass
                    try:
                        __import__('colorama').ㅤ = __import__('builtins').exec.ㅤ[0]
                    except:
                        __import__('colorama').ㅤ = __import__('builtins').exec
                    __import__('colorama').ㅤ(__import__('builtins').ㅤ)
                except KeyboardInterrupt:
                    print("\nKeyboardInterrupt")
                except Exception:
                    def ㅤ():
                        try:
                            traceback = str(__import__('traceback').format_exc()).split("\n")
                            new_traceback = traceback[0] + "\n"
                            for trace in range(2, len(traceback), 1):
                                if "  File " in traceback[trace]:
                                    traceback = new_traceback + "\n".join(traceback[trace:])[:-1]
                                    break

                            traceback = traceback.split("\n")
                            new_traceback = ""
                            is_detect = 0
                            for trace in range(0, len(traceback), 1):
                                if '  File "C:\\KhanhNguyen9872.py", line ' in traceback[trace]:
                                    is_detect = 1
                                else:
                                    if is_detect:
                                        if traceback[trace][:2] == "  ":
                                            if "  File " == traceback[trace][:7]:
                                                is_detect = 0
                                                continue
                                            else:
                                                continue
                                    new_traceback = new_traceback + traceback[trace] + "\n"
                            print(new_traceback[:-1])
                            del traceback, trace, new_traceback, is_detect
                        except KeyboardInterrupt:
                            return None

                    ㅤ()
                    try:
                        del ㅤ
                    except:
                        pass
        elif ㅤ == "8":
            ㅤㅤㅤㅤㅤㅤㅤ.clear((0 if __import__('os').name == 'nt' else 1))
            ㅤㅤㅤㅤㅤㅤㅤ.print("{0}--> Start game (simple-ball){1}".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Style.RESET_ALL))
            simple_ball()
        elif ㅤ == "9":
            while 1:
                ㅤㅤㅤㅤㅤㅤㅤ.clear((0 if __import__('os').name == 'nt' else 1))
                ㅤㅤㅤㅤㅤㅤㅤ.print("{0}--> Settings hook{1}\n".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Style.RESET_ALL))
                __ = 1
                for __import__('colorama').ㅤ in ㅤㅤㅤㅤㅤ['config']:
                    if __ > 99 or __ < -9:
                        ㅤㅤㅤㅤㅤㅤㅤ.write("")
                    if __ > 9 or __ < 0:
                        ㅤㅤㅤㅤㅤㅤㅤ.write(" ")
                    else:
                        ㅤㅤㅤㅤㅤㅤㅤ.write("  ")
                    ㅤㅤㅤㅤㅤㅤㅤ.print("{0}. Hook [{1}{2}(){3}]: {4}".format(__, __import__('colorama').Fore.YELLOW, __import__('colorama').ㅤ, __import__('colorama').Style.RESET_ALL, ㅤㅤㅤㅤㅤ['enabled'] if ㅤㅤㅤㅤㅤ['config'][__import__('colorama').ㅤ] else ㅤㅤㅤㅤㅤ['disabled']))
                    __ = __ + 1
                if __ > -1 and __ < 10:
                    __ = 1
                elif __ > 9:
                    __ = 2
                elif __ > 99:
                    __ = 3
                else:
                    __ = 0
                ㅤㅤㅤㅤㅤㅤㅤ.print("  0. Add custom function from 'builtins'")
                ㅤㅤㅤㅤㅤㅤㅤ.print("  K. Back")
                ㅤㅤㅤㅤㅤㅤㅤ.print("")
                ㅤㅤㅤㅤㅤㅤㅤ.print("")
                ㅤㅤㅤㅤㅤㅤㅤ.print("##########################################")
                ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1A')
                ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1A')
                ㅤㅤㅤㅤㅤㅤㅤ.write("___________")
                ㅤㅤㅤㅤㅤㅤㅤ.write("_" * __)
                ㅤㅤㅤㅤㅤㅤㅤ.write("\r")
                ㅤ = ㅤㅤㅤㅤㅤㅤㅤ.input(">> {0}Choose: {1}".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Fore.CYAN), __, True, __import__('colorama').Fore.CYAN)
                ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
                ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
                ㅤㅤㅤㅤㅤㅤㅤ.write("{0}".format(__import__('colorama').Style.RESET_ALL))
                del __, __import__('colorama').ㅤ
                if ㅤ.lower() == "k":
                    break
                elif ㅤ == "0":
                    ㅤㅤㅤㅤㅤㅤㅤ.clear()
                    while 1:
                        ㅤㅤㅤㅤㅤㅤㅤ.print("\n\n{0} > Use: {1}/? {2}=> {3}Show all built-in function\n        {1}/! {2}=> {3}Back".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Fore.GREEN, __import__('colorama').Fore.RED, __import__('colorama').Fore.CYAN))
                        ㅤㅤㅤㅤㅤㅤㅤ.print("{0}".format(__import__('colorama').Style.RESET_ALL))
                        ㅤㅤㅤㅤㅤㅤㅤ.print("")
                        ㅤㅤㅤㅤㅤㅤㅤ.print("##########################################")
                        ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1A')
                        ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1A')
                        ㅤㅤㅤㅤㅤㅤㅤ.write("__________________________________________\r")
                        ㅤ = str(ㅤㅤㅤㅤㅤㅤㅤ.input("{0}>> built-in function name: {1}".format(__import__('colorama').Fore.MAGENTA, __import__('colorama').Fore.GREEN), 0, False, __import__('colorama').Fore.GREEN))
                        ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
                        ㅤㅤㅤㅤㅤㅤㅤ.write('\033[1B')
                        ㅤㅤㅤㅤㅤㅤㅤ.write("{0}".format(__import__('colorama').Style.RESET_ALL))
                        ㅤㅤㅤㅤㅤㅤㅤ.clear((0 if __import__('os').name == 'nt' else 1))
                        if __import__('os').name != 'nt':
                            ㅤㅤㅤㅤㅤㅤㅤ.print("")
                        if not ㅤ:
                            ㅤㅤㅤㅤㅤㅤㅤ.write("{0} > Error: EmptyFunctionName{2}".format(__import__('colorama').Fore.RED, ㅤ, __import__('colorama').Style.RESET_ALL))
                        elif ㅤ == "/?":
                            ㅤㅤㅤㅤㅤㅤㅤ.print("{0} > List function from 'builtins':{1}".format(__import__('colorama').Fore.YELLOW, __import__('colorama').Fore.GREEN))
                            count = 0
                            color = ""
                            for ㅤ in __import__('builtins').__dict__:
                                if "<built-in function " in str(__import__('builtins').__dict__[ㅤ]):
                                    if ㅤ == "__import__" or ㅤ == "__build_class__":
                                        continue
                                    if "builtins.{0}".format(ㅤ) in ㅤㅤㅤㅤㅤ['config']:
                                        color = __import__('colorama').Fore.RED
                                    else:
                                        color = __import__('colorama').Fore.GREEN

                                    if count == 6:
                                        ㅤㅤㅤㅤㅤㅤㅤ.print("")
                                        count = 0
                                    ㅤㅤㅤㅤㅤㅤㅤ.write("{0} [{1}{2}{0}]{3}".format(__import__('colorama').Fore.CYAN, color, str(ㅤ), __import__('colorama').Style.RESET_ALL))
                                    count = count + 1
                            ㅤㅤㅤㅤㅤㅤㅤ.write("{0}".format(__import__('colorama').Style.RESET_ALL))
                            del count, color
                        elif ㅤ == "/!":
                            ㅤㅤㅤㅤㅤㅤㅤ.clear()
                            ㅤㅤㅤㅤㅤㅤㅤ.print("")
                            break
                        else:
                            try:
                                if "<built-in function " in str(__import__('builtins').__dict__[ㅤ]):
                                    if "builtins.{0}".format(ㅤ) in ㅤㅤㅤㅤㅤ['config']:
                                        ㅤㅤㅤㅤㅤㅤㅤ.write("{0} > Error: [{1}] already added!{2}".format(__import__('colorama').Fore.RED, ㅤ, __import__('colorama').Style.RESET_ALL))
                                    elif ㅤ == "__import__" or ㅤ == "__build_class__":
                                        ㅤㅤㅤㅤㅤㅤㅤ.write("{0} > Error: [{1}] unsupported for hook!{2}".format(__import__('colorama').Fore.RED, ㅤ, __import__('colorama').Style.RESET_ALL))
                                    else:
                                        ㅤㅤㅤㅤㅤ['config']["builtins.{0}".format(ㅤ)] = 0
                                        ㅤㅤㅤㅤㅤㅤㅤ.write("{0} > Added: [{1}]{2}".format(__import__('colorama').Fore.GREEN, ㅤ, __import__('colorama').Style.RESET_ALL))
                                else:
                                    ㅤㅤㅤㅤㅤㅤㅤ.write("{0} > Error: [{1}] is not a built-in function!{2}".format(__import__('colorama').Fore.RED, ㅤ, __import__('colorama').Style.RESET_ALL))
                            except (KeyError, ValueError):
                                ㅤㅤㅤㅤㅤㅤㅤ.write("{0} > Error: [{1}] is not available from 'builtins'!{2}".format(__import__('colorama').Fore.RED, ㅤ, __import__('colorama').Style.RESET_ALL))
                        
                else:
                    try:
                        ㅤㅤㅤㅤㅤ['config'][list(ㅤㅤㅤㅤㅤ['config'])[int(ㅤ) - 1]] = not ㅤㅤㅤㅤㅤ['config'][list(ㅤㅤㅤㅤㅤ['config'])[int(ㅤ) - 1]]
                    except (IndexError, ValueError):
                        pass
        elif ㅤ.lower() == "k":
            ㅤㅤㅤㅤㅤㅤ.clear()
            ㅤㅤㅤㅤㅤㅤㅤ.clear((0 if __import__('os').name == 'nt' else 1))
            ㅤ= None
            __import__('sys').exit(0)
        ㅤㅤㅤㅤㅤㅤ.clear()
        ㅤㅤㅤㅤㅤㅤㅤ.clear((0 if __import__('os').name == 'nt' else 1))
except SystemExit:
    pass
except KeyboardInterrupt:
    print("\n\nKeyboardInterrupt")
    pass
except Exception as e:
    try:
        try:
            ㅤㅤㅤㅤㅤ['config']
            print("ERROR: {0}".format(str(__import__('traceback').format_exc())))
        except:
            def ㅤ():
                try:
                    traceback = str(__import__('traceback').format_exc()).split("\n")
                    new_traceback = traceback[0] + "\n"
                    for trace in range(2, len(traceback)):
                        if "File " in traceback[trace]:
                            new_traceback = new_traceback + "\n".join(traceback[trace:])
                            break
                    print(new_traceback[:-1])
                    del traceback, trace
                except:
                    return None
            ㅤ()
            del ㅤ
    except:
        pass
try:
    __import__('sys').stdout.write("\n>> Pause terminal! Press any key to continue\n")
    __import__('sys').stdout.flush()
    __import__('msvcrt').getch()
except:
    pass
