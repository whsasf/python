#!/usr/bin/env python3

with open('guest.txt','a') as file_object:
    while True:
        guest_name=input('please input the guest name: ')
        if guest_name.strip() == 'quit':
            break
        file_object.write(guest_name+"\n")
    