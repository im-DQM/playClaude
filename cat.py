import os
import sys
import time

CLEAR = "\033[2J\033[H"
HOME = "\033[H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
RESET = "\033[0m"
ORANGE = "\033[38;5;208m"
PINK = "\033[38;5;218m"
CYAN = "\033[38;5;81m"
DIM = "\033[2m"


def enable_ansi():
    # Windows 终端默认不开 ANSI,执行一次空命令即可开启
    if os.name == "nt":
        os.system("")
    # 默认编码是 GBK,无法输出 ♪ 等字符,统一改成 UTF-8
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


ART = """\
{color}       /\\_/\\{reset}
{color}      ( {eyes} ){tail}{reset}
{color}       > {mouth} <{reset}
{color}      /     \\{reset}
"""

TAILS = ["  ~", "  \\", "  |", "  /", "  -"]
EYES = ["o.o", "o.o", "o.o", "-.-", "-.-", "o.o", "o.o", "^.^"]
MOUTHS = ["^", "^", "w", "^", "o", "^"]


def render(tick):
    eyes = EYES[tick % len(EYES)]
    mouth = MOUTHS[(tick // 2) % len(MOUTHS)]
    tail = TAILS[tick % len(TAILS)]
    return ART.format(
        color=ORANGE,
        reset=RESET,
        eyes=eyes,
        mouth=mouth,
        tail=tail,
    )


def banner():
    return (
        f"{PINK}        ~ 一只咕嘎小猫 ~{RESET}\n"
        f"{DIM}     (按 Ctrl+C 退出){RESET}\n"
    )


def main():
    enable_ansi()

    # 可选参数:python cat.py 30  ->  只播放 30 帧后退出(方便测试)
    limit = None
    if len(sys.argv) > 1:
        try:
            limit = int(sys.argv[1])
        except ValueError:
            limit = None

    tick = 0
    sys.stdout.write(HIDE_CURSOR)
    try:
        while limit is None or tick < limit:
            sys.stdout.write(CLEAR)
            sys.stdout.write(banner())
            sys.stdout.write("\n")
            sys.stdout.write(render(tick))
            sys.stdout.write(f"\n{CYAN}          ♪ 喵~{RESET}\n")
            sys.stdout.flush()
            time.sleep(0.12)
            tick += 1
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(SHOW_CURSOR + RESET + CLEAR)
        sys.stdout.flush()
        print("小猫跑走啦,拜拜~  咕嘎")


if __name__ == "__main__":
    main()
