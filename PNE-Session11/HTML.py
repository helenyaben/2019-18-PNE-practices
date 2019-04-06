'''

INTRODUCTION TO HTML: https://www.w3schools.com/html/html_intro.asp

HTML is the standard markup language for creating Web pages.

-HTML stands for Hyper Text Markup Language.
-HTML describes the structure of Web pages using markup.
-HTML elements are the building blocks of HTML pages.
-HTML elements are represented by tags.
-HTML tags label pieces of content such as "heading", "paragraph", "table", and so on.
-Browsers do not display the HTML tags, but use them to render the content of the page.

This is the HTML code for the green server we used in the previous example (green-server.html)

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Green server</title>
  </head>
  <body style="background-color: lightgreen;">
    <h1>GREEN SERVER</h1>
    <p>I am the Green Server! :-)</p>
  </body>
</html>

1. HTML documents should always start with the special tag: <!DOCTYPE html>. This declaration declaration defines this
document to be HTML5.
2. The rest of the html code is inside the <html> and </html> tags.
3. Every html document consist of two parts: the head and the body:
- HEAD : it contains information about the document for the browser.
- TITLE: it specifies a title for the document.
- BODY: it contains the actual content that is going to ve visible for the browser. In this example there are two elements
inside the body:
 -The heading: GREEN SERVER. It is a bigger text
 -A paragraph: "I am the green server"

The background color of the elements in the body is set inside the style attribute.

HTML TAGS

HTML tags are element names surrounded by angle brackets: <tagname> content goes here... </tagname>

'''