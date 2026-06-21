# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- When openning the game I expected there would be an input box for user to type the number first but there was a developer debug info drop down list right under the requirement of the game which showed the secret anser and other information about the current game play which ruined the purpose of the game. There is another bug which is the hint. The hint are very weird and got mixed up whether the number user guest is higher or slower than the secret number and within the range of the requirement, which makes it more difficult for me to guest the correct answer. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 3     | Go higher         | Go higher       | Go higher              |
| 5     | Go higher         | Go lower        | Go lower               |
| 10    | Go higher         | Go lower        | Go lower               |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).



- I used Claude to assist me with this project
- So after I identified the bugs which are the high/low logic hints and out of range guesses. I asked Claude to help me identify the location of the code then asked how can I fix it. Claude helped me understand the logic and how every element related to each other so I can learn while fixing the error. After first fixing, the game gives out correct hint result and make sure the user guess the number within the range.
- There was another bug I found pretty annoying is that you have to click on the submit button twice to put the guess in the history and second time is to make the attempt counted. I asked Claude to help with the same method as above but then Claude changed the layout of the buttons, which I have to change it back myself.
- I verify each result by testing the game and make sure it runs logically.


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?


- The bug was really fixed when I play the game myself to check if the hints, submit button updated correctly.
- I just run "python -m streamlit run app.py" manually to test the game. Claude also helped me created the pytest to confirm the scoring logic return the right output for each test case.
- Yes, AI helped me understand the game logic and code structure better when I ask it to explain the code to me. 


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

- Reruns happen when a user clicks a button or interact with anything, Streamlit will reruns the entire Python script form top to bottom.
- Session state works like a memory to keep track of the score/process so tehy don't reset after each rerun (Like the History part in this game)

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
