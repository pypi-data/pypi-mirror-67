# coding=utf-8
import time

'''
 :Description:    控件类
 :author          bony
 :@version         V1.1
 :@Date            2020年05月
'''


class KEYCODE_HOME:
    NAME = "按键Home"
    CODE = "KEYCODE_HOME"
    ID = "3"


class KEYCODE_BACK:
    NAME = "返回键"
    CODE = "KEYCODE_BACK"
    ID = "4"


class KEYCODE_CALL:
    NAME = "拨号键"
    CODE = "KEYCODE_CALL"
    ID = "5"


class KEYCODE_ENDCALL:
    NAME = "挂机键"
    CODE = "KEYCODE_ENDCALL"
    ID = "6"


class KEYCODE_0:
    NAME = "按键'0'"
    CODE = "KEYCODE_0"
    ID = "7"


class KEYCODE_1:
    NAME = "按键'1'"
    CODE = "KEYCODE_1"
    ID = "8"


class KEYCODE_2:
    NAME = "按键'2'"
    CODE = "KEYCODE_2"
    ID = "9"


class KEYCODE_3:
    NAME = "按键'3'"
    CODE = "KEYCODE_3"
    ID = "10"


class KEYCODE_4:
    NAME = "按键'4'"
    CODE = "KEYCODE_4"
    ID = "11"


class KEYCODE_5:
    NAME = "按键'5'"
    CODE = "KEYCODE_5"
    ID = "12"


class KEYCODE_6:
    NAME = "按键'6'"
    CODE = "KEYCODE_6"
    ID = "13"


class KEYCODE_7:
    NAME = "按键'7'"
    CODE = "KEYCODE_7"
    ID = "14"


class KEYCODE_8:
    NAME = "按键'8'"
    CODE = "KEYCODE_8"
    ID = "15"


class KEYCODE_9:
    NAME = "按键'9'"
    CODE = "KEYCODE_9"
    ID = "16"


class KEYCODE_DPAD_UP:
    NAME = "导航键 向上"
    CODE = "KEYCODE_DPAD_UP"
    ID = "19"


class KEYCODE_DPAD_DOWN:
    NAME = "导航键 向下"
    CODE = "KEYCODE_DPAD_DOWN"
    ID = "20"


class KEYCODE_DPAD_LEFT:
    NAME = "导航键 向左"
    CODE = "KEYCODE_DPAD_LEFT"
    ID = "21"


class KEYCODE_DPAD_RIGHT:
    NAME = "导航键 向右"
    CODE = "KEYCODE_DPAD_RIGHT"
    ID = "22"


class KEYCODE_DPAD_CENTER:
    NAME = "导航键 确定键"
    CODE = "KEYCODE_DPAD_CENTER"
    ID = "23"


class KEYCODE_VOLUME_UP:
    NAME = "音量增加键"
    CODE = "KEYCODE_VOLUME_UP"
    ID = "24"


class KEYCODE_VOLUME_DOWN:
    NAME = "音量减小键"
    CODE = "KEYCODE_VOLUME_DOWN"
    ID = "25"


class KEYCODE_POWER:
    NAME = "电源键"
    CODE = "KEYCODE_POWER"
    ID = "26"


class KEYCODE_CAMERA:
    NAME = "拍照键"
    CODE = "KEYCODE_CAMERA"
    ID = "27"


class KEYCODE_A:
    NAME = "按键'A'"
    CODE = "KEYCODE_A"
    ID = "29"


class KEYCODE_B:
    NAME = "按键'B'"
    CODE = "KEYCODE_B"
    ID = "30"


class KEYCODE_C:
    NAME = "按键'C'"
    CODE = "KEYCODE_C"
    ID = "31"


class KEYCODE_D:
    NAME = "按键'D'"
    CODE = "KEYCODE_D"
    ID = "32"


class KEYCODE_E:
    NAME = "按键'E'"
    CODE = "KEYCODE_E"
    ID = "33"


