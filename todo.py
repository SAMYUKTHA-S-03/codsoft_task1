d={}
print('\t\t\t\t\tTO-DO LIST MENU DRIVEN PROGRAM')
print('\t\t\t\t\t**************************************************')
while True:
    print("\t\t\t\tMENU")
    print("\t\t\t\t********")
    print("\t\t\t\t1)Enter a new task")
    print("\t\t\t\t2)Update the tasks")
    print("\t\t\t\t3)Track the tasks")
    print("\t\t\t\t4)remove task")
    print("\t\t\t\t5)exit")
    a=int(input("\t\tenter your choice"))
    if a==1:
        task=input("\t\tenter the tasks")
        pro=input("\t\tenter the current status of the task:")
        d[task]=pro
        print("\t\t\t\tTASK ADDED IN TO-DO LIST")
    elif a==2:
        if d=={}:
            print('\t\t\t\tTHE TO-DO LIST IS EMPTY')
        else:
            print("\t\t\t\tTO-DO LIST")
            print("\t\t\t\t***************")
            print("\t\t\tTASK","\t\t",'STATUS OF COMPLETION')
            for i in d:
                print('\t\t\t',i,"\t\t\t",d[i])
                task=input("\t\tenter the task to be updated/ name of the task:")
            if task not in d:
                print("\t\t\tplease enter a valid task")
            else:
                pro=input("\t\tenter the updated task status")
                print("\t\t\tTASK STATUS UPDATED")
                d[task]=pro
    elif a==3:
        if d=={}:
            print('\t\t\t\tTHE TO-DO LIST IS EMPTY')
        else:
            print("\t\t\t\tTO DO LIST")
            print("\t\t\t\t***************")
            print("\t\t\tTASK","\t\t",'STATUS OF COMPLETION')
            for i in d:
                print('\t\t\t',i,"\t\t\t",d[i])
    elif a==4:
        if d=={}:
            print('\t\t\t\tTHE TO-DO LIST IS EMPTY')
        else:
            print("\t\t\t\tTO DO LIST")
            print("\t\t\t\t***************")
            print("\t\t\tTASK","\t\t\t","STATUS OF COMPLETION")
            for i in d:
                print('\t\t\t',i,"\t\t\t",d[i])
            a=input("\t\tenter the task to be removed")
            if a in d:
                del d[a]
                print("\t\t\tTASK REMOVED FROM TO-DO LIST")
            else:
                input("\t\t\tplease enter a valid task")
    elif a==5:
        print("\t\t\t\tEND OF MENU")
        print("\t\t\t\tPROGRAM TERMINATED")
        break
    else:
        print("\t\t\tPlease enter valid options")
