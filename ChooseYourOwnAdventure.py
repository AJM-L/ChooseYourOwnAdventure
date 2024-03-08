# AJ Matheson-Lieber
#
#
#

""" 
Title for your adventure:   Where am I?

"""

import time



def adventure():
    """This function runs one session of interactive fiction
       Well, it's "fiction," depending on the pill color chosen...
       Arguments: no arguments (prompted text doesn't count as an argument)
       Results: no results     (printing doesn't count as a result)
    """
    delay = 1.0
    def sheep_plot(var_pass = False):
        """
        prints a possible ending
        """
        if not var_pass:
            print("you decide to return to the sheep figuring it will be safer there")
            print("you hear a voice in the distance calling out, '", user_name, "!'")
            print("you look in the direction of th noise and see no one")
            print("but you hear the voice again, '", user_name, "!'")
            print("this time you see the source of the sound")
            time.sleep(delay*2)
            print("one of the sheep! they are calling your name")
            time.sleep(delay)
            print("you approach the sheep slowly")
            time.sleep(delay)
            print("but before you can get there")
            time.sleep(delay)
        
        print("the sheep lunges at you")
        time.sleep(delay)
        print("suddenly every sheep is hurling themselves at you")
        time.sleep(delay)
        print("you can feel the bones in your body cracking. you feel faint.")
        time.sleep(delay)
        print("you fall to the ground")
        time.sleep(delay)
        print("and finally, you feel nothing")
        time.sleep(delay)
        print("well fought adventurer, you were not meant to win")
        return
    def homestead():
        """
        prints a possible ending
        """
        time.sleep(delay)
        print("you sit back down and realize your surroundings are quite beautiful")
        time.sleep(delay)
        print("you look up at the great blue sky and watch the clouds slowly roll by")
        time.sleep(delay)
        print("you see the sheep meandering slowly through the field")
        time.sleep(delay)
        print("chewing on grass")
        time.sleep(delay)
        print("you see a small stream to your left")
        time.sleep(delay)
        print("you decide this place is not so bad after all and that you might just stay")
        time.sleep(delay)
        print("you get up and begin working on shelter")
        time.sleep(delay)
        print("you gather some sticks and branches from nearby trees and fashion a small A-frame camp")
        time.sleep(delay)
        print("you gather water from the stream and notice all kinds of fish swimming in the clear flowing water")
        time.sleep(delay)
        print("you feel content with your choice to stay here")
        time.sleep(delay)
        print("well done, ", user_name)
        return
    def something_went_wrong():
        time.sleep(delay)
        print("That was not an option. You FOOL. you cannot just say things.")
        time.sleep(delay)
        print("all things must have order")
        time.sleep(delay)
        print("they must have meaning")
        time.sleep(delay)
        print("you see the carefully constructed environment around you begin to flash in and out")
        time.sleep(delay)
        print("the sky turns to static")
        time.sleep(delay)
        print("the ground fails to render its grass")
        time.sleep(delay)
        print("you find yourself in an empty room adorned by ornate marble carvings")
        time.sleep(delay)
        print("you stand in front of what appears to be a mirror")
        time.sleep(delay)
        print("except it is not your reflection you see")
        time.sleep(delay)
        print("'WHAT HAVE YOU DONE!'")
        time.sleep(delay)
        print("'YOU ARE NOT SUPPOSED TO BE HERE!'")
        time.sleep(delay)
        print("the reflection seems to ba a man")
        time.sleep(delay)
        print("he is tall and dressed in pajama pants and a sweatshirt")
        time.sleep(delay)
        print("his face is red")
        time.sleep(delay)
        print("'Well? you aren't just going to stay there are you?'")
        return
    print("")
    print("upon your daily chores")
    print("you come across a wise old man in the alley.")
    print("you aproach him")
    print("his words flow from his mouth with delicate precision")
    print("")
    user_name = input("'Greetings traveler! Tell me, what shall I call you?'").upper()
    print("")
    if user_name == "AJ":
        response = input("'could the legends be true? is it really you AJ? The creator of this here adventure? The architect of the maze?'").upper()
        if "yes" in response:
            print("'well, then quite a day it is. This adventure should be easy for you.'")
        else: 
            print("")
            print("'Ahh, so you have been cursed with the expectation of greatness.'")
            print("'I see, that is a problem I know all too well'")
    
    print("'well, ", user_name, "please, take this potion of wisdom as a gift'")
    print()
    take = input("take the potion Y/N").upper()
    print("")
    if take == "Y":
        print("Great! Now drink up! you will need it for my next question")
        response = input("drink the potion Y/N").upper()
        print("")
        if response == "Y":
            print("you begin to feel lightheaded and dizzy")
            print("your vision goes black...")
        elif response == "N":
            print("well, I guess you do not have the courage necassary to complete this adventure")
            print("farewell stranger!")
            return
        else:
            return something_went_wrong()
    else:
        print("'Sorry, ", user_name, " but that is not an option'")
        print("before you can react the old man lunges at you")
        print("his wrinkly hands grab tight around your neck")
        print("you feel his nails digging into your skin")
        print("your vision goes black...")
    time.sleep(delay*2)
    print("")
    print("you wake up in a large field of sheep surrounded by tall hedges")
    action = input("You get up and A) walk towards the hedges or B) examine the herd of sheep").upper()
    
    if action == "B":
        print("You appraoch the herd of sheep")
        print("as you get closer you notice one of the sheep watching you closely")
        apr = input("do you approach this sheep? Y/N").upper()
        print("")
        if apr == "Y":
            time.sleep(delay)
            print("you approach the sheep carefully")
            print("you notice the sheep smiling")
            print("he seems to want something from you")
            print("'Hey you!' the sheep barks")
            expl = input("'what are YOU doing here?'").upper()
            if len(expl) > 25:
                print("'I aint reading all that'")
                print("good luck on your adventure!")
                return homestead()
            elif user_name in expl:
                print("'well met, ", user_name, "good luck on your adventure!'")
                return homestead()
            else:
                print("Oh! is that the case?")
                print("LIAR!")
                return sheep_plot(True)
        elif apr == "N":
            time.sleep(delay)
            print("you take a cautious step back to reevaluate your surroundings")
            nextmove = input("Do you A) aproach the hedges or B) sit back down and wait").upper()
            if nextmove == "A":
                action = "A"
            elif nextmove == "B":
                return homestead()
            else:
                return sheep_plot()
    if action == "A":
        print("As you approach the hedges, you notice something odd about the leaves")
        print("they seem to be ... flickering")
        touch = input("do you reach out and touch the leaves? Y/N").upper()
        print("")
        if touch == "Y":
            print("you reach towards one of the bigger leaves and gently touch it")
            time.sleep(delay)
            print("OUCH! you scream as a burning tingle shoots up your arm")
            print("Something isnt right about this place you think")
            time.sleep(delay)
            print("frightened, you want to run, but see nowhere to go.")
            print("You feel the urge to jump into the hedge to try and make your way through to the other side")
            death = input("do you charge at the wall? Y/N").upper()
            print("")
            if death =="Y":
                print("you charge headfirst at the hedge")
                time.sleep(delay)
                print("you feel the same shooting pains all over")
                time.sleep(delay)
                print("it hurtts, but you keep pushing through")
                time.sleep(delay)
                print("the agony of each moment makes makes each step feel like a mile")
                time.sleep(delay)
                print("eventually your arm breaks through to the other side")
                time.sleep(delay)
                print("then your face")
                time.sleep(delay)
                print("but as you try to make your first step into freedom")
                time.sleep(delay)
                print("your foot fails to contact the dirt")
                time.sleep(delay)
                print("right as you feel yourself falling, you wake up")
                time.sleep(delay)
                print("the wise man stands above you with a smile")
                time.sleep(delay)
                print("'welcome back' he says slyly")
                time.sleep(delay)
                print("You realize that you may not have what it takes to somplete this old mans adventure and you decide to return home")
                time.sleep(delay)
                print("farewell, ", user_name)
                return
            elif death == "N":
                print("you do not want to feel that pain again")
            else:
                return something_went_wrong()
            return sheep_plot()
        return sheep_plot()    
    return something_went_wrong()