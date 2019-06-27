# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a dark forrest.
A sign is hanging from the branch: "You have one hour dont look back ."
To your left you can see a dark abandond house, and to your right you see a light in the distance.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decide to go left and...")
    print(
    '''
    An abandond house stands before you. There is no light coming from inside, as shown by the broken windows.
    The door is slightly open do you enter?
    '''
    )
    print(y/n)
    user_input = input()
    if user_input == "y":
        print(
        '''
        As you step over the threshol the door slams behind you. Something tells you that you've made a mistake.
        You feel across the wall as you search for a light switch.
        When you flip the switch, the room fills with light 
        '''
        )

    # Continue code to finish story.