class KEYCODE_F:
    NAME = "按键'F'"
    CODE = "KEYCODE_F"
    ID = "34"


class KEYCODE_G:
    NAME = "按键'G'"
    CODE = "KEYCODE_G"
    ID = "35"


class KEYCODE_H:
    NAME = "按键'H'"
    CODE = "KEYCODE_H"
    ID = "36"


class KEYCODE_I:
    NAME = "按键'I'"
    CODE = "KEYCODE_I"
    ID = "37"


class KEYCODE_J:
    NAME = "按键'J'"
    CODE = "KEYCODE_J"
    ID = "38"


class KEYCODE_K:
    NAME = "按键'K'"
    CODE = "KEYCODE_K"
    ID = "39"


class KEYCODE_L:
    NAME = "按键'L'"
    CODE = "KEYCODE_L"
    ID = "40"


class KEYCODE_M:
    NAME = "按键'M'"
    CODE = "KEYCODE_M"
    ID = "41"


class KEYCODE_N:
    NAME = "按键'N'"
    CODE = "KEYCODE_N"
    ID = "42"


class KEYCODE_O:
    NAME = "按键'O'"
    CODE = "KEYCODE_O"
    ID = "43"


class KEYCODE_P:
    NAME = "按键'P'"
    CODE = "KEYCODE_P"
    ID = "44"


class KEYCODE_Q:
    NAME = "按键'Q'"
    CODE = "KEYCODE_Q"
    ID = "45"


class KEYCODE_R:
    NAME = "按键'R'"
    CODE = "KEYCODE_R"
    ID = "46"


class KEYCODE_S:
    NAME = "按键'S'"
    CODE = "KEYCODE_S"
    ID = "47"


class KEYCODE_T:
    NAME = "按键'T'"
    CODE = "KEYCODE_T"
    ID = "48"


class KEYCODE_U:
    NAME = "按键'U'"
    CODE = "KEYCODE_U"
    ID = "49"


class KEYCODE_V:
    NAME = "按键'V'"
    CODE = "KEYCODE_V"
    ID = "50"


class KEYCODE_W:
    NAME = "按键'W'"
    CODE = "KEYCODE_W"
    ID = "51"


class KEYCODE_X:
    NAME = "按键'X'"
    CODE = "KEYCODE_X"
    ID = "52"


class KEYCODE_Y:
    NAME = "按键'Y'"
    CODE = "KEYCODE_Y"
    ID = "53"


class KEYCODE_Z:
    NAME = "按键'Z'"
    CODE = "KEYCODE_Z"
    ID = "54"


class KEYCODE_TAB:
    NAME = "Tab键"
    CODE = "KEYCODE_TAB"
    ID = "61"


class KEYCODE_ENTER:
    NAME = "回车键"
    CODE = "KEYCODE_ENTER"
    ID = "66"


class KEYCODE_DEL:
    NAME = "退格键"
    CODE = "KEYCODE_DEL"
    ID = "67"


class KEYCODE_FOCUS:
    NAME = "拍照对焦键"
    CODE = "KEYCODE_FOCUS"
    ID = "80"


class KEYCODE_MENU:
    NAME = "菜单键"
    CODE = "KEYCODE_MENU"
    ID = "82"


class KEYCODE_NOTIFICATION:
    NAME = "通知键"
    CODE = "KEYCODE_NOTIFICATION"
    ID = "83"


class KEYCODE_SEARCH:
    NAME = "搜索键"
    CODE = "KEYCODE_SEARCH"
    ID = "84"


class KEYCODE_MUTE:
    NAME = "话筒静音键"
    CODE = "KEYCODE_MUTE"
    ID = "91"


class KEYCODE_PAGE_UP:
    NAME = "向上翻页键"
    CODE = "KEYCODE_PAGE_UP"
    ID = "92"


