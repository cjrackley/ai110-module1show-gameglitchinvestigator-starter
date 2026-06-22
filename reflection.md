# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|hitting new game | reset attempts| carries over attempts from previous game | no external error, console outputs "ran out of attempts, game won" if won or out of attempts|
| changing difficulty| reset attempts and change difficulty | changes difficult but does not reset attempts, causing negative attempts in some instances | same as previous bug |
|inputting an attempt | shows up within debug history and changes attempt remaining| first input does neither of these, instead it accepts the input and waits until next input to update history and count | Causes visual error that causes the attempts remaining count to be 1 behind, ending on 1 remaining|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used claude code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). When looking for possible bugs, I asked claude to point out any bugs it could find. It was able to find the bugs I had already found link hints being incorrect and points not being accurate. It was also able to find out exactly why the game wasn't allowing new attemps on a new game after using all attempts during the previous game. It had pointed out that the attempts weren't being cleared for the new game, which it fixed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). When asking to generate a pytest for the in test_game_logic.py, within my directory the file is under tests and while reading the instructions it said "generate a pytest case in test/test_game_logic.py" i typed test instead of tests and it made a whole new folder for test. There weren't any other times claude did something I wasn't expecting it to do.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? Tested 3-4 cases to try and replicate the bug. once I fixed all bugs, claude generated a pytest that passed all testcases.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. When fixing the bug that didn't allow new games to be played if all attempts from previous game, I tested a few different cases. After losing a game, start new game. After using 2 attempts, start new game. After using an attempt, switch game difficulty. Once figuring out the attempts were not resetting, i asked claude to locate the code that would cause this issue, and allow fixes. After testing and confirming the cases worked as intended, I moved on to the next bug.
- Did AI help you design or understand any tests? How? I didn't fully understand the point system for the game. I understood that the point system was off as it would give negative points but I didn't really know what determined the point system. Claude helped describe the logic behind the point system and gave test cases that showed this logic.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? It's similar to React, it gives a preview or working model of the application being made. It allows for realtime updates, so changes can be seen within a few seconds rather than having to save and re run the entire app.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
