# HelpMeWithMyMood
An entry into the IBMHackChallenge 2018

With the advances in technology about sentiment analysis and predictive analytics, it has opened many avenues for researchers and enterprises to understand human mental state better. The proposed challenge is to know the emotion/mood of a person, to help in eliminating any negative state of mind that might have adverse effect on his/her daily life.

## Working

- HelpMeWithMyMood uses twitter authentication to let users sign in.
- Once a user has signed in, their twitter handle is used to collect their tweets.
- The tweets are passed to Watson NLU analisis and the emotion with most score between -1 and 1 is selected as the emotion the user is feeling at that time.
- Based on the emotion, suggestions are given to uplift the mood.

## Set up

To set up the dependencies, you need python 3.X and mongoDB

To install python dependencies

```
    pip3 install -r requirements.txt
```

To start the application

```
    python __init__.py
```