class KEYCODE_PAGE_DOWN:
    NAME = "向下翻页键"
    CODE = "KEYCODE_PAGE_DOWN"
    ID = "93"


class KEYCODE_ESCAPE:
    NAME = "ESC键"
    CODE = "KEYCODE_ESCAPE"
    ID = "111"


class KEYCODE_FORWARD_DEL:
    NAME = "删除键"
    CODE = "KEYCODE_FORWARD_DEL"
    ID = "112"


class KEYCODE_CAPS_LOCK:
    NAME = "大写锁定键"
    CODE = "KEYCODE_CAPS_LOCK"
    ID = "115"


class KEYCODE_SCROLL_LOCK:
    NAME = "滚动锁定键"
    CODE = "KEYCODE_SCROLL_LOCK"
    ID = "116"


class KEYCODE_BREAK:
    NAME = "Break/Pause键"
    CODE = "KEYCODE_BREAK"
    ID = "121"


class KEYCODE_MOVE_HOME:
    NAME = "光标移动到开始键"
    CODE = "KEYCODE_MOVE_HOME"
    ID = "122"


class KEYCODE_MOVE_END:
    NAME = "光标移动到末尾键"
    CODE = "KEYCODE_MOVE_END"
    ID = "123"


class KEYCODE_INSERT:
    NAME = "插入键"
    CODE = "KEYCODE_INSERT"
    ID = "124"


class KEYCODE_NUM_LOCK:
    NAME = "小键盘锁"
    CODE = "KEYCODE_NUM_LOCK"
    ID = "143"


class KEYCODE_VOLUME_MUTE:
    NAME = "扬声器静音键"
    CODE = "KEYCODE_VOLUME_MUTE"
    ID = "164"


class KEYCODE_ZOOM_IN:
    NAME = "放大键"
    CODE = "KEYCODE_ZOOM_IN"
    ID = "168"


class KEYCODE_ZOOM_OUT:
    NAME = "缩小键"
    CODE = "KEYCODE_ZOOM_OUT"
    ID = "169"


class KEYCODE_ALT_LEFT:
    NAME = "Alt+Left"
    CODE = "KEYCODE_ALT_LEFT"
    ID = "null"


class KEYCODE_ALT_RIGHT:
    NAME = "Alt+Right"
    CODE = "KEYCODE_ALT_RIGHT"
    ID = "null"


class KEYCODE_CTRL_LEFT:
    NAME = "Control+Left"
    CODE = "KEYCODE_CTRL_LEFT"
    ID = "null"


class KEYCODE_CTRL_RIGHT:
    NAME = "Control+Right"
    CODE = "KEYCODE_CTRL_RIGHT"
    ID = "null"


class KEYCODE_SHIFT_LEFT:
    NAME = "Shift+Left"
    CODE = "KEYCODE_SHIFT_LEFT"
    ID = "null"


class KEYCODE_SHIFT_RIGHT:
    NAME = "Shift+Right"
    CODE = "KEYCODE_SHIFT_RIGHT"
    ID = "null"


class KEYCODE_PLUS:
    NAME = "按键'+'"
    CODE = "KEYCODE_PLUS"
    ID = "null"


class KEYCODE_MINUS:
    NAME = "按键'-'"
    CODE = "KEYCODE_MINUS"
    ID = "null"


class KEYCODE_STAR:
    NAME = "按键'*'"
    CODE = "KEYCODE_STAR"
    ID = "null"


class KEYCODE_SLASH:
    NAME = "按键'/'"
    CODE = "KEYCODE_SLASH"
    ID = "null"


class KEYCODE_EQUALS:
    NAME = "按键'='"
    CODE = "KEYCODE_EQUALS"
    ID = "null"


class KEYCODE_AT:
    NAME = "按键'@'"
    CODE = "KEYCODE_AT"
    ID = "null"


class KEYCODE_POUND:
    NAME = "按键'#'"
    CODE = "KEYCODE_POUND"
    ID = "null"


