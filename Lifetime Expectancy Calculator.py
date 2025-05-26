while True:
  Score = 0
  print("This will be a life expectancy calculator quiz. 10 questions will be asked, and you must respond honestly to the question. We will not store any data")
  print("Are you a male or female")
  print("a) Male")
  print("b) Female")
  user_input = input("Your answer: ")
  if user_input.lower() == "a":
    Score = Score + 1
    print("On a scale of 1 to 10 (1 being extremely skinny/extremely obese and 10 being perfect), where would you or your doctor place you?")
    user_input = input("Your answer: ")
    Score = Score + int(user_input)
    print("Do you wear a seatbelt while driving?")
    print("a) Yes")
    print("b) No")
    user_input = input("Your answer: ")
    if user_input.lower() == "a":
      print("Do you smoke?")
      print("a) Every day")
      print("b) I used to")
      print("c) I never have")
      print("d) Every so often")
      user_input = input("Your answer: ")
      if user_input.lower() == "a":
        Score = Score + 1
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-70 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 45 years)")
      elif user_input.lower() == "b":
        Score = Score + 3
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "c":
        Score = Score + 5
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "d":
        Score = Score + 2
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
    elif user_input.lower() == "b":
      print("Do you smoke?")
      print("a) Every day")
      print("b) I used to")
      print("c) I never have")
      print("d) Every so often")
      user_input = input("Your answer: ")
      if user_input.lower() == "a":
        Score = Score + 1
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "b":
        Score = Score + 3
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "c":
        Score = Score + 5
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "d":
        Score = Score + 2
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
  elif user_input.lower() == "b":
    Score = Score + 2
    print("On a scale of 1 to 10 (1 being extremely skinny/extremely obese and 10 being perfect), where would you or your doctor place you?")
    user_input = input("Your answer: ")
    Score = Score + int(user_input)
    print("Do you wear a seatbelt while driving?")
    print("a) Yes")
    print("b) No")
    user_input = input("Your answer: ")
    if user_input.lower() == "a":
      print("Do you smoke?")
      print("a) Every day")
      print("b) I used to")
      print("c) I never have")
      print("d) Every so often")
      user_input = input("Your answer: ")
      if user_input.lower() == "a":
        Score = Score + 1
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "b":
        Score = Score + 3
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "c":
        Score = Score + 5
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "d":
        Score = Score + 2
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
    elif user_input.lower() == "b":
      print("Do you smoke?")
      print("a) Every day")
      print("b) I used to")
      print("c) I never have")
      print("d) Every so often")
      user_input = input("Your answer: ")
      if user_input.lower() == "a":
        Score = Score + 1
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "b":
        Score = Score + 3
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "c":
        Score = Score + 5
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
      elif user_input.lower() == "d":
        Score = Score + 2
        if Score > 17:
          print("\033[1;34;40m You will probably live a long life, most likely over 100 years old")
        elif Score > 10 and Score < 17:
          print("\033[1;34;40m You will most likely live an average life, maybe about 90 years old")
        elif Score > 5 and Score < 10:
          print("\033[1;34;40m You will not live a very long life, unfortunately (Maybe 50-80 years)")
        elif Score == 4 or Score < 4:
          print("\033[1;34;40m You will have a very short life (maybe 40 years)")
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
          
        elif Score == 4 or Score < 4:
          print("You will have a very short life (maybe 40 years)")
          
        