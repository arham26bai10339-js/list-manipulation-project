 List Manipulation
print("\t\t\t\t\t\t##############################################")
print("\t\t\t\t\t\t##############################################")
print("\t\t\t\t\t\t##############################################")
print("\t\t\t\t\t\t##############################################")
print()
print("\t\t\t\t\t\t\t*****LIST MANIPULATION*****")
print("\t\t\t\t\t\t*****Designed and maintained by:")
print("\t\t\t\t\t\t*** Arham Pathan – 26BAI10339***")
print()
print("\t\t\t\t\t\t##############################################")
print("\t\t\t\t\t\t##############################################")
print("\t\t\t\t\t\t##############################################")
print("\t\t\t\t\t\t##############################################")
ch=input("press enter to continue")
print()
print("\t\t\t\t\t\tThis is a Python Program which can help you to MANAGE LIST")
print("\t\t\t\t\t\tThis can help you to manipulate the elements of the list")
print("\t\t\t\t\t\tThis can help you to add elements to the list")
print("\t\t\t\t\t\tThis can help you to delete the elements of the list")
print("\t\t\t\t\t\tThis can help you to modify the elements of the list")
print("\t\t\t\t\t\tHope this project work can make your work easier :)")
ch=input("press enter to continue")
print()
a=[]
while True:
    print("\t\t\t\t\t\t----MAIN MENU----")
    print()
    print("\t\t\t\t\t\t** 1-Enter list **")
    print("\t\t\t\t\t\t** 2-Display list **")
    print("\t\t\t\t\t\t** 3-Search an element **")
    print("\t\t\t\t\t\t** 4-Add **")
    print("\t\t\t\t\t\t** 5-Update element **")
    print("\t\t\t\t\t\t** 6-Delete **")
    print("\t\t\t\t\t\t** 7-Sort list **")
    print("\t\t\t\t\t\t** 8-Display max/min value **")
    print("\t\t\t\t\t\t** 9-Exit **")
    ch = input("Enter a choice :")
    if ch=='1':
        a=eval(input('Enter a list :'))
        print()
        print('You entered the list -', a)
    elif ch=='2':
        print('The list is :\n', a)
 elif ch=='3':
        c=eval(input('Enter an element to search :'))
        if c in a:
            print('The element is at the index - ',a.index(c))
        else:
            print('The element is not in the list')
        conti=input('Press any key to continue...')
 elif ch=='4':
        while True:
            print()
            print('1 - To add an element at the end')
            print('2 - To add mutiple elements at the end')
            print('3 - To add elements in between the list')
            print('4 - Exit')
            print()
            ch4= input('Enter your choice :')
            if ch4 == '1':
                ch4a = eval(input('Enter the element to add at the end of the list :'))
                a.append(ch4a)
                print()
                print('The list is - \n' , a)
                print()
                conti=input('Press any key to continue...')
            elif ch4 =='2':
                ch4b = eval(input('Enter the list of mutiple elements to add at the end of the list'))
                a.extend(ch4b)
                print()
                print('The list is - \n', a)
                print()
                conti=input('Press any key to continue...')
            elif ch4=='3':
                ch4c = int(input('Enter the index where you want to add -'))
                ch4d = eval(input(f'Enter the element which you want to add at index {ch4c} -'))
                a.insert(ch4c, ch4d)
                print()
                print('The list is - \n', a)
                print()
                conti=input('Press any key to continue...')
            else:
                break
        #At the end (Append)
        #Multiple elements at the end (Extend)
        #ELemnent in between the list (Insert)
        #Exit choice
        #Run in while loop
        #Print the
list at each if stataements
  elif ch=='5':
        ch5a = int(input('Enter the index at which you want to update the element -'))
        ch5b = eval(input('Enter the element to replace :'))
        if len(a)> ch5a :
                a[ch5a] = ch5b
                print('The list is - \n', a)
                print()
        #Ask index at which to update
        #ASk the element name
elif ch=='6':
        while True:
            print()
            print('1 - To delete an element by index')
            print('2 - To delete an element by value')
            print('3 - To clear the list')
            print('4 - Exit')
            print()
            ch6a = input('Enter your choice :')
            if ch6a == '1':
                ch6b = int(input('Enter the index - '))
                if len(a)>ch6b :
                    a.pop(ch6b)
                    print()
                    print('The list is - \n', a)
                    print()
                    conti=input('Press any key to continue...')
            elif ch6a == '2':
                ch6c = eval(input('Enter the element to delete - '))
                if ch6c :
                    a.remove(ch6c)
                    print()
                    print('The list is \n', a)
                    print()
                    conti=input('Press any key to continue...')
                else:
                    print('the element is out of index')
                    print()
            elif ch6a == '3':
                a.clear()
                print()
                print('The list is -', a)
                print()
                conti=input('Press any key to continue...')
            else:
                break
elif ch=='7':
                while True:
                    print()
                    print('1 - To sort the list in ascending order')
                    print('2 - To sort the list in descending order')
                    print('3-Exit')
                    print()
                    ch7 = input('Enter your choice:')
                    if ch7=='1':
                        a.sort()
                        print('Ascending order :', a)
                    elif ch7=='2':
                        a.sort(reverse=True)
                        print('Descending order :',a)
                    elif ch7=='3':
                        break
                    else :
                        conti = input('Press any key to continue')
        #Ascending order
        #Descending order
        #Exit
        #Run in while loop
elif ch=='8':
        print()
        print('Maximum value :', max(a))
        print('Mimimum value :', min(a))
        print()
        conti = input('Press any key to continue')
elif ch=='9':
	  print('Thank you for using this python program')
        break
    else:
        print('** INVALID CHOICE **')