class KEYCODE_APOSTROPHE:
    NAME = "按键''' (单引号)"
    CODE = "KEYCODE_APOSTROPHE"
    ID = "null"


class KEYCODE_BACKSLASH:
    NAME = "按键'\'"
    CODE = "KEYCODE_BACKSLASH"
    ID = "null"


class KEYCODE_COMMA:
    NAME = "按键','"
    CODE = "KEYCODE_COMMA"
    ID = "null"


class KEYCODE_PERIOD:
    NAME = "按键'.'"
    CODE = "KEYCODE_PERIOD"
    ID = "null"


class KEYCODE_LEFT_BRACKET:
    NAME = "按键'['"
    CODE = "KEYCODE_LEFT_BRACKET"
    ID = "null"


class KEYCODE_RIGHT_BRACKET:
    NAME = "按键']'"
    CODE = "KEYCODE_RIGHT_BRACKET"
    ID = "null"


class KEYCODE_SEMICOLON:
    NAME = "按键';'"
    CODE = "KEYCODE_SEMICOLON"
    ID = "null"


class KEYCODE_GRAVE:
    NAME = "按键'`'"
    CODE = "KEYCODE_GRAVE"
    ID = "null"


class KEYCODE_SPACE:
    NAME = "空格键"
    CODE = "KEYCODE_SPACE"
    ID = "null"


class KEYCODE_NUMPAD_0:
    NAME = "小键盘按键'0'"
    CODE = "KEYCODE_NUMPAD_0"
    ID = "null"


class KEYCODE_NUMPAD_1:
    NAME = "小键盘按键'1'"
    CODE = "KEYCODE_NUMPAD_1"
    ID = "null"


class KEYCODE_NUMPAD_2:
    NAME = "小键盘按键'2'"
    CODE = "KEYCODE_NUMPAD_2"
    ID = "null"


class KEYCODE_NUMPAD_3:
    NAME = "小键盘按键'3'"
    CODE = "KEYCODE_NUMPAD_3"
    ID = "null"


class KEYCODE_NUMPAD_4:
    NAME = "小键盘按键'4'"
    CODE = "KEYCODE_NUMPAD_4"
    ID = "null"


class KEYCODE_NUMPAD_5:
    NAME = "小键盘按键'5'"
    CODE = "KEYCODE_NUMPAD_5"
    ID = "null"


class KEYCODE_NUMPAD_6:
    NAME = "小键盘按键'6'"
    CODE = "KEYCODE_NUMPAD_6"
    ID = "null"


class KEYCODE_NUMPAD_7:
    NAME = "小键盘按键'7'"
    CODE = "KEYCODE_NUMPAD_7"
    ID = "null"


class KEYCODE_NUMPAD_8:
    NAME = "小键盘按键'8'"
    CODE = "KEYCODE_NUMPAD_8"
    ID = "null"


class KEYCODE_NUMPAD_9:
    NAME = "小键盘按键'9'"
    CODE = "KEYCODE_NUMPAD_9"
    ID = "null"


class KEYCODE_NUMPAD_ADD:
    NAME = "小键盘按键'+'"
    CODE = "KEYCODE_NUMPAD_ADD"
    ID = "null"


class KEYCODE_NUMPAD_SUBTRACT:
    NAME = "小键盘按键'-'"
    CODE = "KEYCODE_NUMPAD_SUBTRACT"
    ID = "null"


class KEYCODE_NUMPAD_MULTIPLY:
    NAME = "小键盘按键'*'"
    CODE = "KEYCODE_NUMPAD_MULTIPLY"
    ID = "null"


class KEYCODE_NUMPAD_DIVIDE:
    NAME = "小键盘按键'/'"
    CODE = "KEYCODE_NUMPAD_DIVIDE"
    ID = "null"


class KEYCODE_NUMPAD_EQUALS:
    NAME = "小键盘按键'='"
    CODE = "KEYCODE_NUMPAD_EQUALS"
    ID = "null"


