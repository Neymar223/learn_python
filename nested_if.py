has_ticket= True
has_id= False
has_vip= True
 
if has_ticket:
    if has_id:
        print("wtach th show")
    else :
        print("id is required")

else:
    if has_vip:
        print("Watch the show")
    else:
        print("No Vip NO Ticket")
    print("Please Buy tickets")