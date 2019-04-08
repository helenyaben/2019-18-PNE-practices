"""
1. <FORM ELEMENT>

The HTML <form> element defines a form that is used to collect user input. This element formally defines a form.
It is a container like <div> or <p>, but it also supports some specific attributes to configure the way the form behaves.
All its attributes are optional but it is considered a good practice that always at least the action and method attributes
are present.

- The action attribute defines the location (a URL) from where the information collected by the form should be sent.
If the action attribute is omitted, the action is set to the current page.

- The target attribute: the target attribute specifies if the submitted result will open in a new browser tab, a frame,
or in the current window. The default value is "_self" which means the form will be submitted in the current window.
To make the form result open in a new browser tab, use the value "_blank":

- The method attribute defines with which HTTP method the information will be sent (it can be "get" or "post").
When GET is used, the submitted form data will be visible in the page address field. Always use POST if the form data
contains sensitive or personal information. The POST method does not display the submitted form data in the page address field.

They always start and end with the <form> element:

<form>

form elements

</form>

An HTML form contains form elements.

Form elements are different types of input elements, like text fields, checkboxes, radio buttons, submit buttons,
and more.

2. <INPUT ELEMENTS>

The <input> element is the most important form element.

The <input> element can be displayed in several ways, depending on the type attribute:

(1) <input type="text">	    Defines a one-line text input field
(2) <input type="radio">    Defines a radio button (for selecting one of many choices)
(3) <input type="submit">	Defines a submit button (for submitting the form)


"""