class KEYCODE_NUMPAD_COMMA:
    NAME = "小键盘按键','"
    CODE = "KEYCODE_NUMPAD_COMMA"
    ID = "null"


class KEYCODE_NUMPAD_DOT:
    NAME = "小键盘按键'.'"
    CODE = "KEYCODE_NUMPAD_DOT"
    ID = "null"


class KEYCODE_NUMPAD_LEFT_PAREN:
    NAME = "小键盘按键'('"
    CODE = "KEYCODE_NUMPAD_LEFT_PAREN"
    ID = "null"


class KEYCODE_NUMPAD_RIGHT_PAREN:
    NAME = "小键盘按键')'"
    CODE = "KEYCODE_NUMPAD_RIGHT_PAREN"
    ID = "null"


class KEYCODE_NUMPAD_ENTER:
    NAME = "小键盘按键回车"
    CODE = "KEYCODE_NUMPAD_ENTER"
    ID = "null"


class KEYCODE_F1:
    NAME = "按键F1"
    CODE = "KEYCODE_F1"
    ID = "null"


class KEYCODE_F2:
    NAME = "按键F2"
    CODE = "KEYCODE_F2"
    ID = "null"


class KEYCODE_F3:
    NAME = "按键F3"
    CODE = "KEYCODE_F3"
    ID = "null"


class KEYCODE_F4:
    NAME = "按键F4"
    CODE = "KEYCODE_F4"
    ID = "null"


class KEYCODE_F5:
    NAME = "按键F5"
    CODE = "KEYCODE_F5"
    ID = "null"


class KEYCODE_F6:
    NAME = "按键F6"
    CODE = "KEYCODE_F6"
    ID = "null"


class KEYCODE_F7:
    NAME = "按键F7"
    CODE = "KEYCODE_F7"
    ID = "null"


class KEYCODE_F8:
    NAME = "按键F8"
    CODE = "KEYCODE_F8"
    ID = "null"


class KEYCODE_F9:
    NAME = "按键F9"
    CODE = "KEYCODE_F9"
    ID = "null"


class KEYCODE_F10:
    NAME = "按键F10"
    CODE = "KEYCODE_F10"
    ID = "null"


class KEYCODE_F11:
    NAME = "按键F11"
    CODE = "KEYCODE_F11"
    ID = "null"


class KEYCODE_F12:
    NAME = "按键F12"
    CODE = "KEYCODE_F12"
    ID = "null"


class KEYCODE_MEDIA_PLAY:
    NAME = "多媒体键 播放"
    CODE = "KEYCODE_MEDIA_PLAY"
    ID = "null"


class KEYCODE_MEDIA_STOP:
    NAME = "多媒体键 停止"
    CODE = "KEYCODE_MEDIA_STOP"
    ID = "null"


class KEYCODE_MEDIA_PAUSE:
    NAME = "多媒体键 暂停"
    CODE = "KEYCODE_MEDIA_PAUSE"
    ID = "null"


class KEYCODE_MEDIA_PLAY_PAUSE:
    NAME = "多媒体键 播放/暂停"
    CODE = "KEYCODE_MEDIA_PLAY_PAUSE"
    ID = "null"


class KEYCODE_MEDIA_FAST_FORWARD:
    NAME = "多媒体键 快进"
    CODE = "KEYCODE_MEDIA_FAST_FORWARD"
    ID = "null"


class KEYCODE_MEDIA_REWIND:
    NAME = "多媒体键 快退"
    CODE = "KEYCODE_MEDIA_REWIND"
    ID = "null"


class KEYCODE_MEDIA_NEXT:
    NAME = "多媒体键 下一首"
    CODE = "KEYCODE_MEDIA_NEXT"
    ID = "null"


class KEYCODE_MEDIA_PREVIOUS:
    NAME = "多媒体键 上一首"
    CODE = "KEYCODE_MEDIA_PREVIOUS"
    ID = "null"


