# Final Project Milestone #2

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 6). 

Let's decide on our Final project. Select the idea from Milestone 1 that seems the most interesting to you.

Each class is a model of some real world object. We often refer to data classes as the ***models*** in a GUI program. Your models represent your application data.

Given what you have learned about classes on Chapter 6, describe the ***interface only*** of 3 classes you think you might need for your project.

*For example*, if you want to create a space invaders type game, you would need a class to represent the ship, which could have an interface such as: 

* class ship
    * moveLeft()
    * moveRight()
    * shoot()

***

Come up with interfaces fot 3 possible classes you think you may need. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

For the first interface, the main character would be the main. Through this, I am thinking to use the class to establish the appareance of the main character with a color and an image. After it is the turn of its actions, there would be its directions when the program is running, considering a life counter with 3 lifes, and its special attack; the character creates a line that circle enemies once anyone is in the circle, then all inside would receive damage.  
class Main_character:
 1) appareance:
    * image      
    * color
    * name
 2) functions:
    * directions
    * life counter(3)
    * creation of Loop (attack)

## Class Interface 2

Then I am planning to make another interface for the enemies in base of the main character interface. 
class Enemies:
1) appareance:
   * color
   * image

2) functions:
   * motion pattern
   * location of enemies
   * resistance 


## Class Interface 3

At final, this class would be for secondary elements that are part from the setting, planning to be another obstacles to the user during the game, either be a visual or a an impediment. Such as this example that shows how shinning stars could be a support or a danger according to the color.
class Secondary_elements:
1) setting_stars:
   * color
   * size
   * position
2) Lasers:
   * shoots
   * range of attack movements
   


