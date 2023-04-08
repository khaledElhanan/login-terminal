from pystyle import *

print(Box.Lines(" [+] Welcom Khaled Abd_Elhanan "))

Write.Print('[+] This Program For login page \n\n',
            Colors.purple_to_red, interval=0.1)
Write.Print('Write User Name and Password \n\n',
            Colors.purple_to_red, interval=0.1)

print(Box.DoubleCube('Example 1'))

while True:
    user_name = Write.Input(
        'Enter user name : ', Colors.blue_to_green, interval=0.1)
    pass_Word = Write.Input(
        'Enter Password : ', Colors.blue_to_green, interval=0.1)
    if user_name == "khaled" and pass_Word == '1234':
        Write.Print('[+] Welcom Admin \n', Colors.green, interval=0.1)
        input('\n press any key to exit ... ')
    else:
        if user_name != "khaled" and pass_Word == '1234':
            Write.Print('[-] Error User name is False \n\n ',
                        Colors.red, interval=0.1)
        elif pass_Word != '1234' and user_name == 'khaled':
            Write.Print('[-] Error Password is False \n\n ',
                        Colors.red, interval=0.1)
        else:
            if user_name != 'khaled' and pass_Word != '1234':
                Write.Print('[-] Error Try again  \n\n ',
                            Colors.red, interval=0.1)