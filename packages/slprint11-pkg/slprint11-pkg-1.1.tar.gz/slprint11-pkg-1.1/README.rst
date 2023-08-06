Slowprint
=========

This is simple module that objective is displays a animated text on the
terminal.

| The module has only one function called ``slowprint ()`` that imposes
  a fixed time interval between the display of each character. The
  display can be vertically or horizontally.
| The text can also be displayed in the *yoyo* mode where after the last
  character is displayed the text is removed regressively by means of a
  fixed interval of time between the deletion of each character.

Use:
----

.. code-block:: python
   
   >>>from slprint.slowprint import slowprint
   >>>
   >>>slowprint ("Hello World my friend.", delay = 0.05, yoyo = True, vertical = True)
   >>>slowprint ("Hello World my friend.", delay = 0.05, yoyo = True, vertical = False)
   >>>slowprint ("Hello World my friend.", delay = 0.05, yoyo = False, vertical = True)
   >>>slowprint ("Hello World my friend.", delay = 0.05, yoyo = False, vertical = False)

Parameters:
-----------

| ``text``
| The text to be displayed on the terminal.
| ``delay``
| The time in seconds between the display of each character. Default is
  0.2 seconds.
| ``yoyo``
| If True after displaying the last character, it begins to remove
  character by character regressively. Default is False.
| ``vertical``
| If True displays the text vertically, if False displays the text
  horizontally. Default is False.

Copyright (c) 2020 Ronaldo Augusto Vasques de Souza