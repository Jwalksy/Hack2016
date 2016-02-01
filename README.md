# Hack2016

We built this IOS app at HackRice 2016, winning the Best Community Hack Award. This app visualizes the dishes on the restaurant menu by simply taking and cropping a photo on the phone. I built the front-end IOS with Swift.

Inspiration
Have you ever felt awkward and embarrassed in a foreign food restaurant, because you do not understand the menu? Menuer is designed to help people make orders in restaurants with entree names that are not familiar to them.
Nothing would better explain the food than a top-ranked image search result of the entree name using Microsoft Bing Image Search.

What it does
 Menuer would allow users to take a photo of the menu they are trying to understand, then select the specific entree name they are looking for, and search on Microsoft Bing Image. And it would display a picture of the top-ranked result.
It works with all kinds of food around the world, as long as the food name is presented in Alphabetic letters.

How we built it
We used swift to develop our front-end on IOS, Node.js as the back-end, using AWS hosting the service, and Microsoft Bing API for Image Search.
Challenges we ran into
 We had several cosmetic problem in building the IOS app, mainly due to a lack of familiarity with the language. Also, linking front-end and back-end had a lot of miscellaneous work to do. Also, there were a lot of configuration to be set hosting the app using AWS.
Accomplishments that we're proud of
 We were able to take photo of the menu, and instantly crop out of the relevant text, doing a huge amount of OCR preprocessing with a click of the finger. Also, our OCR is near 100% accurate, and the image search result all came back super relevant.
What we learned
Teamwork, Swift, Node.js, Hosting Web Service, OCR.
What's next for HackRice2016-Menuer-Swift
 Cosmetic improvements, and finding the right OCR for other languages, for example: Chinese, Russian, Japanese...
Built With
swift
node.js
python
amazon-web-services
microsoft-bing-api

Demo -- https://www.youtube.com/watch?v=fdZ03uAcn0A