class KEYCODE_MEDIA_CLOSE:
    NAME = "多媒体键 关闭"
    CODE = "KEYCODE_MEDIA_CLOSE"
    ID = "null"


class KEYCODE_MEDIA_EJECT:
    NAME = "多媒体键 弹出"
    CODE = "KEYCODE_MEDIA_EJECT"
    ID = "null"


class KEYCODE_MEDIA_RECORD:
    NAME = "多媒体键 录音"
    CODE = "KEYCODE_MEDIA_RECORD"
    ID = "null"


class KEYCODE_BUTTON_1:
    NAME = "通用游戏手柄按钮#1"
    CODE = "KEYCODE_BUTTON_1"
    ID = "null"


class KEYCODE_BUTTON_2:
    NAME = "通用游戏手柄按钮 #2"
    CODE = "KEYCODE_BUTTON_2"
    ID = "null"


class KEYCODE_BUTTON_3:
    NAME = "通用游戏手柄按钮 #3"
    CODE = "KEYCODE_BUTTON_3"
    ID = "null"


class KEYCODE_BUTTON_4:
    NAME = "通用游戏手柄按钮 #4"
    CODE = "KEYCODE_BUTTON_4"
    ID = "null"


class KEYCODE_BUTTON_5:
    NAME = "通用游戏手柄按钮 #5"
    CODE = "KEYCODE_BUTTON_5"
    ID = "null"


class KEYCODE_BUTTON_6:
    NAME = "通用游戏手柄按钮 #6"
    CODE = "KEYCODE_BUTTON_6"
    ID = "null"


class KEYCODE_BUTTON_7:
    NAME = "通用游戏手柄按钮 #7"
    CODE = "KEYCODE_BUTTON_7"
    ID = "null"


class KEYCODE_BUTTON_8:
    NAME = "通用游戏手柄按钮 #8"
    CODE = "KEYCODE_BUTTON_8"
    ID = "null"


class KEYCODE_BUTTON_9:
    NAME = "通用游戏手柄按钮 #9"
    CODE = "KEYCODE_BUTTON_9"
    ID = "null"


class KEYCODE_BUTTON_10:
    NAME = "通用游戏手柄按钮 #10"
    CODE = "KEYCODE_BUTTON_10"
    ID = "null"


class KEYCODE_BUTTON_11:
    NAME = "通用游戏手柄按钮 #11"
    CODE = "KEYCODE_BUTTON_11"
    ID = "null"


class KEYCODE_BUTTON_12:
    NAME = "通用游戏手柄按钮 #12"
    CODE = "KEYCODE_BUTTON_12"
    ID = "null"


class KEYCODE_BUTTON_13:
    NAME = "通用游戏手柄按钮 #13"
    CODE = "KEYCODE_BUTTON_13"
    ID = "null"


class KEYCODE_BUTTON_14:
    NAME = "通用游戏手柄按钮 #14"
    CODE = "KEYCODE_BUTTON_14"
    ID = "null"


class KEYCODE_BUTTON_15:
    NAME = "通用游戏手柄按钮 #15"
    CODE = "KEYCODE_BUTTON_15"
    ID = "null"


class KEYCODE_BUTTON_16:
    NAME = "通用游戏手柄按钮 #16"
    CODE = "KEYCODE_BUTTON_16"
    ID = "null"


class KEYCODE_BUTTON_A:
    NAME = "游戏手柄按钮 A"
    CODE = "KEYCODE_BUTTON_A"
    ID = "null"


class KEYCODE_BUTTON_B:
    NAME = "游戏手柄按钮 B"
    CODE = "KEYCODE_BUTTON_B"
    ID = "null"


class KEYCODE_BUTTON_C:
    NAME = "游戏手柄按钮 C"
    CODE = "KEYCODE_BUTTON_C"
    ID = "null"


