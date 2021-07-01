# Cascading Style Sheets or How Websites Look Nice

CSS stands for Cascading Style Sheets. This is the language of computer pizzaz. This is really where the magic happens. After the content is applied in through the HTML language, a formatting page is applied to the site that tells the website how to display everything from the banners to the content with all of the styles colours and images that will bring your website to life.

Websites come with default formatting, but CSS gives the ability to personalize every detail. 

## Structure

CSS is essentially defining the rules for how the page will look, and of course there are rules for how it is written itself. For example, if you wanted the paragraph text in your page to be written in white you could write the following:

p {
   - color: white;

}

- The P in this case which refers to paragraph texts is called a **selector**.
- The curly brackets **{}** enclose the formatting that we are looking to define.
 - Inside are the properties we are looking to define which are called the **declarations**.
 - The object we are looking to define is called the **property**.
 - The assignment of the object in question is called the **value**. 
 - The property is placed before a colon, and a semicolon is placed after the value to complete the style.

 Altogether the style definitions will all be written on the CSS Stylesheet.


 ## Formatting and Priority
 
 CSS can be added to webpages in three ways:
 - External CSS has all of the stylesheet information in one file, usually used to edit a full webpage at once
 - Internal CSS has all of the stylesheet information, likely for one webpage, all at the top of the html for the page in question
 - Inline CSS has more specific formatting, usually for one confined part (or element )of one specific page. 
 -Priority is given to things that are written last if there is contradictory information in one CSS method, and then to Inline then Internal, then External stylesheets. 

 Color can be added to CSS stylesheets through different formats such as naming the color or using color symbols such as HEX, rga, rgba, or hsl.  


[Reading Notes Home Page](README.md)