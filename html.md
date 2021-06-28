# HTML aka HyperText Markdown Language

HTML is the programming languaged used to define the structure of web pages. 

### Wireframing

Wireframes are the basic outlines for conceptualizing a website before writing any code. 

Wireframes are usually drawn out with sharpie and paper or a marker and white-board to decide on the layout of a site with only bare bones information. They are for formatting only and are meant to be basic. Truly less is more here!

Wireframes can be made by doing client research, creating the wireframe with an idea for how clients will flow through the site, and creating a bare-bones sketch of what is expected from the website. After the basic wireframe is created, it can be reviewed with your team and the client before being madee into a prototype.

Remember to keep things clear and simple!


### Writing and Understanding HTML

ELements are the building blocks of writing HTML. They are built of teh opening tag, the content, and the closing tag. If you notice in the heading example below, the opening and closing tags are nearly the same except for a backslash in the closing tag.
/<h1> My Website </h1>

Elements can also have attributes which are essentially more details about how the elements will be used in the structure. Attributes can have notes or directions for the design of the site. Attributes can have their own formatting and reside in the tags. For example, in an opening tag for the heading we can have /<h1 height="200"> An attribite needs a space between the opening element name and the attribute, an equals sign and the attribute value surrounded by quotation marks.

Elements are nested which means can be thought of as ravelling and unravelling your code. Whatever elements sections are opened through the opening tags also need to be closed through closing tags. Also importantly, elements that are opened need to be closed in reverse order properly so that your website will look as expected. The different layers of code are also indented for ease of reading, so some code for a section may look like the following:

- /<main>
-   /<p>
-       /<ul>
-            /<li>
-                Item 1
-            /</li>
-       /</ul>
-    /</p>
- /</main>

Some elements, called empty elements, do not need closing tags. The Img tag is one example. 

Common tags needed to create content:
- <html> Which wraps all of the content on the entire page
- <head> for CSS or design information
- <h1> Headings 1-6 are used to lead sections
- <p> Paragraph tags are used to group content
- <ul> For lists
- <li> For List Items
- <img> For images
- <a> For Adding links /(This commonly has the attribute href and the link witth it).


### Semantics in HTML
Essentially semantics tell your code what certain parts of your website mean. This can help search engines find and display the most important parts of your site!

They are also important because they help with your website's formatting as things are formatted based on the category they call into. 

Some examples of common semantic element tags are:
- /<article> 
- /<body>
- /<footer>
- /<h1> Which is for section headings
- /<header> 
- /<main> 
- /<nav>
- /<section> 
- /<summary> 
- /<title> 
 
[Reading Notes Home Page](README.md)
s