class KEYCODE_BUTTON_X:
    NAME = "游戏手柄按钮 X"
    CODE = "KEYCODE_BUTTON_X"
    ID = "null"


class KEYCODE_BUTTON_Y:
    NAME = "游戏手柄按钮 Y"
    CODE = "KEYCODE_BUTTON_Y"
    ID = "null"


class KEYCODE_BUTTON_Z:
    NAME = "游戏手柄按钮 Z"
    CODE = "KEYCODE_BUTTON_Z"
    ID = "null"


class KEYCODE_BUTTON_L1:
    NAME = "游戏手柄按钮 L1"
    CODE = "KEYCODE_BUTTON_L1"
    ID = "null"


class KEYCODE_BUTTON_L2:
    NAME = "游戏手柄按钮 L2"
    CODE = "KEYCODE_BUTTON_L2"
    ID = "null"


class KEYCODE_BUTTON_R1:
    NAME = "游戏手柄按钮 R1"
    CODE = "KEYCODE_BUTTON_R1"
    ID = "null"


class KEYCODE_BUTTON_R2:
    NAME = "游戏手柄按钮 R2"
    CODE = "KEYCODE_BUTTON_R2"
    ID = "null"


class KEYCODE_BUTTON_MODE:
    NAME = "游戏手柄按钮 Mode"
    CODE = "KEYCODE_BUTTON_MODE"
    ID = "null"


class KEYCODE_BUTTON_SELECT:
    NAME = "游戏手柄按钮 Select"
    CODE = "KEYCODE_BUTTON_SELECT"
    ID = "null"


class KEYCODE_BUTTON_START:
    NAME = "游戏手柄按钮 Start"
    CODE = "KEYCODE_BUTTON_START"
    ID = "null"


class KEYCODE_BUTTON_THUMBL:
    NAME = "Left Thumb Button"
    CODE = "KEYCODE_BUTTON_THUMBL"
    ID = "null"


class KEYCODE_BUTTON_THUMBR:
    NAME = "Right Thumb Button"
    CODE = "KEYCODE_BUTTON_THUMBR"
    ID = "null"


class KEYCODE_NUM:
    NAME = "按键Number modifier"
    CODE = "KEYCODE_NUM"
    ID = "null"


class KEYCODE_INFO:
    NAME = "按键Info"
    CODE = "KEYCODE_INFO"
    ID = "null"


class KEYCODE_APP_SWITCH:
    NAME = "按键App switch"
    CODE = "KEYCODE_APP_SWITCH"
    ID = "null"


class KEYCODE_BOOKMARK:
    NAME = "按键Bookmark"
    CODE = "KEYCODE_BOOKMARK"
    ID = "null"


class KEYCODE_AVR_INPUT:
    NAME = "按键A/V Receiver input"
    CODE = "KEYCODE_AVR_INPUT"
    ID = "null"


class KEYCODE_AVR_POWER:
    NAME = "按键A/V Receiver power"
    CODE = "KEYCODE_AVR_POWER"
    ID = "null"


class KEYCODE_CAPTIONS:
    NAME = "按键Toggle captions"
    CODE = "KEYCODE_CAPTIONS"
    ID = "null"


class KEYCODE_CHANNEL_DOWN:
    NAME = "按键Channel down"
    CODE = "KEYCODE_CHANNEL_DOWN"
    ID = "null"


class KEYCODE_CHANNEL_UP:
    NAME = "按键Channel up"
    CODE = "KEYCODE_CHANNEL_UP"
    ID = "null"


class KEYCODE_CLEAR:
    NAME = "按键Clear"
    CODE = "KEYCODE_CLEAR"
    ID = "null"


class KEYCODE_DVR:
    NAME = "按键DVR"
    CODE = "KEYCODE_DVR"
    ID = "null"


class KEYCODE_ENVELOPE:
    NAME = "按键Envelope special function"
    CODE = "KEYCODE_ENVELOPE"
    ID = "null"


