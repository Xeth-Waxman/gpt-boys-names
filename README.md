# gpt-boys-names
Taking a more incremental step to working with ChatGPT

Based on my previous attempts - which failed - at using ChatGPT to write a fairly sophisticated stock trading application, I decided to take a step and take things more incrementally. This project is based on the following prompt:

> Using python 3.10, I want to create a text file that contains 100 boys' names that are popular in the United States. I would like the file to contain two columns - one with the spelling of the name, and one with the phonetical pronunciation of the name.

I'll then iterate on this quote, asking ChatGPT to correct errors as they come up - because honestly, ChatGPT isn't a very good developer, despite the hype.

# Project Conclusion
Ultimately I got ChatGPT to create a working application. I tried to get ChatGPT is use the epitran library to create phonetic pronounciations that westerners were more familiar with; however, it continuously failed to be able to generate code that could handle the differehnce between strings and lists of strings. It was particular bad at handling empty-length strings, something that I'm noticing is a pattern. My take away so far is that ChatGPT is good at giving a developer a starting point, but really struggles with helping developers take it beyond the 60% complete mark.

However, I would not bet against AI!