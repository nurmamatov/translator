def append():
    import colorama as color
    with open("Other_files/baza.txt","a") as f:
                eng_to_uzb = int(input("1.eng to uzb\n2.uzb to eng\n>>>> "))
                if eng_to_uzb==1:
                    eng=input(color.Fore.GREEN+"eng so'zni kiriting: ")
                    uzb=input(color.Fore.CYAN+"uzb so'zni kiriting: ")
                    f.write('\n'+eng+' '+uzb+'\n')
                    print(color.Fore.MAGENTA+"ma'lumot saqlandi!")
                    print(color.Fore.RESET)
                elif eng_to_uzb==2:
                    uzb=input(color.Fore.CYAN+"uzb so'zni kiriting: ")
                    eng=input(color.Fore.GREEN+"eng so'zni kiriting: ")
                    f.write('\n'+eng+' '+uzb+'\n')
                    print(color.Fore.MAGENTA+"ma'lumot saqlandi!")
                    print(color.Fore.RESET)
                else:
                    print(color.Fore.RED+"siz xato ma'lumot kiritdingiz")