class KEYCODE_EXPLORER:
    NAME = "按键Explorer special function"
    CODE = "KEYCODE_EXPLORER"
    ID = "null"


class KEYCODE_FORWARD:
    NAME = "按键Forward"
    CODE = "KEYCODE_FORWARD"
    ID = "null"


class KEYCODE_FUNCTION:
    NAME = "按键Function modifier"
    CODE = "KEYCODE_FUNCTION"
    ID = "null"


class KEYCODE_GUIDE:
    NAME = "按键Guide"
    CODE = "KEYCODE_GUIDE"
    ID = "null"


class KEYCODE_HEADSETHOOK:
    NAME = "按键Headset Hook"
    CODE = "KEYCODE_HEADSETHOOK"
    ID = "null"


class KEYCODE_META_LEFT:
    NAME = "按键Left Meta modifier"
    CODE = "KEYCODE_META_LEFT"
    ID = "null"


class KEYCODE_META_RIGHT:
    NAME = "按键Right Meta modifier"
    CODE = "KEYCODE_META_RIGHT"
    ID = "null"


class KEYCODE_PICTSYMBOLS:
    NAME = "按键Picture Symbols modifier"
    CODE = "KEYCODE_PICTSYMBOLS"
    ID = "null"


class KEYCODE_PROG_BLUE:
    NAME = "按键Blue “programmable”"
    CODE = "KEYCODE_PROG_BLUE"
    ID = "null"


class KEYCODE_PROG_GREEN:
    NAME = "按键Green “programmable”"
    CODE = "KEYCODE_PROG_GREEN"
    ID = "null"


class KEYCODE_PROG_RED:
    NAME = "按键Red “programmable”"
    CODE = "KEYCODE_PROG_RED"
    ID = "null"


class KEYCODE_PROG_YELLOW:
    NAME = "按键Yellow “programmable”"
    CODE = "KEYCODE_PROG_YELLOW"
    ID = "null"


class KEYCODE_SETTINGS:
    NAME = "按键Settings"
    CODE = "KEYCODE_SETTINGS"
    ID = "null"


class KEYCODE_SOFT_LEFT:
    NAME = "按键Soft Left"
    CODE = "KEYCODE_SOFT_LEFT"
    ID = "null"


class KEYCODE_SOFT_RIGHT:
    NAME = "按键Soft Right"
    CODE = "KEYCODE_SOFT_RIGHT"
    ID = "null"


class KEYCODE_STB_INPUT:
    NAME = "按键Set-top-box input"
    CODE = "KEYCODE_STB_INPUT"
    ID = "null"


class KEYCODE_STB_POWER:
    NAME = "按键Set-top-box power"
    CODE = "KEYCODE_STB_POWER"
    ID = "null"


class KEYCODE_SWITCH_CHARSET:
    NAME = "按键Switch Charset modifier"
    CODE = "KEYCODE_SWITCH_CHARSET"
    ID = "null"


class KEYCODE_SYM:
    NAME = "按键Symbol modifier"
    CODE = "KEYCODE_SYM"
    ID = "null"


class KEYCODE_SYSRQ:
    NAME = "按键System Request / Print Screen"
    CODE = "KEYCODE_SYSRQ"
    ID = "null"


class KEYCODE_TV:
    NAME = "按键TV"
    CODE = "KEYCODE_TV"
    ID = "null"


class KEYCODE_TV_INPUT:
    NAME = "按键TV input"
    CODE = "KEYCODE_TV_INPUT"
    ID = "null"


class KEYCODE_TV_POWER:
    NAME = "按键TV power"
    CODE = "KEYCODE_TV_POWER"
    ID = "null"


class KEYCODE_WINDOW:
    NAME = "按键Window"
    CODE = "KEYCODE_WINDOW"
    ID = "null"


class KEYCODE_UNKNOWN:
    NAME = "未知按键"
    CODE = "KEYCODE_UNKNOWN"
    ID = "null"
