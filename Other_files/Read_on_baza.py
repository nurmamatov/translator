def tarjimasi():
    import colorama as color
    from Other_files import Append_to_baza as app
    with open("Other_files/baza.txt","r") as f:
        all_translate=f.read().split()
        tanlov = int(input("1.eng to uzb\n2.uzb to eng\n>>>> "))
        if tanlov==1:
            soz=input(color.Fore.GREEN+"eng so'zni kiriting: ")
            print(color.Fore.RESET)
            if soz in all_translate:
                if all_translate.count(soz)==1:
                    for i in  range(0,len(all_translate),2):
                        if all_translate[i]==soz:
                            print(color.Fore.YELLOW+all_translate[i+1])
                            print(color.Fore.RESET)
                            break
                elif all_translate.count(soz)>=2:
                    h=0
                    for i in range(all_translate.count(soz)):
                        while h!=len(all_translate):
                            if all_translate[h]==soz:
                                print(color.Fore.YELLOW+all_translate[h+1])
                                print(color.Fore.RESET)
                                h+=2
                                break
                            h+=2
            elif not(soz in all_translate):
                qoshish_tanlov=int(input("bunday so'z yo'q ekan shu so'zni qo'shishni hohlaysizmi?\n1.ha\n2.yo'q\n>>>>"))
                if qoshish_tanlov==1:
                    app.append()
                else:
                    print("Ok!")
        elif tanlov==2:
            soz=input(color.Fore.GREEN+"uzb so'zni kiriting: ")
            if soz in all_translate:
                if all_translate.count(soz)==1:
                    for i in  range(1,len(all_translate),2):
                        if all_translate[i]==soz:
                            print(color.Fore.YELLOW+all_translate[i-1])
                            print(color.Fore.RESET)
                            break
                elif all_translate.count(soz)>=2:
                    h=1
                    for i in range(all_translate.count(soz)):
                        while h!=len(all_translate):
                            if all_translate[h]==soz:
                                print(color.Fore.YELLOW+all_translate[h-1])
                                print(color.Fore.RESET)
                                h+=2
                                break
                            h+=2
            elif not(soz in all_translate):
                qoshish_tanlov=int(input("bunday so'z yo'q ekan shu so'zni qo'shishni hohlaysizmi?\n1.ha\n2.yo'q\n>>>>"))
                if qoshish_tanlov==1:
                    app.append()
                else:
                    print("Ok!")
