import random
#Chatbot for recalling The Office quotes

def generate_quotes(user_input):
  quotes = [
    "Sometimes I’ll start a sentence and I don’t even know where it’s going. I just hope I find it along the way. – Michael Scott (Season 5)",
    "I talk a lot, so I’ve learned to tune myself out. – Kelly Kapoor (Season 7)",
    "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me. – Michael Scott (Season 2)",
    "I’m not superstitious, but I am a little stitious. – Michael Scott (Season 4)",
    "If I don’t have some cake soon, I might die. – Stanley Hudson (Season 4)",
    "I am running away from my responsibilities. And it feels good. – Michael Scott (Season 4)",
    "If I were buying my coffin, I would get one with thicker walls so you couldn’t hear the other dead people. – Dwight Schrute (Season 2)",
    "And I knew exactly what to do. But in a much more real sense, I had no idea what to do. – Michael Scott (Season 5)",
    "There’s a lot of beauty in ordinary things. Isn’t that kind of the point? – Pam Beesly (Season 9)",
    "I wish there was a way to know you’re in the good old days, before you’ve actually left them. – Andy Bernard (Season 9)",
    "I live by one rule: No office romances, no way. Very messy, inappropriate…no. But, I live by another rule: Just do it… Nike. – Michael Scott (Season 1)",
    "’R’ is among the most menacing of sounds. That’s why they call it ‘murder’ and not ‘mukduk.’ — Dwight Schrute (Season 6)",
    "I am Beyoncé, always. – Michael Scott (Season 6)",
    "I’m not usually the butt of the joke. I’m usually the face of the joke. – Michael Scott (Season 6)",
    "The rules of shotgun are very simple and very clear. The first person to shout ‘shotgun’ when you’re within sight of the car gets the front seat. That’s how the game’s played. There are no exceptions for someone with a concussion. – Michael Scott (Season 2)",
    "Did I stutter? – Stanley Hudson (Season 4)",
    "I’m an early bird and I’m a night owl, so I’m wise and have worms. – Michael Scott (Season 2)",
    "I don’t care what they say about me, I just wanna eat. Which I realize is a lot to ask for. At a dinner party. – Pam Beesly (Season 4)",
    "Guess what, I have flaws. What are they? Oh, I don’t know. I sing in the shower. Sometimes I spend too much time volunteering. Occasionally I’ll hit somebody with my car. So sue me. – Michael Scott (Season 4)",
    "You all took a life here today. You did. The life of the party. – Michael Scott (Season 5)",
    "I have a lot of questions. Number one, how dare you? – Kelly Kapoor (Season 4)",
    "This is a dream that I’ve had…since lunch…and I’m not giving it up now. – Michael Scott (Season 5)",
    "Do I need to be liked? Absolutely not. I like to be liked. I enjoy being liked. I have to be liked. But it’s not like a compulsive need to be liked. Like my need to be praised. – Michael Scott (Season 4)",
    "Whenever I’m about to do something, I think, ‘Would an idiot do that?’ And if they would, I do not do that thing. – Dwight Schrute (Season 3)",
    "People underestimate the power of nostalgia. Nostalgia is truly one of the greatest human weaknesses, second only to the neck.  — Dwight Schrute (Season 9)",
    "Why are you the way that you are? — Michael Scott (Season 2)",
    "Fact: Bears eat beets. Bears. Beets. Battlestar Galactica. – Jim Halpert (Season 3)",
    "There are always a million reasons not to do something. – Jan Levinson (Season 2)",
  ]
  return random.choice(quotes)


def init_chat():
  quit_character = 'q'

  user_input = input("Hello! Let's remember funny or inspirational quotes from the tv show, The Office! Press q whenver you are done!")

  while user_input != quit_character:
    
    user_input = input(generate_quotes(user_input) + "\n")

if __name__ == "__main__":
  init_chat()